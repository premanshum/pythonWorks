def do_plus(a, b):
    print(a+b)

#do_plus(7, 8)
#print(type(""))

#print(str(type("")) == "<class 'str'>")

# use lambda with filter
filter_me = [1, 2, 3, 4, 6,7 ,8, 11, 12, 14, 15, 19, 22]
# This will only return true for even numbers (because x%2 is 0, or False,
# for odd numbers)
result = list(filter(lambda x: x%2 == 0, filter_me))
print(result[2])
print([p for p in filter_me if p%3 == 0])
print([p for p in filter_me if p%3 == 0][2])

