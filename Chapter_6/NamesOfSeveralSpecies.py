"""
Print the gene names for the species Drosophila melanogaster and Drosophila simulans
"""

gene_data = open("data.csv")
for genes in gene_data:
    fields = genes.split(",")
    species_name = fields[0]
    sequence = fields[1]
    gene_name = fields[2]
    expression_level = fields[3]
    if species_name == "Drosophila melanogaster" or species_name == "Drosophila simulans":
        print(gene_name)