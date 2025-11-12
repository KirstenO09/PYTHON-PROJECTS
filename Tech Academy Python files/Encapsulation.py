# This class called BankAccount demonstrates encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        # Protected attribute: can be accessed by subclasses
        self._owner = owner

        # Private attribute: cannot be accessed directly outside the class
        self.__balance = balance

    # Public method to display account info
    def display_account(self):
        print(f"Account Owner: {self._owner}")
        print(f"Account Balance: ${self.__balance}")

    # Protected method: intended for internal or subclass use
    def _apply_fee(self, fee_amount):
        self.__balance -= fee_amount
        print(f"A fee of ${fee_amount} has been applied.")

    # Private method: only accessible within this class
    def __secret_bonus(self):
        self.__balance += 100
        print("A secret bonus of $100 has been added!")

    # Public method that internally uses the private method
    def trigger_bonus(self):
        self.__secret_bonus()

    # Public method to safely update the balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

# Create an object of BankAccount
account1 = BankAccount("Kirsten", 500)

# Access public method
account1.display_account()

# Access protected method (allowed but discouraged outside class)
account1._apply_fee(25)

# Try accessing private method directly (will raise an error)
# account1.__secret_bonus()  # Uncommenting this will cause an AttributeError

# Use public method that internally calls the private method
account1.trigger_bonus()

# Deposit money using public method
account1.deposit(150)

# Final account status
account1.display_account()
