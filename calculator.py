class Cal:
    def sum(self, *args):
        return sum(args)
        
    def subtract(self, *args):
        if not args:
            return 0
        result = args[0] #first number
        
        for num in args[1:]: #loop through result and other num
              result -= num
        
        return result
        
    def multiply(self, *args):
         if not args:
             return 0
         result = args[0]
         
         for num in args[1:]:
             result *= num
         return result
         
    def divide(self, *args):
         if not args:
             return 0
         result = args[0]
         try:
             for num in args[1:]:
                 result /= num
             return result
         except ZeroDivisionError:
             return "Number can not be divide by zero"
    def average(self, *args):
        if not args:
            return 0
        result = args[0]
        for num in args[1:]:
            return sum(result)
    
            
cal = Cal()

while True:
    print("\n=== CLASS PROJECT CALCULATOR ===")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ").strip()
    
    if choice == '5':
        print("Goodbye!")
        break
        
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please select 1-5.")
        continue

    # Gather numbers all at once on one line
    raw_input = input("Enter your numbers separated by spaces (e.g., 10 2 5.5): ")
    
    try:
        # Convert the space-separated text into a list of actual decimal numbers
        user_numbers = [float(x) for x in raw_input.split()]
        
        if not user_numbers:
            print("You didn't enter any numbers!")
            continue
            
    except ValueError:
        print("Error: Please only enter valid numbers separated by single spaces.")
        continue

    # Map the menu choice to the correct class method and unpack with *
    if choice == '1':
        print(f"Result: {cal.sum(*user_numbers)}")
    elif choice == '2':
        print(f"Result: {cal.subtract(*user_numbers)}")
    elif choice == '3':
        print(f"Result: {cal.multiply(*user_numbers)}")
    elif choice == '4':
        print(f"Result: {cal.divide(*user_numbers)}")
        