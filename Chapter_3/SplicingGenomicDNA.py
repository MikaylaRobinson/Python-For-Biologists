"""
Splitting a DNA sequence located in a file into coding and non-coding parts. Then writing the regions of DNA to separate files. 
"""

# Open and read the file containing the DNA sequence
dna_file = open("SplicingGenomicDNA.txt")
my_dna = dna_file.read()

# Separate coding and non-coding regions
EXON_ONE = my_dna[0:62]
EXON_TWO = my_dna[90:]
INTRON = my_dna[62:90]

# Open new files to write the sequences to
coding_file = open("coding_dna.txt", "w")
noncoding_file = open("noncoding_dna.txt", "w")

# Write the DNA regions to the new .txt files
coding_file.write(EXON_ONE + EXON_TWO)
noncoding_file.write(INTRON)