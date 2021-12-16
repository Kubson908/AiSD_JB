def numbers(i: int) -> None:
    if i < 0:
        return

    print(i)
    numbers(i - 1)


numbers(20)
