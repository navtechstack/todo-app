import streamlit as st

from modules import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)


st.title('Welcome to my To Do App')
st.subheader('This Subheader')
st.write('Just simply writing')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
        
st.text_input(label='', placeholder='Add a new To Do', on_change=add_todo,
              key='new_todo')
st.session_state
