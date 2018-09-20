"""
Write a function that finds the percentage of the protein that is made up of multiple amino acids
"""

# Define the function
def find_aa_percent(protein, amino_acid=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    protein = protein.upper()
    length_of_protein = len(protein)
    total = 0 
    for aa in amino_acid:
       aa = aa.upper()
       aa_count = protein.count(aa)
       total = total + aa_count
    percentage = total * 100 / length_of_protein
    return percentage

# Test function
assert find_aa_percent("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert find_aa_percent("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert find_aa_percent("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert find_aa_percent("MSRSLLLRFLLFLLLLPPLP") == 65