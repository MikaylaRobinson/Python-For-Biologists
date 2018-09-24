dna_to_proteins = {
"TTT" : "F", "TCT" : "S", "TAT" : "Y", "TGT" : "C", "TTC" : "F",
"TCC" : "S", "TAC" : "Y", "TGC" : "C", "TTA" : "L", "TCA" : "S",
"TAA" : "*", "TGA" : "*", "TTG" : "L", "TCG" : "S", "TAG" : "*",
"TGG" : "W", "CTT" : "L", "CCT" : "P", "CAT" : "H", "CGT" : "R",  
"CTC" : "L", "CCC" : "P", "CAC" : "H", "CGC" : "R", "CTA" : "L", 
"CCA" : "P", "CAA" : "Q", "CGA" : "R", "CTG" : "L", "CCG" : "P",
"CAG" : "Q", "CGG" : "R", "ATT" : "I", "ACT" : "T", "AAT" : "N",
"AGT" : "S", "ATC" : "I", "ACC" : "T", "AAC" : "N", "AGC" : "S",   
"ATA" : "I", "ACA" : "T", "AAA" : "K", "AGA" : "R", "ATG" : "M",
"ACG" : "T", "AAG" : "K", "AGG" : "R", "GTT" : "V", "GCT" : "A",
"GAT" : "D", "GGT" : "G", "GTC" : "V", "GCC" : "A", "GAC" : "D",
"GGC" : "G", "GTA" : "V", "GCA" : "A", "GAA" : "E", "GGA" : "G", 
"GTG" : "V", "GCG" : "A", "GAG" : "E", "GGG" : "G"}

def translation(dna):
    # Make list to hold the proteins that match the codons
    protein_sequence = []

    # Separate the DNA sequence, match the codon in the library, and add the protein to the list
    for codons in range(0, len(dna), 3):
        codon = dna[codons: codons + 3]
        protein = dna_to_proteins.get(codon)
        protein_sequence.append(protein)
  
    # Join the list of proteins to make a string
    final_sequence = "".join(protein_sequence)
    return final_sequence
