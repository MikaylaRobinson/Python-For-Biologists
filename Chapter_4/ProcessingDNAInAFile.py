"""
Trim each line of DNA in a file and then write the new sequences to a new file and print them.
"""

# Open the file containing the DNA sequences
input_file = open("input.txt")

# Create file and open it to write the trimmed DNA sequences
output_file = open("output.txt", "w")

# Process DNA lines
for dna in input_file:
    # Trim each DNA sequence
    trimmed_dna = dna[14:]
    
    # Print each sequence length 
    print(str(len(trimmed_dna)))

    # Write the trimmed sequences to the output file
    output_file.write(trimmed_dna)