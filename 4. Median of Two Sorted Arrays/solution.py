import numpy
import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numscat = numpy.concatenate((nums1, nums2))
        numscat.sort()
        return statistics.median(numscat)
