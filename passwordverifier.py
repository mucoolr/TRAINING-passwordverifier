password=input("Enter Password :")

password_list=list(password)

if len(password)==0:
    print("password can't be null")
elif len(password)<=8:
    print("password length should be greater than 8")
num_check=any(a.isdigit() for a in password_list)
if num_check==False:
    print("password must contain at least one number")
up_check=any(a.isupper() for a in password_list)
if up_check==False:
    print("password must contain at least one upper case")  
lo_check=any(a.islower() for a in password_list)      
if lo_check==False:
    print("password must contain at least one lower case")