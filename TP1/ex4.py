def compte_occurence(liste):
 return {mot:liste.count(mot) for mot in set(liste)}
print(compte_occurence(('a','b','c','b')))
