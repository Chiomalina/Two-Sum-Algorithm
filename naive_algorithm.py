from typing import List

def naive_algorithm_two_sum(nums: List[int], target: int) -> List[int]:
	"""
	The function uses O(n^2) nested loop solution to check and return the
	first pairs of nums that adds up to a target value.
	:param nums: list of numbers
	:param target: an integer
	:return: the index if the pair that adds up to the target int value
	"""
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]
	return[]
