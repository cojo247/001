age = int(input('Enter your age:'))
if age >= 0 and age <= 17:
    print('Kids')
if age > 17 and age < 66:
    print('Adults')
if age > 65:
    print('Seniors')  
if age < 0:
    print('not allowed')