def reverse_palindromes(s:str) -> tuple[list[int]]:
    def  reverse_complement(s: str):
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return ''.join(complement[base] for base in reversed(s))
    palindromes = []

    