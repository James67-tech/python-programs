age = 24
is_verified = True

if 100 >age >=18 and is_verified:
    print("You are eligible to vote.")
elif age >= 18 and not is_verified:
    print("Get Verified to vote.")
else:
    print("You are not eligible to vote.")