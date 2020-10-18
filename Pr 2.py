a=int(input("Primul nr dictat este"))
b=int(input("Al doilea nr dictat este"))
c=int(input("Al treilea nr dictat este"))
if(0<a<32000) and (0<b<32000) and (0<c<32000):
    if(a<+c) and (b<a+c) and (c<a+b):
        print("Da")
    else:
        print("Nu")
else:
    print("Numerele introduse sunt incorecte")
    