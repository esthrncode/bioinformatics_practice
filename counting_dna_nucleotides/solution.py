# brute_force approach

def counting_dna(s: str) -> list[int]:
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for digit in s:
        if digit == "A":
            count_a += 1
        if digit == "C":
            count_c += 1
        if digit == "G":
            count_g += 1
        if digit == "T":
            count_t += 1
    return [count_a, count_c, count_g, count_t]
s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print(counting_dna(s))