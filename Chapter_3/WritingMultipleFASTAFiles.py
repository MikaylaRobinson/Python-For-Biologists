"""
Write a FASTA file to contain the given DNA sequences and headers in the proper format
"""
# Define headers
HEADER_1 = "ABC123"
HEADER_2 = "DEF456"
HEADER_3 = "HIJ789"

# Open a FASTA file to write to
DNA_FILE_1 = open(HEADER_1 + ".fasta", "w")
DNA_FILE_2 = open(HEADER_2 + ".fasta", "w")
DNA_FILE_3 = open(HEADER_3 + ".fasta", "w")


# Define DNA sequences
SEQUENCE_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
SEQUENCE_2 = "actgatcgacgatcgatcgatcacgact"
SEQUENCE_3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

# Write first sequence
DNA_FILE_1.write(">" + HEADER_1 + "\n" + SEQUENCE_1 + "\n")

# Write the second sequence
DNA_FILE_2.write(">" + HEADER_2 + "\n" + SEQUENCE_2.upper() + "\n")

#Write the third sequence
DNA_FILE_3.write(">" + HEADER_3 + "\n" + SEQUENCE_3.replace("-", "") + "\n")