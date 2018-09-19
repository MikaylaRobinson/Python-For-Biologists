"""
Using genomic DNA and exon stop/start postions from two different files to extract exon segments, concatenate them, and write them to a file. 
"""

# Open exon data
exon_positions = open("exons.txt")

# Open genomic DNA 
genomic_dna = open("genomic_dna.txt").read()

# Variable to hold the sequence
complete_sequence = ""

# Get exon start and stop positions from exon file
for exons in exon_positions:
    positions = exons.split(",")
    start = int(positions[0])
    stop = int(positions[1])

    # Extract exons using start and stop locations
    exon_sequences = genomic_dna[start:stop]
    complete_sequence = complete_sequence + exon_sequences

# Write the sequence to a new file
output = open("multiple_exons.txt", "w")
output.write(complete_sequence)
output.close()
