l= [1,2,3,4,5,"hello","b"]
print(len(l[5]))

l.append("This is my world")
print(l)

l.pop(2)
print(l)

# l.sort()
# print(l)
# sort() does not work because of l is heterogenous

numbers = [100,120,22,11]
numbers.sort()
print(numbers)