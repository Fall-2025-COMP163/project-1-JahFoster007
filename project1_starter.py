"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jahiem Foster
Date: 26 October 2025

AI Usage: AI helped with fixing multiple indentation errors and designing level_up function
"""

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold

    Example:
        char = create_character("Aria", "Mage")
        # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    #Character Classes
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    #Returns None if input isn't one of the 4 classes
    if character_class not in valid_classes:
        print("Invalid class selected.")
        return None
    #Starting Level and Gold
    level = 1
    gold = 100
    #Starter stats based on class using calculate_stats function
    strength, magic, health = calculate_stats(character_class, level)
    #Returns a dictionary with all character info
    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }


def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns: tuple of (strength, magic, health)

    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
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
        return (0, 0, 0)

    return (strength, magic, health)


def save_character(character, filename):
    """
    Saves character to text file in specific format.
    Returns: True if successful, False if error occurred.

    Required file format:
    Character Name: [name]
    Character Class: [class]
    Character Level: [level]
    Character Strength: [strength]
    Character Magic: [magic]
    Character Health: [health]
    Character Gold: [gold]
    """
    #import os matches directory formatting to the operating system Ex. Mac or Windows
    import os
    #If character isn't in dictionary format the function returns false
    if not isinstance(character, dict) or not filename:
        return False
    #checks if the directory sharing the filename exists
    #returns false if it doesn't exist
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False
    #Writes character information to a file
    with open(filename, 'w') as f:
        f.write(f'Character Name: {character["name"]}\n')
        f.write(f'Character Class: {character["class"]}\n')
        f.write(f'Character Level: {character["level"]}\n')
        f.write(f'Character Strength: {character["strength"]}\n')
        f.write(f'Character Magic: {character["magic"]}\n')
        f.write(f'Character Health: {character["health"]}\n')
        f.write(f'Character Gold: {character["gold"]}\n')

    return True


def load_character(filename):
    """
    Loads character from text file.
    Returns: character dictionary if successful, None if file not found.
    """
    import os
    #checks for file, returns a string and None if file isn't found
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        return None
    #Loads character info into an empty dictionary
    load = {}
    with open(filename, 'r') as f:
        for line in f:
            if ':' not in line:
                continue
            #formatting by stripping whitespace, splitting at every colon and making each letter lowercase
            key, value = line.strip().split(':', 1)
            #excludes 'character' from categories EX. 'character name' becomes 'name' etc.
            key = key.lower().replace('character', '').strip()
            value = value.strip()
            if value.isdigit():
                value = int(value)
            load[key] = value
        #returns dictionary
    return load


def display_character(character):
    """
    Prints formatted character sheet.
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
    if not isinstance(character, dict):
        print("Invalid character data.")
        return

    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


def level_up(character):
    """
    Increases character level and recalculates stats.
    Modifies the character dictionary directly.
    Returns: None
    """
    if not isinstance(character, dict):
        print("Invalid character data.")
        return

    character['level'] += 1
    strength, magic, health = calculate_stats(character['class'], character['level'])
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health

    print(f"\n{character['name']} leveled up to level {character['level']}!")


if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")

    name = input("What is your name?\n")
    character_class = input("Choose your class: Warrior/Mage/Rogue/Cleric\n")

    character = create_character(name, character_class)

    filename = f'{name}.txt'
    save_character(character, filename)

    loaded = load_character(filename)
    if loaded:
        display_character(loaded)
        level_up(loaded)
        display_character(loaded)
        level_up(loaded)
        display_character(loaded)
        level_up(loaded)
        display_character(loaded)