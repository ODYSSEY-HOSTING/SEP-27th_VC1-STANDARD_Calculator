print(     '호스팅 계산기 (vc1-STANDARD)')
print("=======================================")
vcore=int(input('vm의 코어 수를 입력하세요(숫자만 입력하세요): '))
ram=int(input('ram 용량을 입력하세요(숫자만 입력하세요): '))
vcoreresult= int(1500)*vcore
ramresult= int(1200)*ram
if ram>=32:
    ramplus=int(15000)
elif ram>=16:
    ramplus=int(11000)
elif ram>=9:
    ramplus=int(8500)
elif ram>=5:
    ramplus=int(2500)
else:
    ramplus=int(0)

if vcore>=32:
    vcoreplus=int(57900)
elif vcore>=24:
    vcoreplus=int(37500)
elif vcore>=16:
    vcoreplus=int(22500)
elif vcore>=12:
    vcoreplus=int(10500)
elif vcore>=8:
    vcoreplus=int(5500)
elif vcore>=6:
    vcoreplus=int(3500)
else:
    vcoreplus=int(0)

default=int(4500)

print("=======================================")

result = vcoreresult+ramresult+ramplus+vcoreplus+default
print('계산 결과:', result,'(KRW)')