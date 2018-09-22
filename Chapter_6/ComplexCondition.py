"""
Find all the genes that start with k and h, but are not the Drosophila melanogaster species.
"""

gene_data = open("data.csv")
for gene in gene_data:
    fields = gene.split(",")
    species_name = fields[0]
    sequence = fields[1]
    gene_name = fields[2]
    expression_level = fields[3]
    if gene_name.startswith("k") or gene_name.startswith("h") and not species_name == "Drosophila melanogaster":
        print(gene_name)