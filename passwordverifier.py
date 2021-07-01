password=input("enter a password: ")
if len(password)==0:
    print("password can't be null")
elif len(password)<=8:
    print("length of password must be greater than 8")  
num_check=any(a.isdigit() for a in password)  
if num_check==False:
    print("password must contain at least one number") 
up_check=any(a.isupper() for a in password)    
if up_check==False:
    print("password must contain at least one uppercase letter")  
lo_check=any(a.islower() for a in password)
if lo_check==False:
    print("password must contain at least one lower case letter")     