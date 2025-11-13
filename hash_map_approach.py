from typing import List, Dict

def hash_map_two_sum(nums: List[int], target: int) -> List[int]:
	seen: dict[int, int] = {}
	for i, value in enumerate(nums):
		complement = target - value
		if complement in seen:
			return [seen[complement], i]
		seen[value] = i
	return []

check_sample =hash_map_two_sum([1,3,4,5,6,7,8,8,3,4,3,2], 9)
print(check_sample)
print(hash_map_two_sum([1,3,4,5,6,7,8,9,4,3,2], 9))
print(hash_map_two_sum([1,2,3], 4))
print(hash_map_two_sum([3,3,4], 6))
print(hash_map_two_sum([0,3,4], 6))