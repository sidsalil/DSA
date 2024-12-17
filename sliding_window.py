nums = [2, 1, 5, 1, 3, 2]
k = 3
# max_sum = 0
max_sum = current_sum = sum(nums[:k])  # sum of first window

for i in range(len(nums) - k):
    current_sum = current_sum - nums[i] + nums[i + k]  # slide window
    max_sum = max(max_sum, current_sum)

print(f'Max Sum of numbers in K continuous index from array: {max_sum}')