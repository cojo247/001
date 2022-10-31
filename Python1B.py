#Assignment.Python1
#NAME : COREY A. JONES 
#DATE: OCTOBER 30

#first prime numbers up to 100

rangelist=list(range(3,100))
list_num = []
for i in rangelist:
    x = i
    if x == 2 or x == 3 or x == 5 or x == 7 or x == 9 or (x % 2) > 0 and (x % 3) > 0 and (x % 5) > 0 and (x % 7) > 0 and (x % 9) > 0:
        list_num.append(x) 
        print(x)
# 2 
# 3
# 5
# 7         
# 9
# 11