import random

size_ = int(input("Enter size: "))


def fibonacci(size):
    fib_ls = []
    for number in range(0, size + 1):
        fib = (((1 + 5 ** 0.5)/2) ** number - ((1 - 5 ** 0.5)/2) ** number)/5 ** 0.5
        fib_ls.append(fib)
    print(fib_ls)

fibonacci(size_)


def rand_fibonacci(number):
    fib = (((1 + 5 ** 0.5)/2) ** number - ((1 - 5 ** 0.5)/2) ** number)/5 ** 0.5
    print(fib)

r_number = random.randrange(1000)
rand_fibonacci(r_number)
