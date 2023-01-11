# dictionary = a changeable, unorderd collection of unique key:value pairs.
#              Fast because they use hashing, allow us to access a value quickly


# dictName = {key: value}
capitals = {'USA':'Washington DC',
            'India': 'New Deli',
            'Japan': 'Tokyo',
            'China':'Beijing'}


# it returns KeyError if the key is not in the dicitonary
print(capitals['China'])
# print(capitals['Russia'])


# .get() = get the value in the dictionary, returns "None" if the key is not in the dictionary
print(capitals.get('Germany'))


# .key() = returns only the keys in the dictionary
print(capitals.keys())


# .value() = returns only the values in the dictionary
print(capitals.values())


# add a new dictionary item
capitals.update({'Germany': 'Berlin'})


# change the value
capitals.update({'USA': 'Las Vegas'})


# .items() = shows the entire dictionary
print(capitals.items())
print()


# show the entire dictionary by using for loop
for key,value in capitals.items():
    print(key, value)
print()