def calculate_xp_required(current_level):
    """Return XP needed to level up (level * 100)."""
    # TODO: Implement this function
    return current_level * 100

def can_level_up(xp_remaining, xp_required):
    """Return True if xp_remaining >= xp_required."""
    # TODO: Implement this function
    if xp_remaining >= xp_required:
        return True
    else:
        return False

def calculate_final_level(total_xp):
    """
    Calculate the final level reached.
    """
    # TODO: Implement using calculate_xp_required and can_level_up
    current_level = 1
    xp_required = 100

    while can_level_up(total_xp, xp_required):
        current_level += 1
        xp_required = calculate_xp_required(current_level)

    return current_level, total_xp

# Test your code here
print("Testing Level Up Calculator...")
