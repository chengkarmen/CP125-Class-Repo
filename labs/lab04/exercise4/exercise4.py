
def analyze_performance(lap_times):
    first_half = []
    for i in range(0, (len(lap_times) / 2)):
        first_half.append(lap_times[i])

    second_half = []
    for i in range((len(lap_times) / 2), len(lap_times)):
        second_half.append(lap_times[i])

    first_average = first_half / len(first_half)
    second_average = second_half / len(second_half)
    if first_average < second_average:
        return True
    return False


# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
