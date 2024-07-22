from pathlib import Path
from attribute_split import attributes
import json
MOD_NAMESPACE = 'kubejs'  # TODO: Do the mod, kubejs' also an option

# CYCLE THROUGH THE CHARACTER FILES
# TODO: Verify folder path
for character_file in Path("characters").glob("*"): 
    with open(character_file, "r") as file:
        char_data = json.load(file)
    
    # PREPARE FOR NEW NAMES DEPENDING ON USAGE
    character = character_file.name[:-4] # character file name
    power_dest = f"powers/{character}_attributes.json" 
    
    # INCLUDE ATTRIBUTES INTO POWERS TO ENABLE THEM(
    char_data["powers"].append(f"{character}_attributes")

    # Load new power file
    with open(power_dest, "w") as file:
        power = {
            "type": "origins:multiple",
            "name": char_data["name"] + "attributes",
            "description": char_data["meta"]["goal"]
            }
        # Implement attributes in the multiple
        power |= attributes(char_data["attributes"])

        json.dump(power, file, indent=2)
    
    # TODO: IMPLEMENT DATA INTO THE ORIGIN
    with open(f"origins/{character}.json", "w") as file:
        origin = {
            "powers": [power["name"]] + char_data["powers"],
            "icon": f'{MOD_NAMESPACE}:{char_data["name"].lower()}',
            "order": int(character[:3].replace('0', '')), # TODO: Error handler at the start of the loop. Use logging and continue in skipped files.
            "impact": 0,
            "name": f'{char_data["name"]} {char_data["last"]}',
            "description": char_data["description"]
        }
        # TODO: "upgrades": [logic], and unchoosable

        json.dump(origin, file, indent=2)
    
