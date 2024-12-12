def fusionner_dicts(dict1, dict2):
    for cle, valeur in dict2.items():
        if cle in dict1:
            dict1[cle] += valeur

        else:
            dict1[cle] = valeur
             
        return dict1
    
dc1 = {'a': 1, 'b': 2, 'c': 3}
dc2 = {'b': 3, 'c': 4, 'd': 5}
print(fusionner_dicts(dc1,dc2))
    
