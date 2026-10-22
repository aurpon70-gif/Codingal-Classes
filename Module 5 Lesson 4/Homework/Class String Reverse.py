class reverse:
    def __init__(self, s=""):
        self.s = s

    def get_reversed(self):
        return self.s[::-1]



user_input = input("Enter a string: ")

obj = reverse(user_input)

print("Reversed string:", obj.get_reversed())