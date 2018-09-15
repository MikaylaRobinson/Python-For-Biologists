my_DNA = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# Find length of the DNA strand
LengthOfDNA = len(my_DNA)
# Find how many A's there are
A_Count = my_DNA.count('A')
# Find how many T's there are
T_Count = my_DNA.count('T')
# Find out how many A's and T's we have together
CombinedAT = A_Count + T_Count
# Find the percent!
ATcontent = CombinedAT / LengthOfDNA * 100
print(ATcontent)

