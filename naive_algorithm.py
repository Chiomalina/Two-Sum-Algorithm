def naive_algorithm_two_Sum(nums, target):
	"""
	The function uses nested loop to check for possible pairs of nums that adds up to a target value
	:param nums: list of numbers
	:param target: an integer
	:return: the index if the pair that adds up to the target int value
	"""
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]
	return[]
