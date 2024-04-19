# brute_force approach

def counting_dna(s: str) -> str:
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for digit in s:
        if digit == "A":
            count_a += 1
        elif digit == "C":
            count_c += 1
        elif digit == "G":
            count_g += 1
        elif digit == "T":
            count_t += 1
    return f"{count_a} {count_c} {count_g} {count_t}"
file_path = 'counting_dna_nucleotides/rosalind_dna (4).txt'
rosalind_dna
print(counting_dna(s))

#optimal approach

def 