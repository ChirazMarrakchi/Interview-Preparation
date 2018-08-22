def upperChar(c):
    if not 'a' <= c <= 'z':
        return c
    
    return chr(ord(c) - ord('a') + ord('A'))

def solutions(x, k):
    if x is None or len(x) == 0 or k <= 0:
        return
    
     
    x ,i = list(x) ,0
    
    while i <  len(x):
        # delete dash characters from list X
        if x[i] == '-':
            x.pop(i)

        # increment counters
        i +=1 
        
         
    if len(x) <= k:
        for i in range(len(x)):
            x[i] = upperChar(x[i])

        x = "".join(x)
        return x
    
    i, j = len(x)-1, k
    while i >= 0:
        if j == 0:
            # insert a dash
            x = x[0:i+1] + ["-"] + x[i+1:]
            # re-initialize j
            j = k
        
        # upper-case
        x[i] = upperChar(x[i])

        # decrement counters
        j -= 1
        i -= 1

    return "".join(x)

print (solutions ("abcdefg", 3))
print (solutions ("ab-cde-fg", 3))
print (solutions("aba2 bbababababa",2))
