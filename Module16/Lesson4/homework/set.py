a = set('hello')
print(a)

b = {'a', 'b', 'c', 'd'}
print(b)

c = {i ** 2 for i in range(10)} # генератор множеств
print(c)

d = {}  # А так нельзя!
for i in d:
    print(i)
print(d)

words = ['hello', 'daddy', 'hello', 'mum']
print(set(words))
words_list = set(words)
print(words_list)

a = set('qwerty')
b = frozenset('qwerty')
print(a)
print(b)
if a == b:
    print('True')

# type(a - b)
# type(a | b)
a.add(1)
print(a)
# b.add(1)
# print(b)