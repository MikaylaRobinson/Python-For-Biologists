"""
Find the length of the fragments after a sequence of DNA is digested with two restriction enzymes
"""
import re
dna_info = open("dna.txt")
dna = dna_info.read()

# Make a list to store cut locations and the start/end of the sequence
cut_locations = [0]

# Find cut sites for AbcI
first_recognition_site = re.finditer(r"A[ACGT]TAAT", dna)
for match in first_recognition_site:
    site_start = match.start()
    cut_site = (site_start + 3)
    cut_locations.append(cut_site)
cut_locations.append(len(dna))  

# Find cut sites for AbcII
second_recognition_site = re.finditer(r"GC[AG][AT]TG", dna)
for match in second_recognition_site:
    start_point = match.start()
    cut_point = (start_point + 3)
    cut_locations.append(cut_point)
cut_locations.sort()

# Find sequence length between cut sites
for index in range(1, len(cut_locations)):
    current_cut = cut_locations[index]
    previous_cut = cut_locations[index-1]
    fragment_length = current_cut - previous_cut
    print(fragment_length)