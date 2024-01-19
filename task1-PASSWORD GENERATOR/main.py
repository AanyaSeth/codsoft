import string
import random
lenght= int(input("enter lenght of password:"))
#define Data 
lower= string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation
#combine data
all=lower+upper+num +symbols
#use random
temp=random.sample(all,lenght)
#create password
password="".join(temp)
#print password 
print("password is:",password)


        