#example
#get all names that start with "A"

names = {'Alicia', 'Alexander Hamilton', 'Lin Manuel Miranda', 'Autin','Alex','Napoleon'}


def starts_with_a(name: str) -> bool:
    if name[0] == 'A':
        return True
    else:
        return False

a_names = filter(starts_with_a, names)
print(list(a_names))


#a short way using the lambda function

a_names = filter(lambda name: name[0] == 'A', names)
print(list(a_names))