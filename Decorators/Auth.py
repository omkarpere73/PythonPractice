def auth(func):
    def wrapper(*args , **kwargs):
        if user == "admin" and passwd == 0000:
            print("Login Succesfull")
        else:
            print ("Login Denied")
    return wrapper

@auth
def myfunc(str , passwd):
    user = str
    passwd = passwd
    return user , passwd
user = str(input("Enter Username : "))
passwd = int(input("Enter Passwd : "))

myfunc()
