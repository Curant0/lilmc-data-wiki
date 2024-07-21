from pathlib import Path
import json
EXT = ".json"

# CYCLE THROUGH THE META FILES
for meta_file in Path("meta").glob("*"): 
    with open(meta_file, "r") as file:
        meta = json.load(file)
    
    # PREPARE FOR NEW NAMES DEPENDING ON USAGE
    base_name = meta_file.name[:-4]
    power_dest = f"powers/{base_name}_attributes{EXT}" 
    
    # INCLUDE ATTRIBUTES INTO POWERS TO ENABLE THEM(
    meta["powers"].append(f"{base_name}_attributes")

    # TODO: INTEGRATE ATTRIBUTES IN A origins:multiple
    with open(power_dest, "w") as file:
        power = {
            "type": "origins:multiple",
            "name": meta["name"] + "attributes",
            "description": meta["meta"]["goal"]
            }
        power | attributes.generate(meta["attributes"])

        json.dump(power, file, indent=2)
    
    # TODO: IMPLEMENT DATA INTO THE ORIGIN
    with open(f"origins/{base_name}{EXT}", "w") as file:
        ...
    
