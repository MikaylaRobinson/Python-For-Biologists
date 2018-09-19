"""
Write a function that finds the percentage of the protein that an amino acid makes up
"""
# Define the function
def find_aa_percent(protein, amino_acid):
    protein = protein.upper()
    aa_count = protein.count(amino_acid.upper())
    length_of_protein = len(protein)
    percentage = aa_count / length_of_protein * 100
    return percentage

# Test the function
assert find_aa_percent("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert find_aa_percent("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert find_aa_percent("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert find_aa_percent("MSRSLLLRFLLFLLLLPPLP", "Y") == 0