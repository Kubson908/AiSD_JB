def prime(n: int, m: int = 2) -> bool:
    if n <= 1:
        return False
    if n == m:
        return True
    if n % m == 0:
        return False
    return prime(n, m+1)

print(prime(7))
print(prime(10))
