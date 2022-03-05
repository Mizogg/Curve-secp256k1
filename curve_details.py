from tinyec.ec import SubGroup, Curve

name = 'secp256k1'
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
h = 1

curve = Curve(a, b, SubGroup(p, g, n, h), name)
pubKey = curve.g*1
pubKeyHalves = curve.g * 1
PublicKey = curve.g * 1
halfl= (n//2)
halfh= n-(n//2) # 578128044618658097711785492504343953926418782139537452191302581570759080747169
quarterl= (n//4)
quarterh= n-(n//4)
eighthl= (n//8)
eighthh= n-(n//8)
sixteenthl= (n//16)
sixteenthh= n-(n//16)
thirtytwol= (n//32)
thirtytwoh= n-(n//32)
sixtyfourthl= (n//64)
sixtyfourthh= n-(n//64)
onehundred28l= (n//128)
onehundred28h= n-(n//128)
twohundred56l= (n//256)
twohundred56h= n-(n//256)   # 115339776388732929035197660848497720712787417543609768037360611722996606176000
fivehundred12l= (n//512)
fivehundred12h= n-(n//512)  # 115565932813024562229384322928592814282812490911342336209982887432257383835169
onethousand24l= (n//1024)   # 113078212145816597093331040047546785012536683866284086311137854630388829584
onethousand24h= n-(n//1024) # 115679011025170378826477653968640361067825027595208620296294025286887772664753
twothousand48l= (n//2048)
twothousand48h= n-(n//2048)
fourthousand48l= (n//4096)
fourthousand48h= n-(n//4096)
eightthousand192l= (n//8192)
eightthousand192h= n-(n//8192)
sixteenthousand384l= (n//16384)
sixteenthousand384h= n-(n//16384)
thirtytwohousand768l= (n//32768)
thirtytwohousand768h= n-(n//32768)
sixtyfivehousand536l= (n//65536)
sixtyfivehousand536h= n-(n//65536)
onehundredand31072l= (n//131072)
onehundredand31072h= n-(n//131072)
twohundredand62144l= (n//262144)
twohundredand62144h= n-(n//262144)
fivehundredand24288l= (n//524288)
fivehundredand24288h= n-(n//524288)
onemilland048576l= (n//1048576)
onemilland048576h= n-(n//1048576)

start = int(input("start range Min 1-115679011025170378826477653968640361067825027595208620296294025286887772664753 ->  "))
#mag=int(input("Magnitude Jump Stride -> "))
display =int(input("Pick Display 1 Full 2 Less"))
stop = 10

#while start < stop:
    #start+=mag
k1 = int(start)
HEXk1 = "%064x" % k1
k2 = (k1*(n-1))%n
HEXk2 = "%064x" % k2

k3 = (k1*(halfl))%n
HEXk3 = "%064x" % k3
k3h = (k1*(halfh))%n
HEXk3h = "%064x" % k3h

k4 = (k1*(quarterl))%n
HEXk4 = "%064x" % k4
k4h = (k1*(quarterh))%n
HEXk4h = "%064x" % k4h

k8 = (k1*(eighthl))%n
HEXk8 = "%064x" % k8
k8h = (k1*(eighthh))%n
HEXk8h = "%064x" % k8h

k16 = (k1*(sixteenthl))%n
HEXk16 = "%064x" % k16
k16h = (k1*(sixteenthh))%n
HEXk16h = "%064x" % k16h

k32 = (k1*(thirtytwol))%n
HEXk32 = "%064x" % k32
k32h = (k1*(thirtytwoh))%n
HEXk32h = "%064x" % k32h

k64 = (k1*(sixtyfourthl))%n
HEXk64 = "%064x" % k64
k64h = (k1*(sixtyfourthh))%n
HEXk64h = "%064x" % k64h

k128 = (k1*(onehundred28l))%n
HEXk128 = "%064x" % k128
k128h = (k1*(onehundred28h))%n
HEXk128h = "%064x" % k128h

k256 = (k1*(twohundred56l))%n
HEXk256 = "%064x" % k256
k256h = (k1*(twohundred56h))%n
HEXk256h = "%064x" % k256h

k512 = (k1*(fivehundred12l))%n
HEXk512 = "%064x" % k512
k512h = (k1*(fivehundred12h))%n
HEXk512h = "%064x" % k512h

k1024 = (k1*(onethousand24l))%n
HEXk1024 = "%064x" % k1024
k1024h = (k1*(onethousand24h))%n
HEXk1024h = "%064x" % k1024h

k2048 = (k1*(twothousand48l))%n
HEXk2048 = "%064x" % k2048
k2048h = (k1*(twothousand48h))%n
HEXk2048h = "%064x" % k2048h

k4096 = (k1*(fourthousand48l))%n
HEXk4096 = "%064x" % k4096
k4096h = (k1*(fourthousand48h))%n
HEXk4096h = "%064x" % k4096h

k8192 = (k1*(eightthousand192l))%n
HEXk8192 = "%064x" % k8192
k8192h = (k1*(eightthousand192h))%n
HEXk8192h = "%064x" % k8192h

k16384 = (k1*(sixteenthousand384l))%n
HEXk16384 = "%064x" % k16384
k16384h = (k1*(sixteenthousand384h))%n
HEXk16384h = "%064x" % k16384h

k32768 = (k1*(thirtytwohousand768l))%n
HEXk32768 = "%064x" % k32768
k32768h = (k1*(thirtytwohousand768h))%n
HEXk32768h = "%064x" % k32768h

k65536 = (k1*(sixtyfivehousand536l))%n
HEXk65536 = "%064x" % k65536
k65536h = (k1*(sixtyfivehousand536h))%n
HEXk65536h = "%064x" % k65536h

k131072 = (k1*(onehundredand31072l))%n
HEXk131072 = "%064x" % k131072
k131072h = (k1*(onehundredand31072h))%n
HEXk131072h = "%064x" % k131072h

k262144 = (k1*(twohundredand62144l))%n
HEXk262144 = "%064x" % k262144
k262144h = (k1*(twohundredand62144h))%n
HEXk262144h = "%064x" % k262144h

k524288 = (k1*(fivehundredand24288l))%n
HEXk524288 = "%064x" % k524288
k524288h = (k1*(fivehundredand24288h))%n
HEXk524288h = "%064x" % k524288h

k1048576 = (k1*(onemilland048576l))%n
HEXk1048576 = "%064x" % k1048576
k1048576h = (k1*(onemilland048576h))%n
HEXk1048576h = "%064x" % k1048576h

key1 = pubKey*k1
key2 = pubKey*k2
key3 = pubKey*k3
key3h = pubKey*k3h
key4 = pubKey*k4
key4h = pubKey*k4h
key8 = pubKey*k8
key8h = pubKey*k8h
key16 = pubKey*k16
key16h = pubKey*k16h
key32 = pubKey*k32
key32h = pubKey*k32h
key64 = pubKey*k64
key64h = pubKey*k64h
key128 = pubKey*k128
key128h = pubKey*k128h
key256 = pubKey*k256
key256h = pubKey*k256h
key512 = pubKey*k512
key512h = pubKey*k512h
key1024 = pubKey*k1024
key1024h = pubKey*k1024h
key2048 = pubKey*k2048
key2048h = pubKey*k2048h
key4096 = pubKey*k4096
key4096h = pubKey*k4096h
key8192 = pubKey*k8192
key8192h = pubKey*k8192h
key16384 = pubKey*k16384
key16384h = pubKey*k16384h
key32768 = pubKey*k32768
key32768h = pubKey*k32768h
key65536 = pubKey*k65536
key65536h = pubKey*k65536h
key131072 = pubKey*k131072
key131072h = pubKey*k131072h
key262144 = pubKey*k262144
key262144h = pubKey*k262144h
key524288 = pubKey*k524288
key524288h = pubKey*k524288h
key1048576 = pubKey*k1048576
key1048576h = pubKey*k1048576h

BIN1 = bin(k1)[2:]
Length1= len(BIN1)
full1= BIN1.zfill(8)

BIN2 = bin(k2)[2:]
Length2= len(BIN2)
full2= BIN2.zfill(8)

BIN3 = bin(k3)[2:]
Length3= len(BIN3)
full3= BIN3.zfill(8)
BIN3h = bin(k3h)[2:]
Length3h= len(BIN3h)
full3h= BIN3h.zfill(8)

BIN4 = bin(k4)[2:]
Length4= len(BIN4)
full4= BIN4.zfill(8)
BIN4h = bin(k4h)[2:]
Length4h= len(BIN4h)
full4h= BIN4h.zfill(8)

BIN8 = bin(k8)[2:]
Length8= len(BIN8)
full8= BIN8.zfill(8)
BIN8h = bin(k8h)[2:]
Length8h= len(BIN8h)
full8h= BIN8h.zfill(8)

BIN16 = bin(k16)[2:]
Length16= len(BIN16)
full16= BIN16.zfill(8)
BIN16h = bin(k16h)[2:]
Length16h= len(BIN16h)
full16h= BIN16h.zfill(8)

BIN32 = bin(k32)[2:]
Length32= len(BIN32)
full32= BIN32.zfill(8)
BIN32h = bin(k32h)[2:]
Length32h= len(BIN32h)
full32h= BIN32h.zfill(8)

BIN64 = bin(k64)[2:]
Length64= len(BIN64)
full64= BIN64.zfill(8)
BIN64h = bin(k64h)[2:]
Length64h= len(BIN64h)
full64h= BIN64h.zfill(8)

BIN128 = bin(k128)[2:]
Length128= len(BIN128)
full128= BIN128.zfill(8)
BIN128h = bin(k128h)[2:]
Length128h= len(BIN128h)
full128h= BIN128h.zfill(8)

BIN256 = bin(k256)[2:]
Length256= len(BIN256)
full256= BIN256.zfill(8)
BIN256h = bin(k256h)[2:]
Length256h= len(BIN256h)
full256h= BIN256h.zfill(8)

BIN512 = bin(k512)[2:]
Length512= len(BIN512)
full512= BIN512.zfill(8)
BIN512h = bin(k512h)[2:]
Length512h= len(BIN512h)
full512h= BIN512h.zfill(8)

BIN1024 = bin(k1024)[2:]
Length1024= len(BIN1024)
full1024= BIN1024.zfill(8)
BIN1024h = bin(k1024h)[2:]
Length1024h= len(BIN1024h)
full1024h= BIN1024h.zfill(8)

BIN2048 = bin(k2048)[2:]
Length2048= len(BIN2048)
full2048= BIN2048.zfill(8)
BIN2048h = bin(k2048h)[2:]
Length2048h= len(BIN2048h)
full2048h= BIN2048h.zfill(8)

BIN4096 = bin(k4096)[2:]
Length4096= len(BIN4096)
full4096= BIN4096.zfill(8)
BIN4096h = bin(k4096h)[2:]
Length4096h= len(BIN4096h)
full4096h= BIN4096h.zfill(8)

BIN8192 = bin(k8192)[2:]
Length8192= len(BIN8192)
full8192= BIN8192.zfill(8)
BIN8192h = bin(k8192h)[2:]
Length8192h= len(BIN8192h)
full8192h= BIN8192h.zfill(8)

BIN16384 = bin(k16384)[2:]
Length16384= len(BIN16384)
full16384= BIN16384.zfill(8)
BIN16384h = bin(k16384h)[2:]
Length16384h= len(BIN16384h)
full16384h= BIN16384h.zfill(8)

BIN32768 = bin(k32768)[2:]
Length32768= len(BIN32768)
full32768= BIN32768.zfill(8)
BIN32768h = bin(k32768h)[2:]
Length32768h= len(BIN32768h)
full32768h= BIN32768h.zfill(8)

BIN65536 = bin(k65536)[2:]
Length65536= len(BIN65536)
full65536= BIN65536.zfill(8)
BIN65536h = bin(k65536h)[2:]
Length65536h= len(BIN65536h)
full65536h= BIN65536h.zfill(8)

BIN131072 = bin(k131072)[2:]
Length131072= len(BIN131072)
full131072= BIN131072.zfill(8)
BIN131072h = bin(k131072h)[2:]
Length131072h= len(BIN131072h)
full131072h= BIN131072h.zfill(8)

BIN262144 = bin(k262144)[2:]
Length262144= len(BIN262144)
full262144= BIN262144.zfill(8)
BIN262144h = bin(k262144h)[2:]
Length262144h= len(BIN262144h)
full262144h= BIN262144h.zfill(8)

BIN524288 = bin(k524288)[2:]
Length524288= len(BIN524288)
full524288= BIN524288.zfill(8)
BIN524288h = bin(k524288h)[2:]
Length524288h= len(BIN524288h)
full524288h= BIN524288h.zfill(8)

BIN1048576 = bin(k1048576)[2:]
Length1048576= len(BIN1048576)
full1048576= BIN1048576.zfill(8)
BIN1048576h = bin(k1048576h)[2:]
Length1048576h= len(BIN1048576h)
full1048576h= BIN1048576h.zfill(8)

if display == 1:
    print('\nPrivatekey (dec)k1: ', k1, 'Length Bits = ', Length1, '\nPrivatekey (hex)k1: ', HEXk1)
    print ('\nk1 X: ',key1.x, '\nk1 Y: ',key1.y)
    print ('Binary k1: ', full1)

    print('\nPrivatekey (dec)k2: ', k2,'Length Bits = ', Length2, '\nPrivatekey (hex)k2: ', HEXk2)
    print ('\nk2 X: ',key2.x, '\nk2 Y: ',key2.y)
    print ('Binary k2: ', full2)

    print('\nPrivatekey (dec)k3: ', k3,'Length Bits = ', Length3, '\nPrivatekey (hex)k3: ', HEXk3)
    print ('\nk3 X: ',key3.x, '\nk3 Y: ',key3.y)
    print ('Binary k3: ', full3)
    
    print('\nPrivatekey (dec)k3h: ', k3h,'Length Bits = ', Length3h, '\nPrivatekey (hex)k3h: ', HEXk3h)
    print ('\nk3h X: ',key3h.x, '\nk3 Y: ',key3h.y)
    print ('Binary k3h: ', full3h)

    print('\nPrivatekey (dec)k4: ', k4,'Length Bits = ', Length4, '\nPrivatekey (hex)k4: ', HEXk4)
    print ('\nk4 X: ',key4.x, '\nk4 Y: ',key4.y)
    print ('Binary k4: ', full4)

    print('\nPrivatekey (dec)k4h: ', k4h,'Length Bits = ', Length4h, '\nPrivatekey (hex)k4h: ', HEXk4h)
    print ('\nk4h X: ',key4h.x, '\nk4h Y: ',key4h.y)
    print ('Binary k4h: ', full4h)

    print('\nPrivatekey (dec)k8: ', k8,'Length Bits = ', Length8, '\nPrivatekey (hex)k8: ', HEXk8)
    print ('\nk8 X: ',key8.x, '\nk8 Y: ',key8.y)
    print ('Binary k8: ', full8)

    print('\nPrivatekey (dec)k8h: ', k8h,'Length Bits = ', Length8h, '\nPrivatekey (hex)k8h: ', HEXk8h)
    print ('\nk8h X: ',key8h.x, '\nk8h Y: ',key8h.y)
    print ('Binary k8h: ', full8h)

    print('\nPrivatekey (dec)k16: ', k16,'Length Bits = ', Length16, '\nPrivatekey (hex)k16: ', HEXk16)
    print ('\nk16 X: ',key16.x, '\nk16 Y: ',key16.y)
    print ('Binary k16: ', full16)

    print('\nPrivatekey (dec)k16h: ', k16h,'Length Bits = ', Length16h, '\nPrivatekey (hex)k16h: ', HEXk16h)
    print ('\nk16h X: ',key16h.x, '\nk16h Y: ',key16h.y)
    print ('Binary k16h: ', full16h)

    print('\nPrivatekey (dec)k32: ', k32,'Length Bits = ', Length32, '\nPrivatekey (hex)k32: ', HEXk32)
    print ('\nk32 X: ',key32.x, '\nk32 Y: ',key32.y)
    print ('Binary k32: ', full32)

    print('\nPrivatekey (dec)k32h: ', k32h,'Length Bits = ', Length32h, '\nPrivatekey (hex)k32h: ', HEXk32h)
    print ('\nk32h X: ',key32h.x, '\nk32h Y: ',key32h.y)
    print ('Binary k32h: ', full32h)

    print('\nPrivatekey (dec)k64: ', k64,'Length Bits = ', Length64, '\nPrivatekey (hex)k64: ', HEXk64)
    print ('\nk64 X: ',key64.x, '\nk64 Y: ',key64.y)
    print ('Binary k64: ', full64)

    print('\nPrivatekey (dec)k64h: ', k64h,'Length Bits = ', Length64h, '\nPrivatekey (hex)k64h: ', HEXk64h)
    print ('\nk64h X: ',key64h.x, '\nk64h Y: ',key64h.y)
    print ('Binary k64h: ', full64h)
    
    print('\nPrivatekey (dec)k128: ', k128,'Length Bits = ', Length128, '\nPrivatekey (hex)k128: ', HEXk128)
    print ('\nk128 X: ',key128.x, '\nk128 Y: ',key128.y)
    print ('Binary k128: ', full128)

    print('\nPrivatekey (dec)k128h: ', k128h,'Length Bits = ', Length128h, '\nPrivatekey (hex)k128h: ', HEXk128h)
    print ('\nk128h X: ',key128h.x, '\nk128h Y: ',key128h.y)
    print ('Binary k128h: ', full128h)
    
    print('\nPrivatekey (dec)k256: ', k256,'Length Bits = ', Length256, '\nPrivatekey (hex)k256: ', HEXk256)
    print ('\nk256 X: ',key256.x, '\nk256 Y: ',key256.y)
    print ('Binary k256: ', full256)

    print('\nPrivatekey (dec)k256h: ', k256h,'Length Bits = ', Length256h, '\nPrivatekey (hex)k256h: ', HEXk256h)
    print ('\nk256h X: ',key256h.x, '\nk256h Y: ',key256h.y)
    print ('Binary k256h: ', full256h)
    
    print('\nPrivatekey (dec)k512: ', k512,'Length Bits = ', Length512, '\nPrivatekey (hex)k512: ', HEXk512)
    print ('\nk512 X: ',key512.x, '\nk512 Y: ',key512.y)
    print ('Binary k512: ', full512)

    print('\nPrivatekey (dec)k512h: ', k512h,'Length Bits = ', Length512h, '\nPrivatekey (hex)k512h: ', HEXk512h)
    print ('\nk512h X: ',key512h.x, '\nk512h Y: ',key512h.y)
    print ('Binary k512h: ', full512h)
    
    print('\nPrivatekey (dec)k1024: ', k1024,'Length Bits = ', Length1024, '\nPrivatekey (hex)k1024: ', HEXk1024)
    print ('\nk1024 X: ',key1024.x, '\nk1024 Y: ',key1024.y)
    print ('Binary k1024: ', full1024)

    print('\nPrivatekey (dec)k1024h: ', k1024h,'Length Bits = ', Length1024h, '\nPrivatekey (hex)k1024h: ', HEXk1024h)
    print ('\nk1024h X: ',key1024h.x, '\nk1024h Y: ',key1024h.y)
    print ('Binary k1024h: ', full1024h)
    
    print('\nPrivatekey (dec)k2048: ', k2048,'Length Bits = ', Length2048, '\nPrivatekey (hex)k2048: ', HEXk2048)
    print ('\nk2048 X: ',key2048.x, '\nk2048 Y: ',key2048.y)
    print ('Binary k2048: ', full2048)

    print('\nPrivatekey (dec)k2048h: ', k2048h,'Length Bits = ', Length2048h, '\nPrivatekey (hex)k2048h: ', HEXk2048h)
    print ('\nk2048h X: ',key2048h.x, '\nk2048h Y: ',key2048h.y)
    print ('Binary k2048h: ', full2048h)
    
    print('\nPrivatekey (dec)k4096: ', k4096,'Length Bits = ', Length4096, '\nPrivatekey (hex)k4096: ', HEXk4096)
    print ('\nk4096 X: ',key4096.x, '\nk4096 Y: ',key4096.y)
    print ('Binary k4096: ', full4096)

    print('\nPrivatekey (dec)k4096h: ', k4096h,'Length Bits = ', Length4096h, '\nPrivatekey (hex)k4096h: ', HEXk4096h)
    print ('\nk4096h X: ',key4096h.x, '\nk4096h Y: ',key4096h.y)
    print ('Binary k4096h: ', full4096h)
    
    print('\nPrivatekey (dec)k8192: ', k8192,'Length Bits = ', Length8192, '\nPrivatekey (hex)k8192: ', HEXk8192)
    print ('\nk8192 X: ',key8192.x, '\nk8192 Y: ',key8192.y)
    print ('Binary k8192: ', full8192)

    print('\nPrivatekey (dec)k8192h: ', k8192h,'Length Bits = ', Length8192h, '\nPrivatekey (hex)k8192h: ', HEXk8192h)
    print ('\nk8192h X: ',key8192h.x, '\nk8192h Y: ',key8192h.y)
    print ('Binary k8192h: ', full8192h)
    
    print('\nPrivatekey (dec)k16384: ', k16384,'Length Bits = ', Length16384, '\nPrivatekey (hex)k16384: ', HEXk16384)
    print ('\nk16384 X: ',key16384.x, '\nk16384 Y: ',key16384.y)
    print ('Binary k16384: ', full16384)

    print('\nPrivatekey (dec)k16384h: ', k16384h,'Length Bits = ', Length16384h, '\nPrivatekey (hex)k16384h: ', HEXk16384h)
    print ('\nk16384h X: ',key16384h.x, '\nk16384h Y: ',key16384h.y)
    print ('Binary k16384h: ', full16384h)
    
    print('\nPrivatekey (dec)k32768: ', k32768,'Length Bits = ', Length32768, '\nPrivatekey (hex)k32768: ', HEXk32768)
    print ('\nk32768 X: ',key32768.x, '\nk32768 Y: ',key32768.y)
    print ('Binary k32768: ', full32768)

    print('\nPrivatekey (dec)k32768h: ', k32768h,'Length Bits = ', Length32768h, '\nPrivatekey (hex)k32768h: ', HEXk32768h)
    print ('\nk32768h X: ',key32768h.x, '\nk32768h Y: ',key32768h.y)
    print ('Binary k32768h: ', full32768h)
    
    print('\nPrivatekey (dec)k65536: ', k65536,'Length Bits = ', Length65536, '\nPrivatekey (hex)k65536: ', HEXk65536)
    print ('\nk65536 X: ',key65536.x, '\nk65536 Y: ',key65536.y)
    print ('Binary k65536: ', full65536)

    print('\nPrivatekey (dec)k65536h: ', k65536h,'Length Bits = ', Length65536h, '\nPrivatekey (hex)k65536h: ', HEXk65536h)
    print ('\nk65536h X: ',key65536h.x, '\nk65536h Y: ',key65536h.y)
    print ('Binary k65536h: ', full65536h)
    
    print('\nPrivatekey (dec)k131072: ', k131072,'Length Bits = ', Length131072, '\nPrivatekey (hex)k131072: ', HEXk131072)
    print ('\nk131072 X: ',key131072.x, '\nk131072 Y: ',key131072.y)
    print ('Binary k131072: ', full131072)

    print('\nPrivatekey (dec)k131072h: ', k131072h,'Length Bits = ', Length131072h, '\nPrivatekey (hex)k131072h: ', HEXk131072h)
    print ('\nk131072h X: ',key131072h.x, '\nk131072h Y: ',key131072h.y)
    print ('Binary k131072h: ', full131072h)
    
    print('\nPrivatekey (dec)k262144: ', k262144,'Length Bits = ', Length262144, '\nPrivatekey (hex)k262144: ', HEXk262144)
    print ('\nk262144 X: ',key262144.x, '\nk262144 Y: ',key262144.y)
    print ('Binary k262144: ', full262144)

    print('\nPrivatekey (dec)k262144h: ', k262144h,'Length Bits = ', Length262144h, '\nPrivatekey (hex)k262144h: ', HEXk262144h)
    print ('\nk262144h X: ',key262144h.x, '\nk262144h Y: ',key262144h.y)
    print ('Binary k262144h: ', full262144h)
    
    print('\nPrivatekey (dec)k524288: ', k524288,'Length Bits = ', Length524288, '\nPrivatekey (hex)k524288: ', HEXk524288)
    print ('\nk524288 X: ',key524288.x, '\nk524288 Y: ',key524288.y)
    print ('Binary k524288: ', full524288)

    print('\nPrivatekey (dec)k524288h: ', k524288h,'Length Bits = ', Length524288h, '\nPrivatekey (hex)k524288h: ', HEXk524288h)
    print ('\nk524288h X: ',key524288h.x, '\nk524288h Y: ',key524288h.y)
    print ('Binary k524288h: ', full524288h)
    
    print('\nPrivatekey (dec)k1048576: ', k1048576,'Length Bits = ', Length1048576, '\nPrivatekey (hex)k1048576: ', HEXk1048576)
    print ('\nk1048576 X: ',key1048576.x, '\nk1048576 Y: ',key1048576.y)
    print ('Binary k1048576: ', full1048576)

    print('\nPrivatekey (dec)k1048576h: ', k1048576h,'Length Bits = ', Length1048576h, '\nPrivatekey (hex)k1048576h: ', HEXk1048576h)
    print ('\nk1048576h X: ',key1048576h.x, '\nk1048576h Y: ',key1048576h.y)
    print ('Binary k1048576h: ', full1048576h)
if display == 2:
    print('(dec)STOP: ', k2,'Length Bits = ', Length2)
    print('(dec)1048576INV: ', k1048576h,'Length Bits = ', Length1048576h)
    print('(dec)524288INV: ', k524288h,'Length Bits = ', Length524288h)
    print('(dec)262144INV: ', k262144h,'Length Bits = ', Length262144h)
    print('(dec)131072INV: ', k131072h,'Length Bits = ', Length131072h)
    print('(dec)65536INV: ', k65536h,'Length Bits = ', Length65536h)
    print('(dec)32768INV: ', k32768h,'Length Bits = ', Length32768h)
    print('(dec)16384INV: ', k16384h,'Length Bits = ', Length16384h)
    print('(dec)8192INV: ', k8192h,'Length Bits = ', Length8192h)
    print('(dec)4096INV: ', k4096h,'Length Bits = ', Length4096h)
    print('(dec)2048INV: ', k2048h,'Length Bits = ', Length2048h)
    print('(dec)1024INV: ', k1024h,'Length Bits = ', Length1024h)
    print('(dec)512INV : ', k512h,'Length Bits = ', Length512h)
    print('(dec)256INV : ', k256h,'Length Bits = ', Length256h)
    print('(dec)128INV : ', k128h,'Length Bits = ', Length128h)
    print('(dec)64INV  : ', k64h,'Length Bits = ', Length64h)
    print('(dec)32INV  : ', k32h,'Length Bits = ', Length32h)
    print('(dec)16INV  : ', k16h,'Length Bits = ', Length16h)
    print('(dec)8INV   : ', k8h,'Length Bits = ', Length8h)
    print('(dec)4INV   : ', k4h,'Length Bits = ', Length4h)
    print('(dec)HALFINV: ', k3h,'Length Bits = ', Length3h)
    print('(dec)HALF   : ', k3,'Length Bits = ', Length3)
    print('(dec)4      : ', k4,'Length Bits = ', Length4)
    print('(dec)8      : ', k8,'Length Bits = ', Length8)
    print('(dec)16     : ', k16,'Length Bits = ', Length16)
    print('(dec)32     : ', k32,'Length Bits = ', Length32)
    print('(dec)64     : ', k64,'Length Bits = ', Length64)
    print('(dec)128    : ', k128,'Length Bits = ', Length128)
    print('(dec)256    : ', k256,'Length Bits = ', Length256)
    print('(dec)512    : ', k512,'Length Bits = ', Length512)
    print('(dec)1024   : ', k1024,'Length Bits = ', Length1024)
    print('(dec)2048   : ', k2048,'Length Bits = ', Length2048)
    print('(dec)4096   : ', k4096,'Length Bits = ', Length4096)
    print('(dec)8192   : ', k8192,'Length Bits = ', Length8192)
    print('(dec)16384   : ', k16384,'Length Bits = ', Length16384)
    print('(dec)32768   : ', k32768,'Length Bits = ', Length32768)
    print('(dec)65536   : ', k65536,'Length Bits = ', Length65536)
    print('(dec)131072   : ', k131072,'Length Bits = ', Length131072)
    print('(dec)262144   : ', k262144,'Length Bits = ', Length262144)
    print('(dec)524288   : ', k524288,'Length Bits = ', Length524288)
    print('(dec)1048576   : ', k1048576,'Length Bits = ', Length1048576)
    print('(dec)START  : ', k1, 'Length Bits = ', Length1)