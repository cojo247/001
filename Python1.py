#Assignment.Python1
#NAME : COREY A. JONES 
#DATE: OCTOBER 30

#cubing numbers in a list up to output of 1000

rangelist=list(range(1,1000))
list_num = []
for i in rangelist:
    x=i**3
    v = x
    list_num.append(v)
    if x <= 1000:
        print(v)        