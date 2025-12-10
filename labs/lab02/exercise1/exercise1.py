# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    # TODO: Implement this function
    # Calculate round trip cost and checks if within budget
    round_trip_km = one_way_km * 2
    liter = round_trip_km / km_per_liter
    total = liter * price_per_liter

    is_within_budget = False
    if total <= budget:
        is_within_budget = True
    return is_within_budget
    

# Test your code here
print("Testing Road Trip Budgeter...")
