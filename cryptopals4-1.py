import binascii
with open('crypto4.txt', 'r') as crypto:
    f=0
    for line in crypto:
        x=crypto.read(60)
        f+=1
        line_bin = binascii.unhexlify(x)
        strings = (''.join(chr(i ^ key) for i in line_bin) for key in range(256))
        print(max(strings, key=lambda s: s.count(' '))+str(f))
