import math
import random
print("\nInput")
n = int(input("\n->Enter N(length of codeword)        :"))
k = int(input("->Enter K(length of information bits):"))

info_bits = [i for i in range(0, 2**k)]
print("\n->Decimal :",info_bits)

bitlen = len(bin(max(info_bits))[2:])

info_bits = [(bin(i)[2:]) for i in info_bits]
print("->Binary  :",info_bits)

for i in info_bits:
    k = len(i)
    if k != bitlen:
        info_bits[info_bits.index(i)] = (bitlen - k) * "0" + i

print("\n->information word:",info_bits)

info_bits1 = [i for i in info_bits]
info_bits2 = [i for i in info_bits]

for i in info_bits1:
    c = i.count('1')
    if (c) % 2 == 0:
        info_bits1[info_bits1.index(i)] = i +(n-k-1)*'0'+bin(0)[2:]

    else:
        info_bits1[info_bits1.index(i)] = i +(n-k-1)*'0'+bin(1)[2:]
print("\n->code word 1:",info_bits1)

for i in info_bits2:
    c = i.count('1')
    if (c) % 2 == 0:
        info_bits2[info_bits2.index(i)] = i +(n-k-1)*'0'+bin(1)[2:]

    else:
        info_bits2[info_bits2.index(i)] = i +(n-k-1)*'0'+bin(0)[2:]
print("->code word 2:",info_bits2)

length = min(len(info_bits1),len(info_bits2))//2
info_bits3= [random.choice(info_bits1) for _ in range(length)]
info_bits3 += [random.choice(info_bits2) for _ in range(length)]

random.shuffle(info_bits3)
print("->code word 3:",info_bits3)

#coditions to satisfy the linearity
# 1. all zeros
# 2. sum of 2 cw's is also a cw
# 3. min ham is = min dist
count=0
def zero_vector_check(x): 
    global count
    if '0'*len(x[0]) in x:
        count+=1
        print("\n * It satisies the 1st condition")
    else:
        print("\n * It does not satifies the 1st condition")
    
def sum_check(x):
    flag=0
    global count
    num_bits=len(x[0])
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            xor_result = bin(int(x[i], 2) ^ int(x[j], 2))[2:].zfill(num_bits)
            if xor_result not in x:
                #print(f"XOR of {x[i]} and {x[j]} is {xor_result}, not found in the list.")
                break
            else:
                #print(f"XOR of {x[i]} and {x[j]} is {xor_result}, found in the list.")
                flag+=1
    if flag == (((len(x) - 1) * len(x)) / 2)  :
        print(" * It satisies the 2nd condition")
        count +=1
    else:
        print(" * It does not satisies the 2nd condition")

def hamming_check(x):
    global count
    flag = 0
    num_bits = len(x[0])
    min_weight = float('inf')
    
    for i in x:
        if '1' in i:
            weight = i.count('1')  
            min_weight = min(min_weight, weight)
            #print(min_weight)
    
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            xor_result = bin(int(x[i], 2) ^ int(x[j], 2))[2:].zfill(num_bits)
            ones_xor = xor_result.count('1')  
            #print(ones_xor)
            if min_weight == ones_xor:
                flag += 1

    if flag >= 1:
        count+=1
        print(" * It satisfies the 3rd condition") 
    else:
        print(" * It does not satisfy the 3rd condition")
    
    if count==3:
        print(" * YES, IT'S A LINEAR BLOCK CODE]\n")
    else:
        print(" * NO, IT'S NOT A LINEAR BLOCK CODE\n")
        


print("\n1. CODEWORD - 1")
zero_vector_check(info_bits1)
sum_check(info_bits1)
hamming_check(info_bits1)

print("2. CODEWORD - 2")
zero_vector_check(info_bits2)
sum_check(info_bits2)
hamming_check(info_bits2)

print("3. CODEWORD - 3")
zero_vector_check(info_bits3)
sum_check(info_bits3)
hamming_check(info_bits3)
