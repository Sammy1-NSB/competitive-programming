def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


nums = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(nums))
