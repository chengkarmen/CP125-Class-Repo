

def find_momentum_days(prices):
    changes = []
    momentum_days = []
    for i in range(1, len(prices)):
        price_change = prices[i] - prices[i - 1]
        changes.append(price_change)

    for i in range (1, len(changes)):
        if prices[i] > prices[i-1] and changes[i] > changes [i - 1]:
            momentum_days.append(i)
    
    return momentum_days


# Test
prices = [100, 102, 105, 107, 106, 108, 112, 114]
result = find_momentum_days(prices)
print(f"Momentum days: {result}")  # Expected: [2, 5, 6]
