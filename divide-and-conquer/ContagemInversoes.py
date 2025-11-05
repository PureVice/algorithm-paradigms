# Sort-and-Count(L)
#  If the list has one element then
#   there are no inversions
#  Else
#   Divide the list into two halves:
#    A contains the first ⌈n/2⌉ elements
#    B contains the remaining ⌊n/2⌋ elements
#   (rₐ, A) = Sort-and-Count(A)
#   (r_b, B) = Sort-and-Count(B)
#   (r, L) = Merge-and-Count(A, B)
#  Endif
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