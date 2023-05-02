def func(*args):
    odd_num = []
    for j in args:
        if j % 2 != 0:
            odd_num.append(j)
    return odd_num
result = func(1,2,3,4,5,6)
print(result)