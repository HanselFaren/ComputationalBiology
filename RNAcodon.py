# Define a dictionary that maps each amino acid to its corresponding codon
codon_table = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'C': ['UGU', 'UGC'],
    'D': ['GAU', 'GAC'],
    'E': ['GAA', 'GAG'],
    'F': ['UUU', 'UUC'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'H': ['CAU', 'CAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'K': ['AAA', 'AAG'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'M': ['AUG'],
    'N': ['AAU', 'AAC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'Q': ['CAA', 'CAG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'W': ['UGG'],
    'Y': ['UAU', 'UAC']
}

# Define a function that takes an amino acid sequence and returns the corresponding mRNA sequence
def amino_to_mrna(seq):
    mrna_seq = ''
    for aa in seq:
        codons = codon_table[aa]
        mrna_seq += codons[0]
    return mrna_seq

# Define a function that takes an mRNA sequence and returns a dictionary of the codons and their counts
def count_codons(mrna_seq):
    codon_counts = {}
    for i in range(0, len(mrna_seq), 3):
        codon = mrna_seq[i:i+3]
        if codon in codon_counts:
            codon_counts[codon] += 1
        else:
            codon_counts[codon] = 1
    return codon_counts

# Prompt the user for input and convert the input to uppercase
amino_seq = input('Enter the amino acid sequence: ').upper()

# Convert the amino acid sequence to mRNA and count the codons
mrna_seq = amino_to_mrna(amino_seq)
codon_counts = count_codons(mrna_seq)

# Print the mRNA sequence and the codon counts
print('mRNA sequence:', mrna_seq)
print('Codon counts:')
for codon, count in codon_counts.items():
    print(codon, '=', count)