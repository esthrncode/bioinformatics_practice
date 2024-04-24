def hamming_distance(s, t: str) -> int:
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    return count 
s = 'TACTAGTGTTTGGTGTTTACAGGGACTGCCTCGGATTCCGGTGACCCATGCACAGGCCTAATTTCCCAGCCTGCATTCTATGACCCGCAGTTTCGTCATGGGACGTACGGCTACTCTTCCCAGTCGATATTGAAACTCCCATTCTCTTTAGAGCAAATTCTTTCAAGCAAACCGCGTACCTAGACCTGTCGTAACTACTGGATCGAAGACGTTCATTGAGGGACCTGAGGCAGAACCATCGTCTGACCATTGCTGCTTGATGGGACGCAGTATCCTCTAACCATGTGAGCAGAACGCATAGCATGTTCGTTCCTTGAATCCTTCAACCTTAACAATGTCCACAGGGGAGTTTATCATGTTGTCAGTTCACTTGAAACAATGATTCACTCATCGTCAGTGCTCCGGCATTCCTCTTTTTGCATTAGCTCGCGGCTAACCCATGTAGTCCCTCGCTAAACGCCGAGCTCGCAGCGCCGCTTTCGTTAACTTGCAAAATACGTATGTGCACTGCCGACTTAGTTCCTAGCCCACTAAATAACTCCAGGGGTCGGCTTGAAGAAATCGAAACGGGAAAGGAGGGACCTTCACCCTGCATTTAATATTAGATTTGAGGCCCGTGCTCACCACTGATGATCCAGCCGAACCCGCAGGGTGGTGAGCGGTCAGCAGGAACCGCCAAGTAATCTGAGGGCCGTAAGGCTGACCTTTCAACTAGTAGTGTATGTGTAATCTTTTGTAGAGTCAGCGGCCATCCTTCACCTACCTAGTTTTGATAAGACATAGTCTATAGCAGTGATGGGCCACTGCTCTGGGGGCACTTTAACACACGCTGGCACATCAAATCCGCACTGGGCTCACGTTATGCGCAAGATAAACGGCCGCTCTAGGTACAGGCTGGCGGAAGTGCGTGCTGAAGACGATCATCCCCAGCTTGACGATAGGCCGCCGATCACAAAGCCACACCAATCTGGCAGATCTACTCTGAAGCCGATACGCGC'
t = 'ATACGGAATGAGGGGATTGCCTTATCATCACTGAGGAACGAACACCGACGTGCAGGCATAACCACCAAGTATGCGCCTTCTGAGCCGCAGCTGAGGAAGTACACTCAGAGAGACGTTTGCGAGTGTAATGTTTAAGTTCCTGGTTCTTCATATGAGGGTCTGGTGTCCGTGACATGGACCTAGACGGATCGAAAGTGGACGTTCAAATACTACCCTAGAGAGTCCCTGGGGACTAATACCGTTTTGCTAATTCTGCGTGAACGGAGCCATGCGTCTCTCAAAATGCAAACAGCGCGGTCGGCCACTGACACCCTTGCCTCAATTTACATGGATATAGTATAAATATGAGTTTATGATGATGGCGTTTTATTCATCACGTTGAGTCACGCCACGATAGGCCACAAAAGTACATCTGTGTTCATTGATCATGTAGTTTGCCAGCGACTCAGAGGGTACACGACCACCGCGCAGAGACGCGTTGGGCGCGCTGGAAAGTAGGAGTGCACACTCACTATTTAGGACCTAGCCCTCGCGAGCAGTCCAGAAATTCGTTCGATTAGATCGCGGTGATAGATAAGGCAGGATCACCAAGCAATGGTCATCATGTTTGGGGGCCGTATTCACGACTTACAGTAGACTTGCATGCACATGAACCTGAGCAGGCATTACGATGTGTACAGTGCACGGTGGCCCTGGCAGTAAGTCAAAACGCGAGCAAATAATGTCACACGTTTTGGTCCGTCACAGGGAGTCATGTACCTATATAGATTGAATACGCCCTATTAGTTACGGGCCTGGGGGAGCTGTTCGAGGCACACGATTCTCTACGGCGGCGGACCTCGACCGTGGGGGGCTCCCGTTCAATGGAGAGGAAACGTTCACGCAAGGTTTCAGGAGGAGCATCAGCTTTTTTTGGATAACCACCTCCACCTGATTGAGGTGCGGTTGCCCGCGTTCCCCCACCAAGAATGTGGATTTAGTCGGGACGCGACGCCTAT'

print(hamming_distance(s, t))