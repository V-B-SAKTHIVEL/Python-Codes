def max_subarray_sum(nums):
    if not nums:
        return None
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


print(max_subarray_sum([-7, -6, -8, -4, -1, -5, -2, -3]))
