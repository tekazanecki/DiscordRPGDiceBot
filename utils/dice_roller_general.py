import random
import re

def roll_dice(dice_notation):
    """
    Rolls dice based on the provided notation and returns the results and total sum.

    Args:
        dice_notation (str): Dice notation, e.g., '2k10 + 3', 'k6', '+5', '-2'.

    Returns:
        str: A formatted string showing the roll results and the total sum.
    """
    # Regular expression to match dice notation (e.g., '2k10', 'k6', '+3', '-2')
    pattern = re.compile(r'(\d*)k(\d+)|([+-]?\d+)')
    # Split the notation by '+' to handle multiple parts
    parts = dice_notation.split('+')
    results = []
    current_sum = 0

    for part in parts:
        part = part.strip()
        match = pattern.fullmatch(part)

        if not match:
            return f"Invalid format: {part}. Use e.g., 'k10', '2k10', '4k20', '+3', '-2'."

        if match.group(3):  # Modifier
            modifier = int(match.group(3))
            current_sum += modifier
            results.append(f"{modifier}")
        else:
            num_rolls = int(match.group(1)) if match.group(1) else 1
            dice_size = int(match.group(2))
            # Roll the dice
            rolls = [random.randint(1, dice_size) for _ in range(num_rolls)]
            roll_total = sum(rolls)
            current_sum += roll_total
            roll_str = f"{roll_total} (k{dice_size})" if num_rolls == 1 else f"{roll_total} ({num_rolls}k{dice_size})"
            results.append(roll_str)

    # Join the results and format the total string
    rolls_str = ' + '.join(results)
    total_str = f"{rolls_str} = {current_sum}"

    return total_str
