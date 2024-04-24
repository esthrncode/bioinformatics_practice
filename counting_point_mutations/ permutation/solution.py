import itertools

def all_permutations(n: int):
    arr = list(itertools.permutations(range(1, n+1)))
    total_arr = len(arr)
    return total_arr, arr

n = 5
total, permutations = all_permutations(n)
print(total)
for perm in permutations:
    print(' '.join(map(str, perm)))
