KEY = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

def xor(data, key):
    return bytes(b ^ key for b in data)

for key in range(256):
    try:
        print(key, xor(KEY, key).decode())
    except:
        pass