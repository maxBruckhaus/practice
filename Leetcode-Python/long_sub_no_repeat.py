def long_sub_no_repeat(s):
    if len(s) == 1:
        return 1

    longest_substring = 0
    for i in range(len(s)-1):
        char_dict = {s[i]: 1}
        substring_len = 1
        for j in range(i+1, len(s)):
            if s[j] in char_dict:
                break
            else:
                substring_len += 1
                char_dict[s[j]] = 1
        if substring_len > longest_substring:
            longest_substring = substring_len

    return longest_substring


if __name__ == '__main__':
    print("Longest substring without repeating characters!")

    # setup input
    s = "abcabcbb"
    result = long_sub_no_repeat(s)
    print(s, result)

    s2 = "pwwkew"
    result = long_sub_no_repeat(s2)
    print(s2, result)

    s3 = "bbbbb"
    result = long_sub_no_repeat(s3)
    print(s3, result)

    s4 = " "
    result = long_sub_no_repeat(s4)
    print(s4, result)

    s5 = "ma"
    result = long_sub_no_repeat(s5)
    print(s5, result)
