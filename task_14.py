def is_prime(a: int) -> bool:
    b = 0
    for i in range(2, int(a ** 0.5) + 1):
        if (a % i == 0):
            b = b + 1
    if (b <= 0):
        return True
    else:
        return False


tests: list[tuple[int, bool]] = [(757, True), (571, True), (659, True), (957, False), (841, False), (841.0, False)]
j = 1
for test in tests:
    print(f'test №{j}')
    print(f'input: {test[0]}')
    print(f'verdict: ', end='')
    if is_prime(test[0]) == test[1]:
        print('correct\n')
    else:
        print('incorrectly\n')
    j += 1
    
    
# Ошибки которые выдаёт python    
'''
test.py:12: error: "list" is not subscriptable, use "typing.List" instead  [misc]
test.py:12: error: "tuple" is not subscriptable, use "typing.Tuple" instead  [misc]
test.py:12: error: List item 5 has incompatible type "Tuple[float, bool]"; expected "Tuple[int, bool]"  [list-item]
Found 3 errors in 1 file (checked 1 source file)
'''