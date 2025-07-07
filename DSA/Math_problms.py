def armstrongNumber (n):
    x = n
    reverse_num = 0
    total = 0
    while x > 0:
        last_num = x % 10
        total = total + (last_num ** 3)
        reverse_num = (reverse_num * 10) + last_num
        x = x // 10
    reversed_num = reverse_num
    # Conditions
    if n == total:
        return "Yes"
    elif "-" in str(n):
        return "Yes"
    else:
        return "No"

def evenlyDivides(N):
    divider = 0
    for digit in str(N):
        if int(digit) > 0:
            if N % int(digit) == 0:
                divider += 1
    return divider

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

for index, x in enumerate(fib()):
    if index == 10:
        break
    print("%s" % x)


def is_palindrome(n):
    x = n
    reverse_num = 0
    while x > 0:
        last_num = x % 10
        reverse_num = (reverse_num * 10) + last_num
        x = x // 10
    reversed_num = reverse_num
    # Conditions
    if n == reversed_num:
        return "Yes"
    elif "-" in str(n):
        return "Yes"
    else:
        return "No"


def lcmAndGcd(A , B):
    A_clone = A
    B_clone = B
    # Euclidean Algoritm
    while A > 0 and B > 0:
        if A > B:
            A = A % B
        else:
            B = B % A
        if A == 0:
            gcd = B
        else:
            gcd = A
    lcm = (A_clone * B_clone) // gcd
    return lcm, gcd


def isPrime(N):
    count = 0
    num = 1
    while num * num <= N:
        if N % num == 0:
            count += 1
            if (N // num) != num:
                count += 1
        num += 1
    if count == 2:
        return 1
    else:
        return 0
                

def reverse(x: int) -> int:
    reverse_num = 0
    while x > 0:
        last_num = x % 10
        reverse_num = (reverse_num * 10) + last_num
        x = x // 10
    
    if "-" in str(x):
        x = x - (x + x)
        while x > 0:
            last_num = x % 10
            reverse_num = (reverse_num * 10) + last_num
            x = x // 10
        return reverse_num - (2 * reverse_num)
    return reverse_num
    
def reversedBits(X):
    binary = '{:032b}'.format(X)
    binary = binary[ : : -1]
    decimal = int(binary, 2)
    return decimal


def sumOfDivisors(N):
    divisors_sum = 0
    for number in range(1, N + 1):
        divisors_sum += (N // number) * number
    return divisors_sum
