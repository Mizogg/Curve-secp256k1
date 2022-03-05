from tinyec.ec import SubGroup, Curve

#578128044618658097711785492504343953926418782139537452191302581570759080747169
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

mylist=('2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096', '8192', '16384', '32768', '65536', '131072', '262144', '524288', '1048576', '2097152', '4194304', '8388608', '16777216', '33554432', '67108864', '134217728', '268435456', '536870912', '1073741824', '2147483648', '4294967296', '8589934592', '17179869184', '34359738368', '68719476736', '137438953472', '274877906944', '549755813888', '1099511627776', '2199023255552', '4398046511104', '8796093022208', '17592186044416', '35184372088832', '70368744177664', '140737488355328', '281474976710656', '562949953421312', '1125899906842624', '2251799813685248', '4503599627370496', '9007199254740992', '18014398509481984', '36028797018963970', '72057594037927940', '144115188075855870', '288230376151711740', '576460752303423500', '1152921504606847000', '2305843009213694000', '4611686018427388000', '9223372036854776000', '18446744073709552000', '36893488147419103000', '73786976294838210000', '147573952589676410000')

def curve_div():
     for i in range(0,len(mylist)):
        tinv= (n//(int(mylist[i])))
        binv= n-(n//(int(mylist[i])))
        k = (k1*(tinv))%n
        HEXk = "%064x" % k
        kh = (k1*(binv))%n
        HEXkh = "%064x" % kh
        key1 = pubKey*k
        key2 = pubKey*kh
        BIN1 = bin(k)[2:]
        Length1= len(BIN1)
        full1= BIN1.zfill(8)
        BIN2 = bin(kh)[2:]
        Length2= len(BIN2)
        full2= BIN2.zfill(8)
        print(f'Point   K{int(mylist[i])} : ', k,' Length Bits = ', Length1)
        print(f'Inverse K{int(mylist[i])} : ', kh,' Length Bits = ', Length2)
 
start = int(input("start range Min 1-115679011025170378826477653968640361067825027595208620296294025286887772664753 ->  ")) 
k1 = int(start)
HEXk1 = "%064x" % k1
k2 = (k1*(n-1))%n
HEXk2 = "%064x" % k2
key1 = pubKey*k1
key2 = pubKey*k2
BIN1 = bin(k1)[2:]
Length1= len(BIN1)
full1= BIN1.zfill(8)
BIN2 = bin(k2)[2:]
Length2= len(BIN2)
full2= BIN2.zfill(8)
print('Start Point  : ', k1, 'Length Bits = ', Length1)
print('Inverse Start: ', k2,'Length Bits = ', Length2)
curve_div()

