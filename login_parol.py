import mysql.connector
import platform
import os
import sys

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='qw0002004',
    database='alii'
)

my_cursor = my_db.cursor()
my_cursor.execute("CREATE TABLE IF NOT EXISTS login_parol(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,"
                  "first_name VARCHAR(30) NOT NULL,"
                  "last_name VARCHAR(30) NOT NULL,"
                  "age INT(3) NOT NULL,"
                  "login VARCHAR(30) NOT NULL,"
                  "password VARCHAR(30) NOT NULL)")


class User:
    def __init__(self):
        self.clear()
        self.menu()

    def menu(self):
        self.clear()
        print("""
        [1] Sign up
        [2] Log in
        [0] Exit  """)
        self.choose()

    def choose(self):
        user_input = input("Please choose one of them: ").strip()
        input_options = ['1', '2', '0']
        while user_input not in input_options:
            self.clear()
            self.invalid_input()
            print("""
                    [1] Sign up
                    [2] Log in
                    [0] Exit  """)
            user_input = input("Please choose one of them: ").strip()
        if user_input == '1':
            self.sign_up()
        elif user_input == '2':
            self.log_in()
        else:
            self.exit()

    # _________________________________sign up_________________________________________________________
    def sign_up(self):
        # ______first_name___________
        self.clear()
        first_name = input("Enter your first_name: ").strip().capitalize()
        while not first_name.isalpha():
            self.clear()
            self.invalid_input()
            first_name = input("Enter your first_name: ").strip().capitalize()
        # ______last_name__________
        self.clear()
        last_name = input("Enter your last_name: ").strip().capitalize()
        while not last_name.isalpha():
            self.clear()
            self.invalid_input()
            last_name = input("Enter your last_name: ").strip().capitalize()
        # _______age_______________
        self.clear()
        age = input("Enter your age: ").strip()
        while not age.isnumeric():
            self.clear()
            self.invalid_input()
            age = input("Enter your age: ").strip()
        # _____________login and password______________
        while True:
            # _____logini
            self.clear()
            login = input("Enter your login: ").strip().lower()
            if not self.login_exists(login):
                while not login.isalnum():
                    self.clear()
                    self.invalid_input()
                    login = input("Enter your login: ").strip().lower()
            # _______passwordi
            self.clear()
            password = input("Enter your password: ").strip()
            check_password = input("Confirm your password: ").strip()
            while password != check_password:
                self.clear()
                self.invalid_input()
                password = input("Enter your password: ").strip()
                check_password = input("Confirm your password: ").strip()
            # _______________databasega yozish parti__________________________________________
            my_cursor.execute(f"INSERT INTO login_parol(first_name,last_name,age,login,password) VALUES"
                              f"('{first_name}','{last_name}',{age},'{login}','{password}')")
            my_db.commit()
            print("You've created to system")
            self.menu()

    # _______________________________________log_in__________________________________________
    def log_in(self):
        self.clear()
        login_ = input("Enter your login: ").strip().lower()
        while not login_.isalnum():
            self.clear()
            self.invalid_input()
            login_ = input("Enter your login: ").strip().lower()
        my_cursor.execute(f"SELECT * from login_parol WHERE login = '{login_}'")
        result = my_cursor.fetchall()
        if not result:
            self.clear()
            print("I cant find this login")
            self.log_in()
        else:
            self.clear()
            current_password = result[0][5]
            password_ = input("Enter your password: ").strip()
            while not password_.isalnum():
                self.clear()
                self.invalid_input()
                password_ = input("Enter your password: ").strip().lower()
            if password_ == current_password:
                self.clear()
                print("You've entered to system")
                self.set()
            else:
                self.clear()
                print("Password doesnt match")
                self.log_in()

    def set(self):
        self.clear()
        print("""
        [1] Update login
        [2] Update password
        [3] log out
        [4] Delete account
        [5] Exit""")
        settings_input = input("Choose one of them: ")
        input_options = ['1','2','3','4','5']
        while settings_input not in input_options:
            self.clear()
            self.invalid_input()
            print("""
                    [1] Update login
                    [2] Update password
                    [3] log out
                    [4] Delete account
                    [5] Exit""")
            settings_input = input("Choose one of them: ")
        if settings_input == '1':
            self.update_login()
        elif settings_input == '2':
            self.update_password()
        elif settings_input == '3':
            self.log_out()
        elif settings_input == '4':
            self.delete_account()
        else:
            self.exit()



    @staticmethod
    def login_exists(logiin):
        my_cursor.execute(f"SELECT * FROM login_parol WHERE login = '{logiin}'")
        result = my_cursor.fetchall()
        return result

    def update_login(self):
        self.clear()
        current_login = input("Enter your login: ").strip().lower()
        while not current_login.isalnum():
            self.clear()
            self.invalid_input()
            current_login = input("Enter your login: ").strip().lower()
        while not self.login_exists(current_login):
            self.clear()
            print("I cant find this login")
            current_login = input("Enter your login: ").strip().lower()
        self.clear()
        new_login = input("Enter your new login: ").strip().lower()
        while not new_login.isalnum():
            self.clear()
            self.invalid_input()
            new_login = input("Enter your new login: ").strip().lower()
        my_cursor.execute(f"UPDATE login_parol SET login = '{new_login}' WHERE login = '{current_login}'")
        my_db.commit()
        self.clear()
        self.set()


    def update_password(self):
            self.clear()
            current_password = input("Enter your password: ").strip()
            while not current_password.isalnum():
                self.clear()
                self.invalid_input()
                current_login = input("Enter your password: ").strip()
            my_cursor.execute(f"SELECT password FROM login_parol WHERE password = '{current_password}'")
            result = my_cursor.fetchall()
            while result is None:
                self.clear()
                print("I cant find this password")
                current_login = input("Enter your password: ").strip()
                my_cursor.execute(f"SELECT password FROM login_parol WHERE password = '{current_password}'")
                result = my_cursor.fetchall()
            self.clear()
            new_password = input("Enter your new password: ").strip()
            while not new_password.isalnum():
                self.clear()
                self.invalid_input()
                new_password = input("Enter your new password: ").strip()
            my_cursor.execute(f"UPDATE login_parol SET password = '{new_password}' WHERE password = '{current_password}'")
            my_db.commit()
            self.clear()
            self.set()

    def log_out(self):
        pass

    def delete_account(self):
        pass

    @staticmethod
    def exit():
        print("Thank you bro")
        sys.exit()

    @staticmethod
    def is_str_empty(string):
        return not string

    @staticmethod
    def invalid_input():
        print("Invalid input. BRO please try again :)")

    @staticmethod
    def clear():
        if platform.system() == 'Linux':
            os.system("clear")
        elif platform.system() == 'Windows':
            os.system("cls")
        else:
            print("Sorry ukam :)")


user1 = User()
