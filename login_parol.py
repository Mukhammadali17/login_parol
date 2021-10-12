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
        

    def log_in(self):
        pass

    def set(self):
        pass

    def login_exists(self):
        pass

    def update_login(self):
        pass

    def update_password(self):
        pass

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