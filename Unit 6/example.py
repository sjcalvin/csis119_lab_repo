list = ['Alpha', 2, 'Bravo', [1, 2, 3] ]

list.append(5)

list.extend('macbook')

list.insert(5,'Some_Object')

list.remove('Some_Object')

list.pop(6)

#list.clear()

#print(list.index('Bravo'))

list.sort(key = str)

list.reverse()

#print(list)

#list.count('o')

new_list = [list[i] ** 3 for i in range(len(list)) if str(list[i]).isdigit()]

#print(new_list)


sample_tuple = ('bananas','strawberries','cherries','blueberries')

print(sample_tuple.count('bananas'))

print(sample_tuple[2])

list.extend(sample_tuple)


