#Codigo Cesar
encrip=input("Ingresa tu codigo: ")
encripMayus=encrip.upper()
text=""
aux={}

for i in encripMayus:
    if i.isalpha():
        r=int(encripMayus.count(i))
        aux.update({r:i})
    else:
        continue

clave=max(aux.keys())
num=(aux[clave])

llave=(ord("E")-ord(num))%26

for i in encripMayus:
    if i.isupper():
        unicod=ord(i)
        index=ord(i)-ord("A")
        nuev_index=(index+llave)%26
        nuev_unicode=nuev_index+ord("A")
        nuev_carac=chr(nuev_unicode)
        text=text+nuev_carac
    else:
        text+=i

print(text)
