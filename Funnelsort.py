def funnelsort(array):
    k = 32
    n = len(array)
    
    for i in range(0, n, k):
        array[i:i+k] = mergesort(array[i:i+k])
    
    while k < n:
        for i in range(0, n, 2*k):
            left = array[i:i+k]
            right = array[i+k:i+2*k]
            array[i:i+2*k] = merge(left, right)
        k *= 2
    
    return array