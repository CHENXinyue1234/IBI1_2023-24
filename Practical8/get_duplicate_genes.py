with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f:
    for i in range(10): 
        line = f.readline()
        if line: 
            print(line.strip())


word = "duplication"
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as input_file, open("duplicate_genes.fa", "w") as output_file:
    has_duplication = False
    gene_description = ""
    for line in input_file:
        if line.startswith('>'):
            if word in line:
                has_duplication = True
                gene_description = line  
                gene_name = gene_description.split()[0][1:] 
                output_file.write(f">{gene_name}\n")
            else:
                has_duplication = False
                gene_description = ""
        elif has_duplication:
            output_file.write(line) 
print("New file 'duplicate_genes.fa' is created")