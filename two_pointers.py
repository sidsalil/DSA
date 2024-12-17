nums = [1, 2, 3, 4, 6]
target = 6
left, right = 0, len(nums) - 1

while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == target:
        print(f'two numbers in a sorted array that sum to a target value')
        print(f"Pair found: ({nums[left]}, {nums[right]})")
        break
    elif current_sum < target:
        left += 1  # move left pointer to increase sum
    else:
        right -= 1  # move right pointer to decrease sum