import string

# read list of names from file
with open('names.txt', 'r') as f:
    name_list_raw = f.read()
    name_list = name_list_raw.replace('"', '').split(',')

print('There are {} names in the list'.format(len(name_list)))


ordered_names = sorted(name_list, key=str.lower)

print("Ordered names:")
print(ordered_names)
