import hash_map_approach

def test_basic():
    assert hash_map_approach([2, 7, 11, 15], 9) == [0, 1]

def test_duplicates():
    assert hash_map_approach([3, 3], 6) == [0, 1]

def test_zero_and_negatives():
    assert hash_map_approach([0, -3, 3, 1], 0) in ([1, 2], [2, 1])

def test_no_solution():
    assert hash_map_approach([1, 2, 3], 100) == []
