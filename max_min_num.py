def max_min_num(L):
     max = min = L[0]
     for num in L:
          if num > max:
                max = num
          if num < min:
                min = num
     return max, min

