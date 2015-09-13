test_dict = {'things':['books'], 'places':{'atlanta':'georgia', 'cleveland':'ohio'}, 'people':{'greg':{'age':'26', 'gender':'male'}, 'emma':{'age':'25', 'gender':'female'}}}

# def test_function():
#     for first_level in test_dict:
#         if first_level == 'people':
#             return test_dict[first_level]

# new_dict = test_function()
# print new_dict

# for each in new_dict:
#     new_dict[each].append([some])

# print new_dict

print test_dict

def function(dict):
    for a in dict:
        if a == 'people':
            dict[a] = 'sammy'


test = function(test_dict) 

print test_dict