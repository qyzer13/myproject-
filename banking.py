import re 

class User:
      def __init__(self,name, password, email):
          self.name = name
          self.password = password
          self.email = email
          self.balance = 0.0  # Every new user starts with 0

          
      @staticmethod
      def is_valid_email(email):
         pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
         return bool(re.fullmatch(pattern, email))
class Bank:
      def __init__(self):
      #Store user
          self.users = {}
      def create_account(self):
          while True:
              name = input("username:").strip().capitalize()
              if not name.replace(" ", "").isalpha():
                print("Invalid name! Names can only contain letters and spaces.")
                continue # Added to stop execution and loop back if the name is invalid
              if name in self.users:
                  print("Username already exist")
                  continue


              # Email Validation
              email = input("Email:").strip()

              if not User.is_valid_email(email):
                print("Invalid email! Enter a valid email address.")
                continue
              
              password = input("Enter password (9 characters, including upper, lower, number, and symbol): ")
          
          # Validating length of exactly 9
              if len(password) != 9:
                 print("Password must be exactly 9 characters long.")
                 continue
              if not re.search(r"[A-Z]", password):
                print("Password must contain uppercase")
                continue
              if not re.search(r"[a-z]", password):
                 print("Password must contain a lowercase letter.")
                 continue

              if not re.search(r"[0-9]", password):
                  print("Password must contain a digit.")
                  continue

              if not re.search(r"[^A-Za-z0-9\s]", password):
                  print("Password must contain a special character.")
                  continue
              
          #creating new user object using inputs  
              new_user = User(name, password, email)  
              print("Storing.......")  
              
              #Stored the data into Bank dictionary name as key  
                
              self.users[name] = new_user  
              print("Account created successfully!!")
              
              break
          
      def deposit(self, username):  
         try:
           amount = int(input ("Amount:"))
           if amount <= 0:
               print('Enter valid amount')
           else:
               username.balance += amount  
               print(f'{username.balance}')
         except ValueError:
            print("invalid amount")
      def withdraw(self, username):
        try:
          amount = int(input("Amount:"))
          if amount > username.balance:
            print("Insuffficient found!!!")
          elif amount <= 0:
            print("Amount must be greater than 0")
          else:
            username.balance -= amount
            print("Transaction successful!!")
        except ValueError:
            print("Invalid amount")
      def login(self):  
          if not self.users:  
              print("No account registered yet!.")  
              return  
          name = input("Enter name:").strip().capitalize() 
          password = input("Enter password:")  
          if name in self.users:  
              username = self.users[name]  
              if username.password == password:  
                  print("Login successful!!")  
                   
                  print(f"Welcome back,{username.name}")  
                  print(f"Current balance:{username.balance}")  
                  print("Loading.........")  
                  
                  while True:  
                      print("\n" + "-"*25)  
                      print("      ACCOUNT MENU      ")  
                      print("-"*25)  
                      print("1. Check Balance")  
                      print("2. Deposit Money")  
                      print("3. Withdraw Money")  
                      print("4. Transfer Funds")  
                      print("5. View Transaction History")  
                      print("6. Logout")  
                      choice = int(input("Choose an option: "))  
                      if choice == 6:
                        break
                      elif choice == 1:  
                          print(f"Current balance:{username.balance}")
                      elif choice == 2:
                           self.deposit(username)
                        #self refers to the current Bank object. It makes your class reusable without depending on a globally defined variable.
                      elif choice == 3:
                           self.withdraw(username)
              else:  
                  print("Incorrect password!\n")  
          else:  
              print("User not found!\n")
      

my_bank = Bank()

print("Welcome to Wema".center(30, '=').upper())

while True:
    print("""
    1. Create account
    2. Login
    3. Exit
    """)

    try:
        choose = int(input("Enter a choice: "))

        if choose == 1:
            my_bank.create_account()

        elif choose == 2:
            my_bank.login()

        elif choose == 3:
            print("Thank you for banking with Wema!")
            break

        else:
            print("Invalid choice! Select 1, 2 or 3.")

    except ValueError:
        print("Invalid input! Please enter a number.")
