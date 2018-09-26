"""
Sort each DNA sequence from input files to new folders by the sequence length
"""
import os

# Make the folders for each range of DNA length
for lower_values in range(100, 1000, 100):
    upper_values = lower_values + 99
    newfolder = str(lower_values) + "-" + str(upper_values)
    os.mkdir(newfolder)

# Make the variable that will distinguish each DNA sequence
section = 1

# Read each of the DNA files
for files in os.listdir("."):
    if files.endswith(".dna"):
        print(files)
        dna_info = open(files)

        # Find the length of each DNA sequence
        for line in dna_info:
            sequence = line.rstrip("\n")
            length = len(sequence)
            print(str(length))

            # Sort and write each sequence to a new file and sort to appropriate folders
            for lower_values in range(100, 1000, 100):
                upper_values = lower_values + 99
                if length >= lower_values and length < upper_values:
                    print(str(lower_values) + "to" + str(upper_values))
                    newfolder = str(lower_values) + "-" + str(upper_values)
                    file_path = newfolder + "/" + str(section) + ".dna"
                    output = open(file_path, "w")
                    output.write(sequence)
                    output.close()
                    section = section + 1