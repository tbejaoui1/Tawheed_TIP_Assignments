import numpy as np
import itertools
from typing import List, Iterable


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        print(nums)
        print(target)

        for i in range(len(nums)):

            for n in range(len(nums)):

                if nums[i] + nums[n] == target and i != n:
                    print('output indices and target sum are:', [i, n], target)
                    Output = [i, n]

                # else:

                # print('summed pair not equal to target and/or indices are equal', [i,n])

            n += 1
        i += 1

        return Output

    #todo figure out how to view results in console as seen in leetcode