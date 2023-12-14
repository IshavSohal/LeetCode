from typing import List


class Solution:
    def __init__(self):
        self.money = 0

        # key: index, value: max amount of money to be earned from the subtree
        # rooted at nums[index] (for memoization)
        self.subtree_earnings = {}

    def rob(self, nums: List[int]) -> int:

        self.money = 0
        self.subtree_earnings = {}

        def rob_helper(start: int) -> int:

            # if the max amount of money to be earned from the subtree rooted
            # at nums[start] has not ever been calculated, we must calculate it
            if start not in self.subtree_earnings:

                # Base case: if nums[start] is a leaf node
                if start >= len(nums) - 2:
                    self.subtree_earnings[start] = nums[start]

                # Recursive case: if nums[start] has at least one child node
                else:
                    self.subtree_earnings[start + 2] = rob_helper(start + 2)
                    max_earnings = self.subtree_earnings[start + 2]

                    if start + 3 < len(nums):
                        self.subtree_earnings[start + 3] = rob_helper(start + 3)

                        if self.subtree_earnings[start + 3] > self.subtree_earnings[start + 2]:
                            max_earnings = self.subtree_earnings[start + 3]

                    self.subtree_earnings[start] = nums[start] + max_earnings


            #print("values", self.subtree_earnings)
            return self.subtree_earnings[start]

        earnings = rob_helper(0)

        if len(nums) > 1:
            tmp = rob_helper(1)

            if tmp > earnings:
                earnings = tmp

        return earnings


class Solution2:
    def __init__(self):
        self.money = 0

    def rob(self, nums: List[int]) -> int:

        self.money = 0

        def rob_helper(start: int, amount: int) -> None:

            # Base case
            if start >= len(nums) - 2:
                if amount > self.money:
                    self.money = amount

            # Recursive case
            else:

                rob_helper(start+2, amount + nums[start+2])

                if start+3 < len(nums):
                    rob_helper(start+3, amount + nums[start+3])

        rob_helper(0, nums[0])

        if len(nums) > 1:
            rob_helper(1, nums[1])

        return self.money



if __name__ == "__main__":
    x = Solution()
    y = x.rob([2, 7, 3, 9, 11, 8, 9, 18])
    print(y)
