def square_it_out(start, end):
    squares = [i ** 2 for i in range(start, end + 1)]
    
    
    even_squares = [num for num in squares if num % 2 == 0]
    odd_squares = [num for num in squares if num % 2 != 0]
    
    
    print(f"All Squares: {squares}")
    print(f"Even Squares: {even_squares}")
    print(f"Odd Squares: {odd_squares}")


start_range = int(input("Enter the beginning of the range: "))
end_range = int(input("Enter the end of the range: "))

square_it_out(start_range, end_range)