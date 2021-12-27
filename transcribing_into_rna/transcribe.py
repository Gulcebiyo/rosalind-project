# Constants
FILE_PATH = "rosalind_rna.txt"
THYMINE = "T"
URACIL = "U"
READ = "r"

# Variable
rna_string = ""

# Opening file
with open(FILE_PATH, READ) as file:
    dna_string = file.read()

# Searching for thymine basis, if we find, we are changing with uracil
for nucleotide in dna_string:
    if nucleotide == THYMINE:
        rna_string += URACIL
    else:
        rna_string += nucleotide

# Printing it out
print(f"Transcribed version of DNA to RNA: {rna_string}")
