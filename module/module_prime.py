
def is_prime(a):
    b = 0
    for i in range(2, int(a ** 0.5) + 1):
        if (a % i == 0):
            b = b + 1
    if (b <= 0):
        return True
    else:
        return False

