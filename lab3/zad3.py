def power(number: int, n: int) -> int:
    if n == 0:
        return 1

    return number * power(number, n - 1)


print(power(3, 4))
