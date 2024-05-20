input_sequence = input("input one of the two repetitive sequences(GTGTGT or GTCTGT):")
fname = input_sequence + '_duplicate_genes.fa'
xfile = open(fname, 'w')
yfile = open('duplicate_genes.fa', 'r')
import re
gene_name = ""
gene_sequence = ""
for line in yfile:
    if line.startswith('>'):  
        if gene_name and gene_sequence:  
            count = len(re.findall(r'(?=(' + input_sequence + '))', gene_sequence))
            if count>0:
                new_gene_name = f"{gene_name} {count}"
                xfile.write(f">{new_gene_name[1:]}\n")
                xfile.write(f"{gene_sequence}\n")
        gene_name = line.strip() 
        gene_sequence = "" 
    else:
        gene_sequence += line.strip()
if gene_name:
    count=len(re.findall(input_sequence, gene_sequence))
    if count>0:
        new_gene_name = f"{gene_name} {count}"
        xfile.write(f">{new_gene_name[1:]}\n")
        xfile.write(f"{gene_sequence}\n")
if xfile:
    xfile.close()
if yfile:
    yfile.close()


        




