class IntegerToRoman:
    def __init__(self, number):
        """Initialize the class with the integer provided by the user."""
        self.number = number

    def compute_roman(self):
        """Computes and returns the equivalent Roman numeral for the integer."""
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_numeral = ""
        num = self.number

        for i in range(len(val)):
            while num >= val[i]:
                roman_numeral += syb[i]
                num -= val[i]
                
        return roman_numeral


if __name__ == "__main__":
    try:
        user_input = int(input("Enter an integer: "))
        
        converter = IntegerToRoman(user_input)
        
        result = converter.compute_roman()
        print(f"The Roman numeral for {user_input} is: {result}")
        
    except ValueError:
        print("Invalid input! Please enter a whole number.")