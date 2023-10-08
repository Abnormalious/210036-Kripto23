print("Ptext : ", end="")
ptext = input().upper()
print("Key   : ", end="")
key = input().upper()
ctext = ""
dtext = ""

for i in range(len(ptext)) :
    ctext += chr(((ord(ptext[i])-ord('A'))+ord(key[i%len(key)])-ord('A'))%26+ord('A'))

for i in range(len(ctext)) :
    dtext += chr(((ord(ctext[i])-ord('A'))-ord(key[i%len(key)])-ord('A'))%26+ord('A'))

print("Ctext : " + ctext, "Dtext : " + dtext, sep="\n")