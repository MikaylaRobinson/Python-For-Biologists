my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#Find length of fragment one
fragment_one = my_dna.find('GAATTC') + 1

#Find length of fragment two
fragment_two = len(my_dna) - fragment_one

print('Length of the first fragment: ' + str(fragment_one))
print('Length of the second fragment: ' + str(fragment_two))