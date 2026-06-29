class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        new = []
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                new.append(nums1[i])
                i +=1
            else:
                new.append(nums2[j])
                j +=1
        while i < n:
            new.append(nums1[i])
            i +=1
        while j < m:
            new.append(nums2[j])
            j +=1
        if len(new)%2 != 0:
            mth = (len(new)-1)//2
            median = new[mth]
            return median
        else:
            mth = (len(new)-1)//2
            nth = (len(new))//2
            median = (new[mth] + new[nth])/2
            return median