"""
Splicing out introns to have just the coding regions of the DNA sequence
"""

GENOMIC_DNA ="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGA TCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

# Extract the first exon 
exon_one = GENOMIC_DNA[0:64]

# Extract the second exon
exon_two = GENOMIC_DNA[91:1000]

#Print the exons combined 
print(exon_one + exon_two)