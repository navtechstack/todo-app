FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read the content of the text file and return it as List"""
    with open(filepath, 'r') as file_read:
        todos_read = file_read.readlines()
    return todos_read


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the content To Do content(first arg) into a text file(second arg)"""
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)


# print(help(get_todos))
# print(help(write_todos))
print(__name__)
if __name__ == '__main__':
    print("Hello")
    # print(get_todos())
