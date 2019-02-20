my_list = list(range(16))
print([x for x in my_list if x % 3 == 0])

#is the same as:
def by_three(x):
    return x % 3 == 0
