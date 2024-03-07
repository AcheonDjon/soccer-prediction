

def sqt(x):
    return x**2


df = [1, 2, 3, 4, 5]

squared_values = list(map(lambda p: sqt(p), df))
print(squared_values)
