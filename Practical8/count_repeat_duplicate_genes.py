input_sequence = input("input one of the two repetitive sequences(GTGTGT or GTCTGT):")
fname = input_sequence + '_duplicate_genes.fa'
xfile = open(fname, 'w')
yfile = open('duplicate_genes.fa', 'r')
import re
name = ""
sequence = ""
for line in yfile:
    if line.startswith('>'):  
        if name and sequence:  
            count = len(re.findall(r'(?=(' + input_sequence + '))', sequence)) #use '?=' to match overlapping occurrences of a repeated pattern.
            if count>0:
                new_gene_name = f"{name} {count}"
                xfile.write(f">{new_gene_name[1:]}\n")
                xfile.write(f"{sequence}\n")
        name = line.strip() 
        sequence = "" 
    else:
        sequence += line.strip()
if name:
    count=len(re.findall(input_sequence, sequence))
    if count>0:
        new_gene_name = f"{name} {count}"
        xfile.write(f">{new_gene_name[1:]}\n")
        xfile.write(f"{sequence}\n")
if xfile:
    xfile.close()
if yfile:
    yfile.close()


        




