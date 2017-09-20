
add2 = lambda a2, b2 : a2 + b2

a = add2(100,200)
print(a)


def add1 (a,b) : return a + b
print(add1(10,20))


add11 = add1


# filter
ls = [100,200,300]
new_ls = filter(lambda x: x > 100, ls)
print(type(new_ls))
print(list(new_ls))


