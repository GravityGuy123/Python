# NB: The classname has to be in Paschal case e.g MyNameIsSimonAndAmAProgrammer

class BankAccount:
    MINIMUM_BALANCE = 100
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.balance = self.MINIMUM_BALANCE  # start with minimum balance
    
    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        return True
    
    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.balance - amount < self.MINIMUM_BALANCE:
            print("Cannot withdraw beyond minimum balance.")
            return False
        self.balance -= amount
        return True
    
    def check_balance(self) -> dict:
        return {
            "name": self.name,
            "balance": self.balance
        }


# --- Usage ---
ifenna = BankAccount("Ifenna")
print(ifenna.check_balance())

ifenna.deposit(50)
print(ifenna.check_balance())

ifenna.deposit(-550)  # will be rejected
print(ifenna.check_balance())

ifenna.withdraw(30)
print(ifenna.check_balance())

