# Constants
FILE_PATH = "rosalind_dna.txt"
ADENINE = "A"
THYMINE = "T"
GUANINE = "G"
CYTOSINE = "C"
INCREASE = 1
READ = "r"

# Variables
adenine_count = 0
thymine_count = 0
guanine_count = 0
cytosine_count = 0

# Opening file
with open(FILE_PATH, READ) as file:
    dna_string = file.read()

# Searching for nucleotide
for nucleotide in dna_string:
    if nucleotide == ADENINE:
        adenine_count += INCREASE
    elif nucleotide == CYTOSINE:
        cytosine_count += INCREASE
    elif nucleotide == GUANINE:
        guanine_count += INCREASE
    elif nucleotide == THYMINE:
        thymine_count += INCREASE

# Printing counts of each nucleotide
print(f"Adenine count: {adenine_count}\n"
      f"Cytosine count: {cytosine_count}\n"
      f"Guanine count: {guanine_count}\n"
      f"Thymine count: {thymine_count}")
