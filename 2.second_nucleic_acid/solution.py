import pandas as pd
from timeit import default_timer as timer

def read_rna(file_path: str) -> str:
    data = pd.read_csv(file_path, header=None, dtype=str)
    rosalind_rna = ''.join(data[0])
    return rosalind_rna

def rna_transcribed(t: str) -> str:
    rna = t.replace('T', 'U')
    return rna

file_path = 'second_nucleic_acid/rosalind_rna.txt'

# read the file using pandas
rosalind_rna = read_rna(file_path)
start = timer()
print(rna_transcribed(rosalind_rna))
end = timer()
print(end - start)