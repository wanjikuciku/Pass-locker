#!/usr/bin/env python3.6


import random
from user import User
from credentials import Credential


def create_user_account(username, password):
    """
    Function to create a new account
    """
    new_user = User(username, password)
    return new_user


def create_credentials(view_password, account, loginname, password):
    """
    Function to create a new credential
    """
    new_credential = Credential(view_password, account, loginname, password)
    return new_credential


def save_user_account(user):
    """
    Function to save user account
    """
    user.save_user()


def save_credentials(credential):
    """
    Function to save credentials
    """
    credential.save_credential()


def check_existing_users(characters):
    """
    Function that checks if a user exists with those characters and retuen a boolean
    """
    return User.user_exists(characters)


def display_credentials():
    """
    Function that returns the credentials list
    """
    return Credential.display_credentials()


def main():
    print("Hello! Welcome to the Pass_locker. What is your name?")
    username = input()
    print("\n")
    print(f"Hello {username}.")
    while True:
        print("\nUse these short codes below:")
        print("." * 40)
        print("\n ca - create an account, cc - create credentials, gp - generate password, cp - create own password, ex - exit password locker, dc - display credentials, ")
        short_code = input().lower()

        if short_code == 'ca':
            print("New account")
            print("." * 14)

            print("\nEnter your user name")
            print("."*40)
            username = input()

            print("\nEnter a password")
            print("."*40)
            password = input()

            save_user_account(create_user_account(username, password))

            print("\n")
            print(f"New Account {username} created.\n")

        elif short_code == "cc":
            print("\nLogin to your account")
            print("."*40)
            print("\nUsername?")
            print("." * 20)
            username = input()
            print("\nPassword?")
            print("."*20)
            password = input()
            view_password = password
            if check_existing_users(password):
                print("\nWelcome back!")
                print("New Credential")
                print("." * 20)

                print("\nWhich account do the credentials belong to?")
                print("."*40)
                account = input()

                print(f"\nWhat's your login name for the {account} account?")
                print("."*40)
                login_name = input()

                print("\nChoose:")
                print("."*20)
                print(
                    "'gp' - program to generate your password for you, 'cp' - create your own password")
                password_creation_input = input()
                if password_creation_input == "cp":
                    print("\nEnter your password")
                    print("."*20)
                    password = input()
                elif password_creation_input == "gp":
                    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                    password = "".join(random.choice(chars) for _ in range(8))
                    print(f"\nYour password is: **{password}**")

                save_credentials(create_credentials(
                    view_password, account, login_name, password))
                print("\n")
                print(
                    f"New credentials {account}, {login_name}, {password} created")

            else:
                print("Wrong password or username. Please Try again.\n Username?")
                print("."*20)
                username = input()
                print("\nPassword?")
                print("."*20)
                password = input()
                if check_existing_users(password):
                    print("\nWelcome back!")
                else:
                    print("You don't have an account.\n")

        elif short_code == 'dc':
            if display_credentials():
                print("Here is a list of your credentials:")
                print("."*40)

                for credential in display_credentials():
                    print(
                        f"\nAccount: {credential.account}\nLogin Name: {credential.login}\nAccount Password: {credential.password}")
            else:
                print("\n You don't seem to have any credentials saved yet")

        elif short_code == 'ex':
            print("."*50)
            print("Thank you for using Pass-locker...")
            print("."*50)
            break

        else:
            print("Sorry, I didn't get that. Please use the short codes\n")


if __name__ == '__main__':
    main()
