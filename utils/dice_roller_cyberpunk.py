import random
import re
from utils.cyberpunk_critical_hits import head_critical_injuries, body_critical_injuries

def roll_cyber(dice_notation):
    """
    Rolls a single d10 and adds a modifier. Special rules apply for rolling 1 and 10.

    Args:
        dice_notation (str): Dice notation, e.g., '10', '+5', '-3'.

    Returns:
        tuple: Roll results as a list, the final result after applying special rules.
    """
    pattern = re.compile(r'([+-]?\d+)')
    match = pattern.fullmatch(dice_notation.strip())

    if not match:
        return "Invalid format. Use e.g. '10', '+5'."

    modifier = int(match.group(1))
    roll = random.randint(1, 10)
    rolls = [roll]
    final_result = roll

    if roll == 1:
        # Roll another d10 and subtract the result
        second_roll = random.randint(1, 10)
        rolls.append(second_roll)
        final_result -= second_roll
    elif roll == 10:
        # Continue rolling as long as 10 is rolled
        while roll == 10:
            roll = random.randint(1, 10)
            rolls.append(roll)
            final_result += roll

    final_result += modifier
    return rolls, final_result

def roll_cyber_dmg(dice_notation):
    """
    Processes dice notation for damage rolls in Cyberpunk and returns the results.

    Args:
        dice_notation (str): Dice notation, e.g., '10 2 head', '10 +5 head'.

    Returns:
        str: Roll results, total damage, and special effect if a critical hit is detected.
    """
    pattern = re.compile(r'(\d+)\s+([+-]?\d+)?\s+(\w+)')
    match = pattern.fullmatch(dice_notation.strip())

    if not match:
        return "Invalid format. Use e.g. '10 2 head', '10 +5 head'."

    num_dice = int(match.group(1))
    modifier = int(match.group(2)) if match.group(2) else 0
    location = match.group(3)

    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    total_damage = sum(rolls) + modifier
    critical_hits = rolls.count(6) >= 2

    if critical_hits:
        total_damage += 5
        special_roll = sum(random.randint(1, 6) for _ in range(2))
        special_effect = (body_critical_injuries if location == 'body' else head_critical_injuries)[special_roll]
        return (f"Rolls: {', '.join(map(str, rolls))}\nTotal Damage: {total_damage}\n"
                f"Critical Hit!\nInjury: {special_effect['Injury']}\nEffect: {special_effect['Effect']}\n")

    return f"Rolls: {', '.join(map(str, rolls))}\nTotal Damage: {total_damage}"
