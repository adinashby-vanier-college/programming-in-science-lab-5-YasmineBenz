# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    shape=''
    if n >= 1:
        for i in range(n):
            shape +='*'
    shape+='\n'
    for i in range(n - 2):
       shape += '*'
       for i in range(n - 2):
           shape += ' '
       shape += '*\n'
    if n > 1:
        for i in range(n):
            shape += '*'
    return shape.rstrip()

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result=''
    for i in range(1, n+1):
        for j in range (1, i+1):
            result += str(j) 
        result+='\n' 
    return result.rstrip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    result=0
    for i in range(n):
        result+= (i+1)
    return result

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    shape=''
    for i in range(1,n+1):
        for j in range(n-i):
            shape+=' '
        for j in range(2*i-1):
            shape+='*'
        shape+='\n'
    return shape.rstrip()




