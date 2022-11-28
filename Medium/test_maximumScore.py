from unittest import TestCase
from maximumScore import maximumScore

class Test(TestCase):

    def test_maxmimum_score(self):
        nums1, multiplier1 = [1, 2, 3], [3, 2, 1]
        nums2, multiplier2 = [-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]
        assert maximumScore(nums1, multiplier1) == 14
        assert maximumScore(nums2, multiplier2) == 102

