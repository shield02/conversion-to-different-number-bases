base_16 = 'A2B'
n = len(base_16) - 1
dec_val = 0
hex_val = { 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15 }
for i in base_16:
    if i in hex_val:
        i = hex_val[i]
    dec_val += (int(i))*(16**n)
    n = n-1
print(dec_val)