# -------------HackerRank 30 days challenge--------------
# -----------------Day 27: Testing-----------------------

def minimum_index(seq):
    if len(seq) == 0:
       raise ValueError("cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
           min_idx = i
    return min_idx

class TestDataEmptyArray(object):
     @staticmethod
     def get_array():
         return[] # just return an empty list

class TestDataUniqueValues(object):
     @staticmethod
     def get_array():
         # Any list with at least 2 unique values
         return [10, 5, 20]
     @staticmethod
     def get_expected_result():
         # The index of the minimum value(5 is at index 1)
         return 1

class TestDataExactlyTwoDifferentMinimums:
     @staticmethod
     def get_array():
         # The minimum value(1) must appear exactly twice
         return [1, 5, 1, 10]
     @staticmethod
     def get_expected_result():
         # The index of the first occurence of the minimum value
         return 0

def TestWithEmptyArray():
    try:
       seq = TestDataEmptyArray.get_array()
       result = minimum_index(seq)
    except ValueError as e:
         pass
    else:
         assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2
    assert len(list(set(seq))) == len(seq)
    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

def TestiWithExactlyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactlyTwoDifferentMinimums()
print("OK")

