"""
Write a FASTA file to contain the given DNA sequences and headers in the proper format
"""

# Open a FASTA file to write to
DNA_FILE = open("my_dna.fasta", "w")

# Define headers
HEADER_1 = "ABC123"
HEADER_2 = "DEF456"
HEADER_3 = "HIJ789"

# Define DNA sequences
SEQUENCE_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
SEQUENCE_2 = "actgatcgacgatcgatcgatcacgact"
SEQUENCE_3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

# Write first sequence
DNA_FILE.write(">" + HEADER_1 + "\n" + SEQUENCE_1 + "\n")

# Write the second sequence
DNA_FILE.write(">" + HEADER_2 + "\n" + SEQUENCE_2.upper() + "\n")

#Write the third sequence
DNA_FILE.write(">" + HEADER_3 + "\n" + SEQUENCE_3.replace("-", "") + "\n")
