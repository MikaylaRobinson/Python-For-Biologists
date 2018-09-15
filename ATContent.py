my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

# Find length of the DNA strand
length_of_dna = len(my_dna)

# Find how many A's there are
a_count = my_dna.count('A')

# Find how many T's there are
t_count = my_dna.count('T')

# Find out how many A's and T's we have together
combined_at = a_count + t_count

# Find the percent!
at_content = combined_at / length_of_dna * 100
print(at_content)