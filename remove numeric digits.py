# Python code to demonstrate
# how to remove numeric digits from string
# using join and isdigit

# initialising string
ini_string = "Sanjit123for127sanjit"

# printing initial ini_string
print("initial string : ", ini_string)

# using join and isdigit
# to remove numeric digits from string
res = ''.join([i for i in ini_string if not i.isdigit()])

# printing result
print("final string : ", res)
