# lower to upper and the other way round case converter

ask = input("Do you want to covert the text to uppercase or to lowercase? (lower, upper) ")
if ask == "upper":
    pass
elif ask == "lower":
    pass
else:
    print('invalid input, you can only enter "lower" or "upper"')
    exit()

text = input("Enter the text: ")

if ask == "lower":
    converted = text.lower()
    print(converted)
elif ask == "upper":
    converted = text.upper()
    print(converted)
