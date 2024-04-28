def parse_fasta(file_contents):
    sequences = []
    sequence = ''
    for line in file_contents.splitlines():
        if line.startswith('>'):
            if sequence:
                sequences.append(sequence)
                sequence = ''
        else:
            sequence += line.strip()
    if sequence:
        sequences.append(sequence)
    return sequences

def longest_common_substring(sequences):
    shortest_seq = min(sequences, key=len)
    length = len(shortest_seq)
    
    for substr_length in range(length, 0, -1):  # Start with the longest possible substring
        for start in range(length - substr_length + 1):
            substr = shortest_seq[start:start + substr_length]
            if all(substr in other for other in sequences):
                return substr  # Return the first longest substring found
    return ''  # Return an empty string if no common substring found

# Read the content from the file
with open("/path/to/your/fasta/file/rosalind_lcsm.txt", "r") as file:
    file_content = file.read()

# Parse the sequences
sequences = parse_fasta(file_content)

# Find the longest common substring
result = longest_common_substring(sequences)
print("Longest Common Substring:", result)
