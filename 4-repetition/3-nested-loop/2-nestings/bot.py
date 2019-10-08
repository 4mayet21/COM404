# need to record length, record how many until you hit X
#reverse it, count again and subtract the two numbers
#from the orginal length

char = "x"
seq = "-x---x--"
seqsp = ""
num1 = 0
num2 = 0
num3 = ((len(seq) - num1))

for item in range(0, len(seq)):
    seqsp = seq[item]
    while seqsp != char:
        num1 = num1 + 1


print(num1)



#revMod = ""
#for item in range(0, len(scrawl)):
#    rev = scrawl[item]
#    revMod = rev + revMod