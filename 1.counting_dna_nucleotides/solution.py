# brute_force approach
import pandas as pd
from collections import Counter
from timeit import default_timer as timer

def read_dna(file_path: str) -> str:
    data = pd.read_csv(file_path, header=None, dtype=str)
    rosalind_dna = ''.join(data[0])
    return rosalind_dna
def counting_dna(rosaline_rna: str) -> str:
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for digit in rosalind_dna:
        if digit == "A":
            count_a += 1
        elif digit == "C":
            count_c += 1
        elif digit == "G":
            count_g += 1
        elif digit == "T":
            count_t += 1
    return f"{count_a} {count_c} {count_g} {count_t}"

file_path = 'counting_dna_nucleotides/rosalind_dna.txt'

# read the file using pandas
rosalind_dna = read_dna(file_path)

# optimal approach

def counting_dna_optinal(file_path: str) -> str:
    counts = Counter(rosalind_dna)
    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"
if __name__ == "__main__":
    file_path = 'counting_dna_nucleotides/rosalind_dna.txt'
    rosalind_dna = read_dna(file_path)
    start = timer()
    print(counting_dna(rosalind_dna))  # Brute-force approach
    end = timer()
    print(f'time for brute-force is: {end - start}')
    start = timer()
    print(counting_dna_optinal(rosalind_dna))  # Optimal approach using Counter
    end = timer()
    print(f'time for optimal is: {end - start}')