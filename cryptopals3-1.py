import binascii

a= '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

a_bin = binascii.unhexlify(a)
strings = (''.join(chr(ab ^ key) for ab in a_bin) for key in range(256))
print(strings)
print(max(strings, key=lambda s: s.count(' ')))
