def encode(string_encode, shift):
  result = ""
  i = 0
  while i < len(string_encode):
    result += chr(ord(string_encode[i]) + shift)
    i += 1

  return result

print(encode("EncodeThis", 1))