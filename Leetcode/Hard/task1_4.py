import unittest
from time import perf_counter

t1 = perf_counter()


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    sort_new_arr = sorted(nums1 + nums2)
    if len(sort_new_arr) % 2 == 0:
        i = int(len(sort_new_arr) / 2)
        return (sort_new_arr[i - 1] + sort_new_arr[i]) / 2
    else:
        i = int(len(sort_new_arr) / 2)
        return float(sort_new_arr[i])


print(findMedianSortedArrays(nums1=[1, 3], nums2=[2]))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_findMedianSortedArrays(self):
        expected = 2.00000
        actual = findMedianSortedArrays(nums1=[1, 3], nums2=[2])
        self.assertEqual(expected, actual)

    def test02_findMedianSortedArrays(self):
        expected = 2.50000
        actual = findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4])
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
