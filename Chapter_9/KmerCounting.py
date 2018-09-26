"""
Calculate kmers across DNA sequence and display those that occur more than a given amount of times
"""
import os

# Set up inputs 
accession = input("kmer_length")
accession2 = input("cutoff_number")
k_length = int(accession)
kmer_cutoff =int(accession2)

# Make a function to find the start point for each kmer
def cut_kmers(dna, k_length):
    kmers= []
    for sequences in range(0, len(dna)-(k_length-1),1):
        sequence = dna[sequences: sequences + k_length]
        kmers.append(sequence)
    return kmers

# Make a library for all of the kmer counts
kmer_counts = {}

# Open the DNA files
for files in os.listdir("."):
    if files.endswith(".dna"):
        dna_info = open(files)
        
#Cut each DNA sequence according to kmer settings
        for lines in dna_info:
            dna = lines.rstrip("\n")
            for kmer in cut_kmers(dna, k_length):
                counts = kmer_counts.get(kmer,0)
                updated_count = counts + 1
                kmer_counts[kmer] = updated_count

# Print kmers that occur more than the given cutoff
for kmer, count in kmer_counts.items():
    if count > kmer_cutoff:
        print(kmer + "/" + str(count))