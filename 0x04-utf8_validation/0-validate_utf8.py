#!/usr/bin/python3
"""Method that determines if a given data set
represents a valid UTF-8 encoding"""


def count_num_of_leading_set_bits(num):
    """returns the number of leading set bits (1)"""
    num_set_bits = 0
    helper = 1 << 7
    while helper & num:
        num_set_bits += 1
        helper = helper >> 1
    return num_set_bits


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    bits_count = 0
    for x in range(len(data)):
        if bits_count == 0:
            bits_count = count_num_of_leading_set_bits(data[x])
            '''1-byte (format: 0xxxxxxx)'''
            if bits_count == 0:
                continue
            """character in UTF-8 can be 1 - 4 bytes long"""
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            """checks if current byte has correct format"""
            if not (data[x] & (1 << 7) and not (data[x] & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
