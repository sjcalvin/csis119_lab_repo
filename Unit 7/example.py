dictionary_1 = {
    'city': 'Kansas City',
    'state': 'MO'
}

dictionary_2 = dict(
    city = "Lee's Summit",
    state = 'MO'
)

# print(dictionary_1)
# print(dictionary_2)

# print(dictionary_1['city'])
# #print(dictionary_1['county'])

# print(dictionary_1.get('city'))
# print(dictionary_1.get('county'))

dictionary_1['county'] = 'Jackson'
dictionary_2['county'] = 'Jackson'

# print(dictionary_1)
# print(dictionary_2)

# Print the values in the dictionary using the keys.
# for i in dictionary_1.items():

#     print (i[1])

# if 'county' in dictionary_1:

#     print('County is a key in dictionary_1')

dictionary_1.update(
    {
        'city': 'Harrisonville',
        'county': 'Cass',
        'area_code': 816
    }
)

#print(dictionary_1)

dictionary_3 = dict.fromkeys(['city', 'state'])

print(dictionary_3)

a = {1, 2, 3, 4}

for num in a:

    print(num)



