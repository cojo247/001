#Question 1:
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_"+user_name+"!")
user_name = input('Enter USERNAME: ')
hello_name(user_name)
