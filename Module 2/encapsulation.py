import random

class Bank:
    def __init__(self, salary, account):
        self.__salary = salary #private attribute
        self._account = account #protected attribute
        self.employee_id = random.randint(1,100) #public attribute

    def get_salary(self): #getter
        return self.__salary
    
    def set_salary(self, salary): #setter
        if salary > 10000:
            print("Salary cannot exceed 10,000 for trainees")
        else:
            self.__salary = salary

class Company(Bank):
    def transfer_salary(self):
        self._account += self._Bank__salary #Classes cannot inherit private stuff

    def _show_account(self): #protected method
        return f"Amount in account: {self._account}"
    
    def _store_id(self): #protected method
        return self.employee_id
    
ids = Company(7000, 1000)
#print("Your salary for this month:" , ids.__salary) #Public Access
print("Your account at IDS:" , ids._account) #Protected accessed through subclass (ok?)
ids.transfer_salary()
print(ids._show_account())
#print(ids.__salary) #displays error
print(ids._Bank__salary) #this works but not recommended because whats the point of making it private then?
print(ids._store_id()) #agaim, protected methods should not be accessed outside either

#From the 2 lines above, we have seen that it is unethical to access protected/private stuff outside the class,
# which is why it's better as a programmer to use getters and setters, where you can get the private attribute not by
# directly accessing it or changing it using the object, but by using methods that can fetch it for you (getter) or
# that can set it/change it for you (if you have any conditions also) (setter)

print(f"Previous Stipend at IDS: {ids.get_salary()}") #getter - before setting
ids.set_salary(9000) #setter - changed
print(f"New Stipend at IDS: {ids.get_salary()}") #getter - after changing
