def berkeley_algorithm(clocks):

    avg_time = sum(clocks) / len(clocks)

    adjusted_clocks = []

    for clock in clocks:
        adjusted_clocks.append(avg_time)

    return adjusted_clocks


clocks = [10, 12, 14, 16]

adjusted = berkeley_algorithm(clocks)

print("Adjusted clocks:", adjusted)