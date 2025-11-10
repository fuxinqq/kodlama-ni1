#VİZE VE FİNAL NOT HESAPLAMA DEVAMSIZLIK DAHİL
print("NOT HESAPLAMA PROGRAMINA HOŞGELDİNİZ")
print("VİZE VE FİNAL NOTUNUZU GİRİNİZ")
X=int(input())
Y=int(input())
print("DEVAMSIZLIK HAFTA SAYINIZI GİRİNİZ")
D=int(input())
if D<=5:
    Z=(X*0.4)+(Y*0.6)
    if Z>=50:
        print("dersi geçtiniz notunuz:..",Z)
    else:
        print("dersten kaldınız notunuz:..",Z)
else:
    print("devamsızlık hakkınızı aştığınız için devamsızlıktan kaldınız notunuz:..0")
