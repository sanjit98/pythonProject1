# Python3 program to validate the
# PAN Card number using Regular
# Expression
import re

# Function to validate the
# PAN Card number.


def isValidPanCardNo(panCardNo):

	# Regex to check valid
	# PAN Card number
	regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"

	# Compile the ReGex
	p = re.compile(regex)

	# If the PAN Card number
	# is empty return false
	if(panCardNo == None):
		return False

	# Return if the PAN Card number
	# matched the ReGex
	if(re.search(p, panCardNo) and
	len(panCardNo) == 10):
		return True
	else:
		return False

# Driver Code.


# Test Case 1:
str1 = "BNZAA2318J"
print(isValidPanCardNo(str1))

# Test Case 2:
str2 = "23ZAABN18J"
print(isValidPanCardNo(str2))

# Test Case 3:
str3 = "BNZAA2318JM"
print(isValidPanCardNo(str3))

# Test Case 4:
str4 = "BNZAA23184"
print(isValidPanCardNo(str4))

# Test Case 5:
str5 = "BNZAA 23184"
print(isValidPanCardNo(str5))

# This code is contributed by avanitrachhadiya2155
