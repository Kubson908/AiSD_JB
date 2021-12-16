def reverse(txt: str) -> str:
    if len(txt) == 0:
        return ''
    s: str = txt[len(txt) - 1]
    return s + reverse(txt[:len(txt) - 1])


print(reverse('test'))
