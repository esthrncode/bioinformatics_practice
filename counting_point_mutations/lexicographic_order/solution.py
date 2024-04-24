import itertools

def lexicographic_order(s: str, n: int) -> list[str]:
    sorted_s = sorted(s)
    arr = itertools.product(sorted_s, repeat=n)
    return [''.join(char) for char in arr]

input_s = 'A B C D E F G H I J'
s = input_s.split()
n = 2
all_string = lexicographic_order(s,n)
for string in all_string:
    print(string)
    
 