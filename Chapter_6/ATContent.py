gene_data = open("data.csv")
def finding_at_content(dna_sequence):
        a_count = dna_sequence.upper().count("A")
        t_count = dna_sequence.upper().count("T")
        at_content = (a_count + t_count) / len(dna_sequence)
        return at_content 

for genes in gene_data:
    fields = genes.split(",")
    species_name = fields[0]
    sequence = fields[1]
    gene_name = fields[2]
    expression_level = fields[3] 
    if finding_at_content(sequence) < 0.5 and int(expression_level) > 200:
            print(gene_name)