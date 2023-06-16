#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")  #python datetime format codes
print("It is",now)
while True:
    user_action = input("Type show or add or exit or edit or complete: ")
    user_action = user_action.strip()


    if 'add' in user_action:
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)
    elif 'show' in user_action:

        todos = functions.get_todos("todos.txt")

        new_todos = []


        new_todos = [item.strip('\n') for item in todos]

        for index,item in enumerate(new_todos):
            #print(index, "-" ,item)
            row = f"{index+1}-{item}"
            print(row)
        print("Total: ",index+1)
        #print(len(todos))
    elif 'edit' in user_action:
        try:
            number = int(user_action[5:])
            print(number)
            number = number-1

            todos = functions.get_todos()

            new_todo  = input("enter new: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("your command is not valid")
            continue


    elif 'complete' in user_action:
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            todos.pop(number-1)

            functions.write_todos(todos)
        except IndexError:
            print("there is no item with that number.")
            continue

    elif 'exit' in user_action:
        break

    else:
        print("command is not valid!")



print("Bye")