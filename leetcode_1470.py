def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    result = []

    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])

    return result

if __name__ == "__main__":
    print(shuffle([1, 5, 7, 9, 11, 12, 15, 17], 4))
