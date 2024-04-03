import re
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
match_form1 = re.findall(r'GTGTGT', seq)
match_form2 = re.findall(r'GTCTGT', seq)
total_number = len(match_form1) + len(match_form2)
print("The total number of repeat elements:", total_number)
