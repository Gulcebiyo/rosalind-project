# Constants
ADENINE = "A"
THYMINE = "T"
GUANINE = "G"
CYTOSINE = "C"
FILE_PATH = "rosalind_revc.txt"
READ = "r"  # stands for reading file
REVERSE = -1  # stands for reversing our string

# Variable
reversed_complement = ""

# Opening file
with open(FILE_PATH, READ) as file:
    dna_string = file.read()

# Searching for nucleotide, then we will complement it with pair nucleotide
for nucleotide in dna_string:
    if nucleotide == ADENINE:
        reversed_complement += THYMINE
    elif nucleotide == CYTOSINE:
        reversed_complement += GUANINE
    elif nucleotide == GUANINE:
        reversed_complement += CYTOSINE
    elif nucleotide == THYMINE:
        reversed_complement += ADENINE

# Reversing it and then printing it out
reversed_complement = reversed_complement[::REVERSE]
print(f"Reversed version is: {reversed_complement}")
