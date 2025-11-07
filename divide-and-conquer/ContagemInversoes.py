def merge_and_count(L1, L2) -> tuple[int, list]:
    
    merged_list : list = []
    inversoes = ponteiro_L1 = ponteiro_L2 = 0
    tamanho_L1 = len(L1)
    tamanho_L2 = len(L2)
    
    while((tamanho_L1 - ponteiro_L1) and (tamanho_L2 - ponteiro_L2)):
        elemento_L1 = L1[ponteiro_L1]
        elemento_L2 = L2[ponteiro_L2]
        if(elemento_L2 < elemento_L1): #lista = [4, 5, 3, 1, 2, 6] -> 1, 
            merged_list.append(elemento_L2)
            inversoes+= len(L1) - ponteiro_L1 + 1 
            ponteiro_L1+=1
        else:
            merged_list.append(elemento_L1)
            ponteiro_L2+=2    

    if(not L1):
        merged_list = merged_list + L1[ponteiro_L1:]
    else:
        merged_list = merged_list + L2[ponteiro_L2:]

    return (inversoes, merged_list)

def sort_and_count(L:list):
    tamanho_lista = len(L)
    if  tamanho_lista <= 1:
        return (0, L)
    
    metade = tamanho_lista//2
    L1 = L[0:metade]
    L2 = L[metade:]

    inversoes1 : tuple[int, list] = sort_and_count(L1)
    inversoes2 : tuple[int, list] = sort_and_count(L2)
    inversoes : tuple[int, list] = merge_and_count(L1, L2) 
    
    return (inversoes1[0] + inversoes2[0] + inversoes[0], L)

def main():
    lista = [4, 5, 3, 1, 2, 6]
    sort_and_count(lista)    

if __name__ == "__main__":
    main()
# Sort-and-Count(L)


#   (rₐ, A) = Sort-and-Count(A)
#   (r_b, B) = Sort-and-Count(B)
#   (r, L) = Merge-and-Count(A, B)
#  
#  Return r = rₐ + r_b + r, and the sorted list L


# Merge-and-Count(A, B)
#  Maintain a Current pointer into each list, initialized to
#   point to the front elements
#  Maintain a variable Count for the number of inversions,
#   initialized to 0
#  While both lists are nonempty:
#   Let aᵢ and bⱼ be the elements pointed to by the Current pointer
#   Append the smaller of these two to the output list
#   If bⱼ is the smaller element then
#    Increment Count by the number of elements remaining in A
#   Endif
#   Advance the Current pointer in the list from which the
#    smaller element was selected.
#  EndWhile
#  Once one list is empty, append the remainder of the other list
#   to the output
#  Return Count and the merged list