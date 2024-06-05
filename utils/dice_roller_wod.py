import random
import re


def roll_wod(num_dice, difficulty=8, critical_success=10):
    """
    Rolls dice according to World of Darkness rules with additional mechanics.

    Args:
        num_dice (int): Number of dice to roll.
        difficulty (int): Success threshold (default is 6).
        critical_success (int): Value at which an additional die is added (default is 10).

    Returns:
        tuple: Roll results as a list and the number of successes.
    """
    rolls = []
    successes = 0

    while num_dice > 0:
        roll = random.randint(1, 10)
        rolls.append(roll)

        if roll >= difficulty:
            successes += 1
        if roll == 1:
            successes -= 1
        if roll >= critical_success:
            num_dice += 1

        num_dice -= 1

    return rolls, successes


def roll_dice_wod(dice_notation):
    """
    Processes dice notation and returns the roll results and number of successes.

    Args:
        dice_notation (str): Dice notation, e.g., '10k6', '5', '3+2', '10k6/8e9'.

    Returns:
        str: Roll results and number of successes.
    """
    # Default values for difficulty and critical success
    difficulty = 8
    critical_success = 10

    # Patterns to match different parts of the notation
    sum_pattern = re.compile(r'(\d+)\s*\+\s*(\d+)(?:\s*/\s*(\d+))?(?:\s*e\s*(\d+))?')
    basic_pattern = re.compile(r'(\d+)(?:\s*/\s*(\d+))?(?:\s*e\s*(\d+))?')

    # Check for sum notation
    match = sum_pattern.fullmatch(dice_notation)
    if match:
        num_dice = int(match.group(1)) + int(match.group(2))
        if match.group(3):
            difficulty = int(match.group(3))
        if match.group(4):
            critical_success = int(match.group(4))
    else:
        # Check for basic notation
        match = basic_pattern.fullmatch(dice_notation)
        if match:
            num_dice = int(match.group(1))
            if match.group(2):
                difficulty = int(match.group(2))
            if match.group(3):
                critical_success = int(match.group(3))
        else:
            return f"Invalid format: {dice_notation}. Use e.g. '5/8 e10', '3+2/6 e10'."

    rolls, successes = roll_wod(num_dice, difficulty, critical_success)
    rolls_str = ', '.join(map(str, rolls))
    result = f"Rolls: {rolls_str}\nSuccesses: {successes}"
    return result
