import streamlit as st
import functions

def add_to_do():
    to_do = st.session_state["new_to_do"]
    to_do_list = functions.get_to_do_list()
    to_do_list.append(to_do + "\n")
    functions.write_to_do_list(to_do_list)
    
to_do_list = functions.get_to_do_list()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This is a todo app by J Hall")

for index, to_do in enumerate(to_do_list):
    checkbox = st.checkbox(to_do, key=to_do)
    if checkbox:
        to_do_list.pop(index)
        functions.write_to_do_list(to_do_list)
        del st.session_state[to_do]
        st.rerun()
    
st.text_input(label="Add new to do item...", label_visibility="hidden", placeholder="Add new to do item...", on_change=add_to_do, key="new_to_do")