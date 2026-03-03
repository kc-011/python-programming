class Bank:
    def __init__(self, salary, account):
        self.salary = salary
        self._account = account

class Company(Bank):
    def transfer_salary(self):
        self._account += self.salary

    def _show_account(self):
        return f"Amount in account: {self._account}"

ids = Company(5000, 0)
print("Your salary for this month:" , ids.salary) #Public Access
print("Your account at IDS:" , ids._account) #Protected accessed through subclass (ok?)
ids.transfer_salary()
print(ids._show_account())
