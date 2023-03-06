from module_prime import is_prime

tests = [(757, True), (571, True), (659, True), (957, False), (841, False)]
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