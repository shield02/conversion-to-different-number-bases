#!/usr/bin/env python

def from_2_to_8(x):
    """ Convert a number base 2 to base 8

        Arguments:
        ------------------------
        x: an int value

        Returns:
        ------------------------
        base_8: str base 8 values
    """
    base_8 = ''
    count = 0
    digit = 0

    x = str(x)                                    # convert x vals to str

    for i in range(len(x),0,-1):
        if count < 3:
            digit += int(x[i-1])*(2**count)       # build the base 8 digits
            count+=1                              # increment count by 1
        
        if count == 3:
            base_8 += str(digit)                  # convert to string, add to base_8 variable
            count, digit = (0, 0)                 # reset count and digit
    
    base_8 = base_8[::-1]                         # reverse the digits of base_8

    return base_8

def from_16_to_10(x):
    """ Convert a number from base 16 to base 8

        Arguments:
        ------------------------
        x: int of base 16 digits

        Returns:
        ------------------------
        base_10: base 10 int vals
    """
    hex_val = { 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15 }

    base16 = str(x)                       # convert x vals to str

    n = len(base16) - 1                   # get value to be used as power
    base_10 = 0                           # init base 10 to zero

    for i in base16:
        if i in hex_val.keys():           # check for each digit in hex_val
            i = hex_val[i]                # set i to be base 10 equival val
        base_10 += (int(i))*(16**n)       # build up base 10 value
        n-=1                              # decrease n
    
    return base_10

def from_10_to_8(x):
    """ Convert a number to base 16

        Arguments:
        ------------------------
        x: an int value

        Returns:
        ------------------------
        base_8: str base 8 values
    """
    base_8 = ''                # init to empty string

    x = int(x)                 # convert x vals to int

    while x//8 > 0:
        remd = x%8             # get the remainder
        base_8 += str(remd)    # convert rem to str and to base_2
        x = x//8               # reset x
    base_8 += str(x)           # add the last rem to base_2
    base_8 = base_8[::-1]      # reverse base_2

    return base_8

def to_base8(x,y=10):
    """ Convert a number to base 8

        Arguments:
        ------------------------
        x: int or str val
        y: int val, default 10

        Returns:
        ------------------------
        base_8: str of base 8 values
    """
    if y == 2: 
        # convert to base 8
        base_8 = from_2_to_8(x)

        return f'{x} base {y} converted to base {8} is {base_8}'
    
    elif y == 16:
        # convert from base 16 to base 10
        base_10 = from_16_to_10(x)
        
        # convert from base 10 to base 8
        base_8 = from_10_to_8(base_10)

        return f'{x} base {y} converted to base {8} is {base_8}'
    
    elif y == 8: 
        # y is in base 8
        return f'{x} is assummed to already be in base {y}'
        
    else: 
        # convert from base 10 to base 8
        base_8 = from_10_to_8(x)

        return f'{x} base {y} converted to base {8} is {base_8}'

print(to_base8('001010111100',y=2))
print(to_base8(1274,y=8))
print(to_base8('2BC',y=16))
print(to_base8(700))

