# Q. Make a Register/Login/Change Password/Exit UI
'''
user_info = {}
while True:
    user_input = input('\nWhat would you like to do?\n1. Register (R)\n2. Login (L)\n3. Change Password (C)\n4. Exit (E)\n')
    if user_input.lower() == 'r':
        useremail = input('Enter your email: ')
        userpwd = input('Enter your password: ')
        user_info[useremail]=userpwd
        print('Registered Successfully')
    if user_input.lower() == 'l':
        useremail = input('Enter your email: ')
        if useremail in user_info.keys():
            userpwd = input('Enter your password: ')
            if user_info.get(useremail) == userpwd:
                print('Login Successful')
            else:
                print('Wrong password. Please try again')
        else:
            print('Email not found. Please Register.')
    if user_input.lower() == 'c':
        useremail = input('Enter your email: ')
        if useremail in user_info.keys():
            oldpwd = input('Enter your old password: ')
            if user_info.get(useremail) == oldpwd:
                newpwd = input('Enter new password: ')
                user_info.update({useremail:newpwd})
                print('Password Updated Successfully')
                print(user_info)
            else:
                print('Old password does not match.')
        else:
            print('Email not found.')
    if user_input.lower() == 'e':
        print('See you soon!')
        break
'''     
# try to use more .get()


# Q. Ask the user a couple questions randomly from a question bank and increase/decrease the score
# based on the answers. Store the user's answers also to compare with the final answers at the end
'''
qbank = {
'35+19':{53:False, 54:True, 55:False},
'7+9':{13:False, 20:False, 16:True},
'32-17':{15:True, 17:False, 16:False},
'57-29':{26:False, 28:True, 24:False},
'13*8':{104:True, 109:False, 111:False},
'6*8':{54:False, 48:True, 42:False},
#'8/3':{2.33:False, 2.5:False, 2.66:True},
'72/12':{6:True, 5:False, 4:False}
}

import random
i=0
score = 0
correct_ans = []
user_ans = []
while i!=2:
    print('\n-------Question-------')
    ques = random.choice(list(qbank.keys()))
    print(ques)
    print('------Options-------')
    options = qbank.get(ques)
    for option in options:
        print(option)
        if options.get(option) == True:
            correct_ans.append(option)
    ans = int(input('\nEnter your answer: '))
    user_ans.append(ans)
    if options.get(ans) == True:
        score+=1
    else:
        score-=0.25
    
    
    
    qbank.pop(ques)
    i+=1
print('\nYour score:', score)
print('Your answers:', user_ans)
print('Correct answers:', correct_ans)
'''

# Q. Make a ticking timer function
'''
import time
def timer(seconds):
    minutes, seconds = divmod(seconds, 60)
    while minutes>-1:
        print(f"\r{minutes:02d}:{seconds:02d}", end='')
        time.sleep(1)
        seconds-=1
        if seconds == -1:
            if minutes == 1:
                seconds = (minutes*60)-1
            else:
                seconds = ((minutes*60-((minutes-1)*60))-1)
            minutes-=1
    print(f"\rTime's Up!")

timer(125)
'''

# Q. Check if an email ID is valid
'''
import re

def check_email(email):
    ptrn = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(ptrn, email)

user_input = input('Enter an email ID: ')
res = check_email(user_input)

if res is None:
    print('Email is Invalid')
else:
    print('Email is valid')
'''

# Q. Categorize a list of names into a dictionary where the key is the initial of the name
# and the values are a list of names of that initial
'''
lst = ['shalini', 'shawarma', 'bubbly', 'arnav', 'mimi', 'boba', 'lulu']
names = {}
def cat_names(name_list):
    for name in lst:
        if name[0] not in names:
            names[name[0].lower()] = []
        names[name[0].lower()].append(name)
    return names

print(cat_names(lst))
'''

# Q. Make a register/login/change password system using file handling

def register():
    uname, upwd = [x.strip() for x in input('Enter username, password: ').split(",")]
    isreg = False
    with open(r'C:\Users\Karan\Desktop\ids-python\python-programming\CS-Infotech\users.txt','r') as fp:
        lines = fp.readlines()
        for line in lines:
            username = line.strip().split(",")[0]
            if username == uname:
                print('User already exists')
                isreg = True
    if isreg == False:
        with open(r'C:\Users\Karan\Desktop\ids-python\python-programming\CS-Infotech\users.txt', 'a') as fp:
            fp.write(uname+", "+upwd+"\n")
            print("Registration Successful")

def login():
    uname, upwd = [x.strip() for x in input('Enter username, password: ').split(",")]
    islogin = False
    with open(r'C:\Users\Karan\Desktop\ids-python\python-programming\CS-Infotech\users.txt', 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            username = line.strip().split(",")[0]
            password = line.strip().split(",")[1]
            if username == uname:
                if password == upwd:
                    print("Login Successful")
                else:
                    print("Password incorrect. Try again")
                islogin = True
    if islogin == False:
        print("Username does not exist. Please Register")

import os
def change_pwd():
    current_dir = os.getcwd()
    file_name = 'users1.txt'
    file_path = os.path.join(current_dir, file_name)
    uname, oldpwd, newpwd = [x.strip() for x in input('Enter username, old password, new password: ').split(",")]
    with open(r'C:\Users\Karan\Desktop\ids-python\python-programming\CS-Infotech\users.txt', 'r') as fp, open(file_path, 'w') as fp1:
        lines = fp.readlines()
        for line in lines:
            username = line.strip().split(",")[0]
            actpwd = line.strip().split(",")[1]
            if username != uname:
                fp1.write(line)
            elif username == uname and actpwd == oldpwd:
                fp1.write(username+", "+newpwd+"\n")
    os.remove(r'C:\Users\Karan\Desktop\ids-python\python-programming\CS-Infotech\users.txt')
    os.rename(file_path, r'C:\Users\Karan\Desktop\ids-python\python-programming\CS-Infotech\users.txt')

while True:
    user_in = int(input("\nHi, what would you like to do?\n1. Register\n2. Login\n3. Change password\n4. Exit\n--> "))
    if user_in == 1:
        register()
    elif user_in == 2:
        login()
    elif user_in == 3:
        change_pwd()
    else:
        print("Bye!")
        break

# basically in my change_pwd function, if i dont put the correct username or password, it deletes it???
# i shall fix it soon cuz for now the core concept is done
