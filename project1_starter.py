"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Jahiem Foster]
Date: [26 October 2025]

AI Usage: [Document any AI assistance used]
AI helped with fixing multiple indentation errors
"""

def create_character(name, character_class):
    if character_class == 'Warrior':
        level, strength, magic, health, gold = 1, 14, 5, 12, 100
    elif character_class == 'Mage':
        level, strength, magic, health, gold = 1, 4, 14, 8, 100
    elif character_class == 'Rogue':
        level, strength, magic, health, gold = 1, 8, 9, 6, 100
    elif character_class == 'Cleric':
        level, strength, magic, health, gold = 1, 8, 12, 14, 100
    else:
        return None
    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }


"""
Creates a new character dictionary with calculated stats
Returns: dictionary with keys: name, class, level, strength, magic, health, gold

Example:
char = create_character("Aria", "Mage")
# Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
"""
# TODO: Implement this function
# Remember to use calculate_stats() function for stat calculation
pass

def calculate_stats(character_class, level):
    if character_class == "Warrior":
        strength = 10 + (level * 4)
        magic = 4 + (level * 1)
        health = 9 + (level * 3)
    elif character_class == "Mage":
        strength = 3 + (level * 1)
        magic = 10 + (level * 4)
        health = 6 + (level * 2)
    elif character_class == "Rogue":
        strength = 6 + (level * 2)
        magic = 7 + (level * 2)
        health = 4 + (level * 2)
    elif character_class == "Cleric":
        strength = 6 + (level * 2)
        magic = 9 + (level * 3)
        health = 11 + (level * 3)
    else:
        # If invalid class
        return (0, 0, 0)

    return (strength, magic, health)


"""
Calculates base stats based on class and level
Returns: tuple of (strength, magic, health)

Design your own formulas! Ideas:
- Warriors: High strength, low magic, high health
- Mages: Low strength, high magic, medium health  
- Rogues: Medium strength, medium magic, low health
- Clerics: Medium strength, high magic, high health
"""
# TODO: Implement this function
# Return a tuple: (strength, magic, health)
pass

def save_character(character, filename):
    with open(filename, 'w') as f:
        f.write(f'Character Name: {character["name"]}\n')
        f.write
