def alphabator(lst):
    for num in lst:
        if num in range(1,27):
            yield chr(num+64)
        else:
            yield num
    
