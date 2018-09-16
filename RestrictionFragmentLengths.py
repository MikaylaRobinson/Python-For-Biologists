"""
Find the length of the two fragments created after a DNA sequence is digested with EcoRI.
"""

MY_DNA = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
RECOGNITION_SITE = "GAATTC"

# Find length of fragment one
fragment_one_length = MY_DNA.find(RECOGNITION_SITE) + 1

# Find length of fragment two
fragment_two_length = len(MY_DNA) - fragment_one

print('Length of the first fragment: ' + str(fragment_one_length))
print('Length of the second fragment: ' + str(fragment_two_length))