# TODO: Get modded damage names/tags (i.e. Create's crushing wheels)

# https://minecraft.wiki/w/Tag#Damage_type_tags
PHYSICAL_DAMAGE_TAGS = (
    "burn_from_stepping", 
    "damages_helmet", 
    "is_drowning",
    "is_fall"
)
MAGICAL_DAMAGE_TAGS = (
    "is_explosion",
    "is_fire",
    "is_freezing",
    "is_lightning"
)
# https://origins.readthedocs.io/en/latest/misc/extras/damage_source_names/
PHYSICAL_DAMAGE_NAMES = (
    "anvil",
    "anvil.player",
    "arrow",
    "arrow.item",
    "cactus",
    "cactus.player",
    "cramming",
    "cramming.player",
    "drown",
    "drown.player",
    "fall",
    "fall.player",
    "fallingBlock",
    "fallingBlock.player",
    "fallingStalactite",
    "fallingStalactite.player",
    "flyIntoWall",
    "flyIntoWall.player",
    "hotFloor",
    "hotFloor.player",
    "inWall",
    "lava",
    "lava.player",
    "mob", # I guess this stuff is physical with on hand objects
    "mob.item",
    "player", # Same idea
    "player.item",
    "stalagmite",
    "stalagmite.player",
    "sting",
    "sting.player",
    "sting.item",
    "sweetBerryBush",
    "sweetBerryBush.player",
    "thrown.item",
    "trident",
    "trident.item",
    "wither",
    "wither.player"
    "origins:no_water_for_gills",
    "origins:no_water_for_gills.player",
)
MAGICAL_DAMAGE_NAMES = (
    "badRespawnPoint",
    "dragonBreath",
    "dragonBreath.player",
    "explosion",
    "explosion.player",
    "fireball",
    "fireball.player",
    "fireworks",
    "fireworks.player",
    "fireworks.item",
    "freeze",
    "freeze.player",
    "indirectMagic",
    "indirectMagic.item",
    "inFire",
    "inFire.player",
    "lightningBolt",
    "lightningBolt.player",
    "magic",
    "magic.player",
    "onFire",
    "onFire.player",
    "sonic_boom",
    "sonic_boom.player",
    "sonic_boom.item",
    "thorns", # In this category because it is an enchantment
    "thorns.item",
    "witherSkull",
    "origins:genericDamageOverTime",
    "origins:genericDamageOverTime.player",
    "origins:hurt_by_water",
    "origins:hurt_by_water.player"
)
PHYSICAL_DTC = {
    "type": "origins:or",
    "conditions": [{"type": "origins:in_tag", "tag": tag} for tag in PHYSICAL_DAMAGE_TAGS] + [{"type": "origins:name", "name": name} for name in PHYSICAL_DAMAGE_NAMES] 
}
MAGICAL_DTC = {
    "type": "origins:or",
    "conditions": [{"type": "origins:in_tag", "tag": tag} for tag in MAGICAL_DAMAGE_TAGS] + [{"type": "origins:name", "name": name} for name in MAGICAL_DAMAGE_NAMES]
}

def attributes(bundle: dict) -> dict:
    powers = {}
    
    # DAMAGE INCREASE
    powers["pd"] = {
        "type": "origins:modify_damage_dealt",
        "damage_condition": PHYSICAL_DTC,
        "modifier": {  # TODO: Check again, maybe too unbalanced
            "operation": "multiply_total_multiplicative",
            "value": bundle["pd"] / 100
        }
    }
    powers["md"] = {
        "type": "origins:modify_damage_dealt",
        "damage_condition": MAGICAL_DTC,
        "modifier": {  # TODO: Check again, maybe too unbalanced
            "operation": "multiply_total_multiplicative",
            "value": bundle["md"] / 100
        }
    }

    # DAMAGE REDUCTION
    powers["pr"] = {
        "type": "origins:modify_damage_taken",
        "damage_condition": PHYSICAL_DTC,
        "modifier": {
            "operation": "multiply_total_multiplicative",
            "value": bundle["pr"] / 100
        }
    }
    powers["mr"] = {
        "type": "origins:modify_damage_taken",
        "damage_condition": MAGICAL_DTC,
        "modifier": {
            "operation": "multiply_total_multiplicative",
            "value": bundle["mr"] / 100
        }
    }
    # TODO: height and health logic
        
    return powers


