def solution(n):
    arr = []
    
    while n > 0:
        arr.append(str(n%3))
        n //= 3
        
    return int(''.join(arr), 3)