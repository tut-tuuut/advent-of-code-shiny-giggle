def is_valid_password(password):
    intpwd = int(password)
    strpwd = str(password)
    if str(intpwd) != strpwd:
        return False
    if len(strpwd) != 6:
        return False
    doubleCriteria = False
    for i in range(1, len(strpwd)):
        if strpwd[i] == strpwd[i - 1]:
            doubleCriteria = True
        if int(strpwd[i - 1]) > int(strpwd[i]):
            return False
    return doubleCriteria


# print(f'This should be true: {is_valid_password(111111)}')
# print(f'This should be false: {is_valid_password(223450)}')
# print(f'This should be false: {is_valid_password(123789)}')

print("first part answer:")
print(len(list(filter(is_valid_password, range(109165, 576723)))))


def is_really_valid_password(password):
    if not is_valid_password(password):
        return False
    strpwd = str(password)
    groups = [strpwd[0]]
    for i in range(1, len(strpwd)):
        c = strpwd[i]
        if c == strpwd[i - 1]:
            groups[-1] += c
        else:
            groups.append(c)
    groups = list(filter(lambda s: len(s) > 1, groups))
    return min(list(map(len, groups))) == 2


# print(is_really_valid_password(111111))
# print(is_really_valid_password(223458))

print("second part answer:")
print(len(list(filter(is_really_valid_password, range(109165, 576723)))))
