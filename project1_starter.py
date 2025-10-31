"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jahiem Foster
Date: 26 October 2025

AI Usage: AI helped with fixing multiple indentation errors and designing level_up function
"""

def create_character(name, character_class):
    """Creates a character and assigns stats based on class chosen"""
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        print("Invalid class selected.")
        return None

    level = 1
    gold = 100
    strength, magic, health = calculate_stats(character_class, level)

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
    """Calculates character stats based on class and level"""
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
    """Saves a character dictionary to a file; returns False for invalid paths"""
    import os

    if not isinstance(character, dict) or not filename:
        return False

    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False

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
    """Loads character from file; returns None if file not found"""
    import os

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        return None

    load = {}
    with open(filename, 'r') as f:
        for line in f:
            if ':' not in line:
                continue
            key, value = line.strip().split(':', 1)
            key = key.lower().replace('character', '').strip()
            value = value.strip()
            if value.isdigit():
                value = int(value)
            load[key] = value

    return load


def display_character(character):
    """Prints a formatted character sheet"""
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
    """Increases character level and recalculates stats"""
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
