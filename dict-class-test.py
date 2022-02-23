# Test the dict class
import geodexdictionary

dictionary = geodexdictionary.GeodexDictionary()

try:
    output = dictionary.map_type_dictt[999]
    print(output)
except KeyError:
    print("The key provided was not found in the dictionary.")
except AttributeError:
    print("The dictionary attribute does not exist.")
    
    def vdir(obj):
        return [x for x in dir(obj) if not x.startswith('__')]

    print("Possible dictionary attributes:")

    for d in vdir(dictionary):
        print(d)

import geodexdictionaryfunction

print(geodexdictionaryfunction.geodexDictFunction(primeMeridian_dict, 135))