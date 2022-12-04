# x = int(input('Enter the number you want to convert: '))
# y = int(input('Enter 2 or 16 or 10 as the current base: '))

def to_base2(x):
    """ Convert a number to base 2

        Arguments:
        ------------------------
        x: an int value

        Returns:
        ------------------------
        base_2: str base 2 values
    """
    base_2 = ''                   # int to empty string

    x = int(x)                    # convert x vals to int

    while x//2 > 0:
        remd = x%2                # get the remainder
        base_2 += str(remd)       # convert rem to str and to base_2
        x = x//2                  # reset x
    base_2 += str(x)              # add the last rem to base_2
    base_2 = base_2[::-1]         # reverse base_2

    # if base_2 len not multiple of 3, pad leading zeros
    if len(base_2) % 3 == 1:
        base_2 = '00' + base_2
    elif len(base_2) % 3 == 2:
        base_2 = '0' + base_2

    return base_2

def from_2_to_8(x):
    """ Convert a number base 2 to base 16

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

def to_base8(x):
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

def to_base16(x):
    """ Convert a number to base 16

        Arguments:
        ------------------------
        x: an int value

        Returns:
        ------------------------
        base_16: base 16 values
    """
    base_16 = ''                       # init base 16 to empty string

    hex_char = '0123456789ABCDEF'      # all hex-decimal values

    x = int(x)                         # convert x vals to int

    while x//16 > 0:
        remd = x%16                    # get the remainder
        base_16 += hex_char[remd]      # convert rem to str and to base_16
        x = x//16                      # reset x
    base_16 += hex_char[x]             # add the last rem to base_16
    base_16 = base_16[::-1]            # reverse base_16

    return base_16

def from_16_to_10(base16):
    """ Convert a number from base 16 to base 8

        Arguments:
        ------------------------
        base16: string of base 16 digits

        Returns:
        ------------------------
        base_10: base 10 int vals
    """
    hex_val = { 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15 }

    base16 = str(base16)                  # convert base16 vals to str

    n = len(base16) - 1                   # get value to be used as power
    base_10 = 0                           # init base 10 to zero

    for i in base16:
        if i in hex_val.keys():           # check for each digit in hex_val
            i = hex_val[i]                # set i to be base 10 equival val
        base_10 += (int(i))*(16**n)       # build up base 10 value
        n-=1                              # decrease n
    
    return base_10

def to_base(x, y=8):
    """ Convert a number from a specified base to base 8

        Arguments:
        ------------------------
        x: int val
        y: int val

        Returns:
        ------------------------
        base_8: str of base 8 values
    """
    i_x = x              # keep initial value of x
    i_y = y              # keep initial value of y

    # covert base 2 to base 8
    if y == 2: 
        # convert to base 2
        base_2 = to_base2(x)
            
        # convert to base 8
        base_8 = from_2_to_8(base_2)

        return f'{i_x} base {i_y} is {base_2}, and {base_2} converted to base {8} is {base_8}'

    # convert base 16 to base 8
    elif y == 16:
        # convert to base 16
        base_16 = to_base16(x)

        # convert from base 16 to base 10
        base_10 = from_16_to_10(base_16)
        
        # convert from base 10 to base 2
        #base_2 = to_base2(base_10)

        # convert to base 8
        base_8 = to_base8(base_10)

        return f'{i_x} base {i_y} is {base_16}, and {base_16} converted to base {8} is {base_8}'

    # convert base 10 to base 8
    elif y == 10: 
        # convert to base 8
        base_8 = to_base8(x)

        return f'{i_x} base {i_y} converted to base {8} is {base_8}'

    # y is in base 8
    else: 
        return f'Your number {i_x} is assummed to already be in base {i_y}'

print(to_base(58,2))
print(to_base(58,10))
print(to_base(58,16))
print(to_base(58))

print('-----------------------------')

print(to_base(700,2))
print(to_base(700,10))
print(to_base(700,16))
print(to_base(700))
