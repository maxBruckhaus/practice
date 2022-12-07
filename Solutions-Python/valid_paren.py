def valid_paren(s):
    print(s)
    bracket_list = []

    for item in s:
        if item == ')':
            if len(bracket_list) == 0 or bracket_list[-1] != '(':
                return False
            del bracket_list[-1]
        elif item == ']':
            if len(bracket_list) == 0 or bracket_list[-1] != '[':
                return False
            del bracket_list[-1]
        elif item == '}':
            if len(bracket_list) == 0 or bracket_list[-1] != '{':
                return False
            del bracket_list[-1]
        else:
            bracket_list.append(item)

    if len(bracket_list) > 0:
        return False

    return True


if __name__ == '__main__':
    str1 = "()"
    print(valid_paren(str1))

    str2 = "(()"
    print(valid_paren(str2))

    str3 = ")(["
    print(valid_paren(str3))

    str4 = "([)]"
    print(valid_paren(str4))

    str5 = "{[]}"
    print(valid_paren(str5))
