dna_string = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# Change A's to filler
dna_string = dna_string.replace('A' , 'Z')
# Change T's to A's 
dna_string = dna_string.replace('T' , 'A')
#Change the filler Z to T's
dna_string = dna_string.replace('Z' , 'T')
# Change C's to filler X
dna_string = dna_string.replace('C' , 'X')
# Change G's to C's
dna_string = dna_string.replace('G' , 'C')
# Change filler X to G's
dna_string = dna_string.replace('X' , 'G')
print(dna_string)
