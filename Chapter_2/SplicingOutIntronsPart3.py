"""
Printing the DNA sequence with coding bases in uppercase and non-coding in lowercase
"""
GENOMIC_DNA = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

# Define bases as either exons or introns
EXON_ONE = GENOMIC_DNA[0:62]
EXON_TWO = GENOMIC_DNA[90:]
INTRON = GENOMIC_DNA[62:90]

# Print exons remaining uppercase introns as lowercase
print(EXON_ONE + INTRON.lower() +EXON_TWO)