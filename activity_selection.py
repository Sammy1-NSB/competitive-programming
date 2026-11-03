def activity_selection(activities):
    # Sort activities by finish time
    activities.sort(key=lambda x: x[1])

    selected = []
    last_finish = float('-inf')

    for start, finish in activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


activities = [
    (2, 4),
    (1, 5),
    (4, 6),
    (6, 8),
    (5, 7),
    (8, 10)
]

result = activity_selection(activities)

print("Selected activities:", result)
print("Maximum number:", len(result))