def func(*args):
    return ', '.join(str(arg) for arg in args)
result = func('gleb', 'sasha', 'ya')
print(result)
