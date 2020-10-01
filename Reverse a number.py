# Reversing digits in number
try:
    # Convert input into string, if failed print error message
    # Convert entered int to str and reverse it
    # Convert back str into int
    print(int(str(int(input()))[::-1]))
except ValueError:
    print("Enter a valid number to reverse the digits")
