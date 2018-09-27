def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) > 6 and hasNumbers(newpassword):
        res = True
    else:
        res = False
    return(res)
print(new_password("neee", "sdfdfdsfsdfsdf1231",))