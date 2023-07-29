"""                        Solution                            """


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        size = len(nums)
        for i in range(size - 1):
            j = i + 1
            while j < size:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1


"""                        Testing Solution                    """
if __name__ == '__main__':
    test = Solution()
    print(test.twoSum([2, 7, 11, 15], 9))
