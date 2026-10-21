# Convert number to Roman symbol 
# Greedy Algorithm approach

number = int(input("Typ een getal: "))

# Function number to roman symbol
def num_roman(number):

    # Check if number is within range
    if number < 1 or number > 3999:
        return "Numer is not within convertion range!"

    

    else:
        result = "" 
        # Dictionary for roman symbols
        roman_symbol= {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C',   90: 'XC',  50: 'L',  40: 'XL',
        10: 'X',     9: 'IX',   5: 'V',   4: 'IV',
        1: 'I'}


        for value, symbol in roman_symbol.items():
            # Calculat division
            amount = number // value
            # Set result
            result += symbol * amount
            # Calculate modulo
            number =  number % value

    return result
print(f"Roman symbol is: {num_roman(number)}")
