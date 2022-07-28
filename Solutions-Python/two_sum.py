# time: O(n^2)
# space: O(1)
def two_sum_brute(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# time: O(n)
# space: O(n)
def two_sum_hash(nums, target):
    nums_dict = {}
    for i in range(len(nums)):
        nums_dict[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums_dict and nums_dict[complement] != i:
            return [i, nums_dict[complement]]


def my_print(nums, target, result):
    print("nums:", nums)
    print("target:", target)
    print("result:", result, "\n")


if __name__ == '__main__':
    print("Brute force approach...")
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result = two_sum_brute(nums1, target1)
    my_print(nums1, target1, result)

    nums2 = [3, 2, 4]
    target2 = 6
    result = two_sum_brute(nums2, target2)
    my_print(nums2, target2, result)

    nums3 = [3, 3]
    target3 = 6
    result = two_sum_brute(nums3, target3)
    my_print(nums3, target3, result)

    print("Hash map approach...")
    result = two_sum_hash(nums1, target1)
    my_print(nums1, target1, result)

    result = two_sum_hash(nums2, target2)
    my_print(nums2, target2, result)

    result = two_sum_hash(nums3, target3)
    my_print(nums3, target3, result)
