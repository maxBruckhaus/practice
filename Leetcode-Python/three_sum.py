def three_sum_cubic(arr):
    target = 0
    result = []
    used_nums = []
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    nums = [arr[i], arr[j], arr[k]]
                    nums.sort()
                    if nums not in used_nums:
                        used_nums.append(nums)
                        result.append([arr[i], arr[j], arr[k]])

    return result


def three_sum_quadratic(arr):
    result = set()

    # split into positive, negative, and zeros
    pos = []
    neg = []
    zeros = []
    for num in arr:
        if num > 0:
            pos.append(num)
        elif num < 0:
            neg.append(num)
        else:
            zeros.append(num)

    # create set for negatives and positives
    pos_set = set(pos)
    neg_set = set(neg)

    # if there are at least 3 zeros, add that case
    if len(zeros) > 2:
        result.add((0, 0, 0))

    # if there is at least 1 zero, check if x and -x exists
    if len(zeros) > 0:
        for num in pos:
            if -1 * num in neg_set:
                result.add((-1*num, 0, num))

    # find a positive complement for pairs of negative nums
    for i in range(len(neg)-1):
        for j in range(i+1, len(neg)):
            complement = -1 * (neg[i] + neg[j])
            if complement in pos_set:
                result.add(tuple(sorted([neg[i], neg[j], complement])))

    # find a negative complement for pairs of positive nums
    for i in range(len(pos)-1):
        for j in range(i+1, len(pos)):
            complement = -1 * (pos[i] + pos[j])
            if complement in neg_set:
                result.add(tuple(sorted([pos[i], pos[j], complement])))

    return result


if __name__ == '__main__':
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(three_sum_cubic(nums1))
    print(three_sum_quadratic(nums1))
