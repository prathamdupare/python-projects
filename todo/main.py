# TODO program written in python .

import os
import pickle
from datetime import datetime

todos = []

TODO_FILE = "todos.pkl"


class Todo:
    def __init__(self, title, created_at, is_completed=False):
        self.title = title
        self.created_at = created_at
        self.is_completed = is_completed


def save_to_file():
    with open(TODO_FILE, "wb") as file:
        pickle.dump(todos, file)


def read_from_file():
    global todos
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "rb") as file:
            todos = pickle.load(file)


def add_todo():
    title = input("Type your todo: ")
    created_at = datetime.now().strftime("%d/%m %H:%M")
    todo = Todo(title, created_at)
    todos.append(todo)
    save_to_file()


def print_all_todos():
    print("+------+------------------------+---------------------+------------------+")
    print("| ID   |       Todo Title        |     Created At       |    Completed   |")
    print("+------+------------------------+---------------------+------------------+")

    for i, todo in enumerate(todo):
        print(
            f"| {i + 1:2} | {todo.title:35} | {todo.created_at:12}| {'tick' if todo.is_completed else 'cross':^11} |"
        )
        print(
            "+------+------------------------+---------------------+------------------+"
        )


def mark_as_complete():
    print_all_todos()
    try:
        print_all_todos()
        todo_id = int(input("Enter the id of the todo: ")) - 1
        todos[todo_id].is_completed = True
        save_to_file()
    except IndexError:
        print("Invalid Todo ID")
    except ValueError:
        print("Invalid Input")


def delte_todo():
    print_all_todos()
    try:
        todo_id = int(input("Enter the id of the todo: ")) - 1
        del todos[todo_id]
        save_to_file()
    except IndexError:
        print("Invalid Todo ID")
    except ValueError:
        print("Invalid Input")


def show_options():
    while True:
        user_choice = input(
            "Type A to add, D to delete, C to mark complete, or Q to quit"
        ).upper()
        if user_choice == "A":
            add_todo()
        elif user_choice == "D":
            delte_todo()
        elif user_choice == "C":
            mark_as_complete()
        elif user_choice == "Q":
            print("Thank you for using this app.")
            break
        else:
            print("Command not found")
        print_all_todos()


def is_this_your_first_time():
    if os.path.exists(TODO_FILE):
        read_from_file()
        print_all_todos()
    else:
        print("Welcome to TaskMaster")
        add_todo()
        print_all_todos()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[32;1m")
    is_this_your_first_time()
    show_options()
