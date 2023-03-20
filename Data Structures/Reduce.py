from functools import reduce
def multiply(a,b):
    return a*b

a_list = [1,2,3,4]
product = reduce(multiply,a_list)
print(product)
