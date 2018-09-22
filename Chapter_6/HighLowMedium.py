"""
Print out each gene name and a message labeling the AT content as high, medium, or low
"""

def finding_at_content(dna_sequence):
    a_content = dna_sequence.upper().count("A")
    t_content = dna_sequence.upper().count("T")
    at_content = (a_content + t_content) / len(dna_sequence)
    return at_content

gene_data = open("data.csv")
for gene in gene_data:
    fields = gene.rstrip("\n").split(",")
    species_name = fields[0]
    sequence = fields[1]
    gene_name = fields[2]
    expression_level = fields[3]
    if finding_at_content(sequence) > 0.65:
        print(gene_name + " has high AT content")
    elif finding_at_content(sequence) < 0.45:
        print(gene_name + " has low AT content")
    else:
        print(gene_name + " has medium AT content")