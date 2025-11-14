import os
import sys
import pytest

# to ensure the import works and the project root is on sys.path, use sys.path.append
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from naive_algorithm import naive_algorithm_two_sum

@pytest.mark.parametrize(
	"nums,target,expected",
	[
		# basic pair
		([2, 7, 11, 15], 9, [0, 1]),

		# duplicates
        ([3, 3], 6, [0, 1]),

		# zero + negatives
        ([0, -3, 3, 1], 0, [1, 2]),

		# later valid pair
        ([1, 4, 2, 4], 8, [1, 3]),
	],
)

def test_found_pairs(nums, target, expected):
	assert naive_algorithm_two_sum(nums, target) == expected

def test_no_solution():
	assert naive_algorithm_two_sum([1, 2, 3], 100) == []