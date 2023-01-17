from collections import Counter, OrderedDict, defaultdict

list = [1,2,3,4,5,6,7,8,9]

sentence = "haruto is always thinking about python"

print("how many the same number is in the list: ")
print(Counter(list))
print()

print("how many each letter is in the sentence: ")
print(Counter(sentence))
print()

dict = defaultdict(lambda: 'doesn\'t exist', {'a': 1, 'b': 2})
print(dict['c'])
print()

dict2 = OrderedDict()
dict2['b'] = 2
dict2['a'] = 1

print(dict2 == dict)
