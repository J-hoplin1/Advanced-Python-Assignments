def remove_dups(L1, L2):
    return [ i for i in L1 if i not in L2 ]

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
L1 = remove_dups(L1,L2)
print(L1)