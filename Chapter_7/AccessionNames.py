"""
Print the accession names that meet the specified criteria
"""
import re
accession_names = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

# Find names that contain the number 5
print("Names that contain 5:")
for name in accession_names:
    if re.search(r"5", name):
        print(name)

# Find names that contain the letter d or e
print("Names that contain the letter d or e:")
for name in accession_names:  
    if re.search(r"(d|e)", name):
        print(name)

# Find names that contain the letters d and e in that order
print("Names that contain the letters d and e in that order:")
for name in accession_names:   
    if re.search(r"d.*e", name):
        print(name)

# Find names that contain the letters d and e in that order with a single letter between them
print("Names that contain the letters d and e in that order with a single letter between them:")
for name in accession_names:   
    if re.search(r"d.e", name):
        print(name)    

# Find names that contain both the letters d and e in any order
print("Names that contain both the letters d and e in any order:") 
for name in accession_names: 
    if re.search(r"d.*e", name) or re.search(r"e.*d", name):
        print(name)

#Find names that start with x or y 
print("Names that start with x or y:")
for name in accession_names:
    if re.search(r"^(x|y)", name):
        print(name)

# Find names that start with x or y and end with e
print("Names that start with x or y and end with e:")
for name in accession_names:
    if re.search(r"^(x|y).*e$", name):
        print(name)

# Find names that contain three or more numbers in a row
print("Names that contain three or more numbers in a row:")
for name in accession_names:
    if re.search(r"[0123456789]{3,1000}", name):
        print(name)

# Find names that end with d followed by either a, r or p 
print("Names that end with d followed by either a, r, or p:")
for name in accession_names:
    if re.search(r"d[arp]$", name):
        print(name)