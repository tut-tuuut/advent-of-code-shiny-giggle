def assert_equals(tested, expected, comment = ''):
    if tested == expected:
        print(f'\033[92m(YAY)\033[0m {tested} {comment}')
    else:
        print(f'\033[91m(NAY)\033[0m got {tested} ! expected {expected} ! {comment}')