def read_sequence(file):
    with open(file, 'r') as file:
        sequence = ''
        for line in file:
            if line[0] != '>':  
                sequence += line.strip() 
    return sequence

human_sequence = read_sequence("SLC6A4_HUMAN.fa")
mouse_sequence = read_sequence("SLC6A4_MOUSE.fa")
rat_sequence = read_sequence("SLC6A4_RAT.fa")


import blosum as bl
matrix=bl.BLOSUM(62)
def alignment_score(seq1, seq2):
    score=0
    for i in range(len(seq1)):
        score+=matrix[seq1[i]][seq2[i]]
    return score

Human_vs_Mouse_AlignmentScore = alignment_score(human_sequence, mouse_sequence)
Human_vs_Rat_AlignmentScore = alignment_score(human_sequence, rat_sequence)
Mouse_vs_Rat_AlignmentScore = alignment_score(mouse_sequence, rat_sequence)

def percentage_identity(seq1, seq2):
    identical_count = 0
    for i in range(len(seq1)):
        if seq1[i]==seq2[i]:
            identical_count+=1
    percentage = (identical_count / len(seq1)) * 100    
    return percentage

Human_vs_Mouse_identity = percentage_identity(human_sequence, mouse_sequence)
Human_vs_Rat_identity = percentage_identity(human_sequence, rat_sequence)
Mouse_vs_Rat_identity = percentage_identity(mouse_sequence, rat_sequence)

print("Human vs Mouse:")
print('Human sequence:', human_sequence)
print('Mouse sequence:', mouse_sequence)
print(f"Alignment Score: {Human_vs_Mouse_AlignmentScore}")
print(f"Percentage of identical	amino acids: {Human_vs_Mouse_identity}%")

print("Human vs Rat:")
print('Human sequence:', human_sequence)
print('Rat sequence:', rat_sequence)
print(f"Alignment Score: {Human_vs_Rat_AlignmentScore}")
print(f"Percentage of identical	amino acids: {Human_vs_Rat_identity}%")

print("Mouse vs Rat:")
print('Mouse sequence:', mouse_sequence)
print('Rat sequence:', rat_sequence)
print(f"Alignment Score: {Mouse_vs_Rat_AlignmentScore}")
print(f"Percentage of identical	amino acids: {Mouse_vs_Rat_identity}%")