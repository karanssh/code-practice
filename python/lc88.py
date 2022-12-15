from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t1 = m-1
        t2 = n-1
        f = m+n-1 
        while t1 >=0 and t2 >=0:
            if nums1[t1]> nums2[t2]:
                nums1[f] = nums1[t1]
                f -=1
                t1 -=1
            else:
                nums1[f] = nums2[t2]
                f -=1 
                t2 -=1
        while t2 >=0:
            nums1[f] = nums2[t2]
            t2 -=1
            f-=1
        print(nums1)
        

if __name__ == "__main__":
    merge([1,2,3,0,0,0],3, [1,2,3],3)
