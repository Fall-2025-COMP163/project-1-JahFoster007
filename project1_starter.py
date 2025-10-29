"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Jahiem Foster]
Date: [26 October 2025]

AI Usage: [Document any AI assistance used]
AI helped with fixing multiple indentation errors
"""


def create_character(name, character_class):
    level = 1
    gold = 100
    if character_class == 'Warrior':
        strength, magic, health = calculate_stats(character_class, level)
    elif character_class == 'Mage':
        strength, magic, health = calculate_stats(character_class, level)
    elif character_class == 'Rogue':
        strength, magic, health = calculate_stats(character_class, level)
    elif character_class == 'Cleric':
        strength, magic, health = calculate_stats(character_class, level)
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

import os
def save_character(character, filename):
    with open(filename, 'w') as f:
        f.write(f'Character Name: {character["name"]}\n')
        f.write(f'Character Class: {character["class"]}\n')
        f.write(f'Character Level: {character["level"]}\n')
        f.write(f'Character Strength: {character["strength"]}\n')
        f.write(f'Character Magic: {character["magic"]}\n')
        f.write(f'Character Health: {character["health"]}\n')
        f.write(f'Character Gold: {character["gold"]}\n')
    return True


"""
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred

    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
# TODO: Implement this function
# Remember to handle file errors gracefully



def load_character(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass


def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)

    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass


def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    level = int(1)
    name = input("What is your name?\n")
    character_class = input("Choose your class: Warrior/Mage/Rogue/Cleric\n")
    character = create_character(name, character_class)
    print(character)
    character_stats = calculate_stats(character_class, level)
    print(character_stats)
    save = save_character(character, name)
    load = load_character(name)
    print(save)
    print(load)

    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
