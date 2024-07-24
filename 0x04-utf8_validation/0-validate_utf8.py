#!/usr/bin/python3
"""Method that determines if a given data set
represents a valid UTF-8 encoding"""


def count_num_of_leading_set_bits(byte_value):
  """ function to counts the number of leading set bits (1) in a byte"""
  num_set_bits = 0
  mask = 1 << 7
  while byte_value & mask:
    num_set_bits += 1
    mask >>= 1
  return num_set_bits

def is_valid_utf8(byte_sequence):
  """Determines if the given byte sequence represents valid UTF-8 encoding."""
  num_bytes_to_process = 0
  for byte in byte_sequence:
    if num_bytes_to_process == 0:
      num_bytes_to_process = count_num_of_leading_set_bits(byte)
      if num_bytes_to_process == 0:
        continue  
      if num_bytes_to_process == 1 or num_bytes_to_process > 4:
        return False  
    else:
      if not (byte & (1 << 7) and not (byte & (1 << 6))):
        return False  
      num_bytes_to_process -= 1
  return num_bytes_to_process == 0
