# from functions import get_todos, write_todos
from modules import functions
import time

# text = """
# How to not procrastinate
# Silence your inner critic
# Reach stimulating literature
# """

# print(text)
now = time.strftime("%b %d, %Y %H:%M")
print("It is ", now)

while True:
    user_action = input("Please type: add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif 'show' in user_action:
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)

    elif 'edit' in user_action:
        numToDo = int(user_action[5:])
        numToDo = numToDo - 1

        todos = functions.get_todos()

        newToDo = input('Enter the new To Do :')
        todos[numToDo] = newToDo + "\n"

        functions.write_todos(todos)

    elif 'complete' in user_action:
        numComplete = int(user_action[9:])
        numComplete = numComplete - 1

        todos = functions.get_todos()

        todo_removed = todos[numComplete].strip('\n')

        todos.pop(numComplete)

        functions.write_todos(todos)

        message = f"Removed {todo_removed} as it is completed"
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("You entered invalid command")

print('Bye for now!')
