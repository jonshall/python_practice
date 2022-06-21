"""count_set_bits.py

Function to get number of set bits in binary representation of number
"""
def CountSetBits(num):
 
    count = 0
    while (num):
        num &= (num - 1)
        count += 1
     
    return count
