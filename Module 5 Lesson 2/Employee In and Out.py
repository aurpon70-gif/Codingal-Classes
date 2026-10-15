class Employee:

    def __init__(self):
        print("Employee class initialized.")

    def __del__(self):
        print("Employee class destroyed.")

def Create_obj():
    print('Making Object')
    obj = Employee()
    print('Returning Object')
    return obj

print('Calling Create_obj()')
obj = Create_obj()
print('Program Ended')