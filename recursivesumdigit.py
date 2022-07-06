def superDigit(n, k):
    # Write your code here
    digits = map(int, list(n))
    return get_super_digit(str(sum(digits) * k))

def get_super_digit(p):
    if len(p) == 1:
        return int(p)
    else:
        digits = map(int, list(p))
        return get_super_digit(str(sum(digits)))

n='9875'
k=1   
'''super_digit(9875)   	9+8+7+5 = 29 
	super_digit(29) 	2 + 9 = 11
	super_digit(11)		1 + 1 = 2
	super_digit(2)		= 2  '''
k=4
'''superDigit(p) = superDigit(9875987598759875)
                9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    superDigit(p) = superDigit(116)
                1+1+6 = 8
    superDigit(p) = superDigit(8)'''
print(superDigit(n,k))
