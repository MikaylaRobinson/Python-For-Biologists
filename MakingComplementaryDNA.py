DNA = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# Change A's to filler
NewDNA1 = DNA.replace('A' , 'Z')
# Change T's to A's 
NewDNA2 = NewDNA1.replace('T' , 'A')
#Change the filler Z to T's
NewDNA3 = NewDNA2.replace('Z' , 'T')
# Change C's to filler X
NewDNA4 = NewDNA3.replace('C' , 'X')
# Change G's to C's
NewDNA5 = NewDNA4.replace('G' , 'C')
# Change filler X to G's
NewDNA6 = NewDNA5.replace('X' , 'G')
print(NewDNA6)
