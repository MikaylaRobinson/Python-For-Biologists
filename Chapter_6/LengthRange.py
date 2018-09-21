"""
Print the genes that have a sequence between 90 and 110 bases
"""

gene_data = open("data.csv")
for genes in gene_data:
    fields = genes.split(",")
    species_name = fields[0]
    sequence = fields[1]
    gene_name = fields[2]
    expression_level = fields[3]
    gene_length = len(sequence)
    if gene_length > 90 and gene_length < 110:
        print(gene_name)       