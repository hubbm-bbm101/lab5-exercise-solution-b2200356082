def eemail(a):
    if "." and "@" in a:
        return True
    else:
        return False
email = str(input("Please enter your email:"))
if eemail(email) == True:
    print(email + "is a valid e-mail thank you.")
else:
    print(email + "isn't a valid e-mail please write correctly.")

        