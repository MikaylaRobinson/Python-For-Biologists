"""
Calculate what percentage of the DNA sequence is coding
"""
# Define the DNA sequence and the exons 
GENOMIC_DNA = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGA TCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
EXON_ONE = GENOMIC_DNA[0:62]
EXON_TWO = GENOMIC_DNA[90:]

# Find the length of combined exons
combined_exons = len(EXON_ONE + EXON_TWO)

# Find the length of the entire sequence
length_of_sequence = len(GENOMIC_DNA)

# Find proportion of DNA that is coding
coding_proportion = combined_exons / length_of_sequence
print(coding_proportion * 100)



