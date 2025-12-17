# Lab 02 Exercise 8: Bouncing Ball Simulation
# Write your code below:

def calculate_bounce_height(current_height):
    """Calculate next bounce height (80% of current)."""
    # TODO: Implement this function
    current_height -= current_height * 0.2
    return current_height

def is_ball_stopped(height):
    """Return True if height < 1, False otherwise."""
    # TODO: Implement this function
    if height < 1:
        return True
    else:
        return False

def simulate_bouncing_ball(start_height):
    """
    Simulate bouncing ball.
    Returns: (bounce_count, total_distance)
    """
    # TODO: Implement using calculate_bounce_height and is_ball_stopped
    bounce_count = 0
    total_distance = start_height

    while not is_ball_stopped(start_height):
        bounce_count += 1
        start_height = calculate_bounce_height(start_height)
        total_distance +=  start_height * 2

    return bounce_count, total_distance

# Test your code here
print("Testing Bouncing Ball Simulation...")
