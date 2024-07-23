from typing import Union, Optional

def generic(name: str, value: Union[int, float], addition: bool = False) -> dict:
    """origins:attribute generic minecraft attribute"""
    return {
        "name": "@s",
        "attribute": f"minecraft:generic.{name}",
        "operation": "multiply_total" if not addition else "addition",
        "value": round(value, 6)
    }

def command(command: str, value: Optional[Union[int, float]] = None) -> dict:
    """origins:execute_command selecting the entity that runs it"""
    return {
        "type": "origins:execute_command",
        "command": command + f" {round(value, 6)} @s" if value else " @s"
    }

