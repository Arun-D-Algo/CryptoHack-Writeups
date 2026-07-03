text = "label"
flag = ""
for i in text:
    flag += chr(ord(i)^13)
print("crypto{"+flag+"}")