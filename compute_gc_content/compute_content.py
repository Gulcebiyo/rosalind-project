# Constants
PERCENTAGE = 100
ROUND_FLOAT = 6
READ = "r"
LINE_SPLIT = ">"
FILE_PATH = "rosalind_gc.txt"
GUANINE = "G"
CYTOSINE = "C"
SPLIT_GREATER = 1


def read_file():  # reading file and returning a dictionary which keys are ID's, values are DNA strings
    fasta_dict = {}
    with open(FILE_PATH, READ) as file:
        for line in file.readlines():
            if LINE_SPLIT in line:
                fasta_label = line.strip()[SPLIT_GREATER:]
                fasta_dict[fasta_label] = ""
            else:
                fasta_dict[fasta_label] += line.strip()
    return fasta_dict


def count_values(fasta_dict):
    """"
    Takes fasta dictionary and returns a dictionary which has counted values and max valued ID.
    :argument
    fasta_dict : dictionary : keys are ID's and values are DNA strings.
    :returns
    max_dict : string : has the maximum rated ID of fasta_dict.
    counted_dict : dictionary : keys are ID's and values are rates of 'G' and 'C'.
    """
    counted_dict = {key: g_c_count(value) for (key, value) in fasta_dict.items()}
    max_dict = max(counted_dict, key=counted_dict.get)
    return max_dict, counted_dict


def g_c_count(value):
    g_c_rate = round(((value.count(CYTOSINE) + value.count(GUANINE)) / len(value) * PERCENTAGE), ROUND_FLOAT)
    return g_c_rate


def main():
    max_dict, counted_dict = count_values(read_file())
    print(f"ID which has the maximum rate of 'G' and 'C' is: {max_dict}")
    print(f"The ID's rate is: {counted_dict[max_dict]}")


main()
