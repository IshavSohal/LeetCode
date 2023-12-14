def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        element1 = nums[i]

        for j in range(i+1, len(nums)):
            element2 = nums[j]

            if element1 + element2 == target:
                return [i, j]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(twoSum(nums, target))
