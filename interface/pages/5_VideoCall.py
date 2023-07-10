import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

selected = option_menu(
    menu_title = None,  #"Main Menu",
    options = ['Profile', 'Doctors', 'VideoCall', 'Logout'],
    icons = ['house', 'book', 'book'],
    menu_icon = 'cast',
    default_index=2,
    orientation = "horizontal"
)

if selected == 'Profile':
    switch_page("Profile")
elif selected == 'Doctors':
    switch_page("Doctors")
elif selected == 'Logout':
    switch_page("Home")

st.markdown("# Videocalling")

col1, col2 = st.columns(2)


with col1:
    st.title('Patient')
    picture = st.camera_input("Patient", key=1)

    if picture:
        st.image(picture)
with col2:
    st.title('Doctor')
    picture = st.camera_input("Doctor",key=2)

    if picture:
        st.image(picture)
