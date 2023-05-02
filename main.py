def func(*args):
    s = {arg: arg ** 2 for arg in args}
    return s

result = func(1, 2, 3, 4, 5)
print(result)