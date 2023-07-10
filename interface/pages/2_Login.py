import streamlit as st
import streamlit_authenticator as stauth

from PIL import Image
from utils.nav import *
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
import os
from security.utils import upload_names_usernames
from pathlib import Path

names, usernames = upload_names_usernames()

hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

import yaml
from yaml.loader import SafeLoader

path_temporal = Path(__file__).parent

with open(os.path.join(path_temporal, '..', 'security','config.yaml')) as file:
    config = yaml.load(file, Loader=SafeLoader)
for username, hashed_password in zip(config['credentials']['usernames'].keys(), hashed_passwords):
    config['credentials']['usernames'][username]['password'] = hashed_password

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

selected = option_menu(
    menu_title = None,  #"Main Menu",
    options = ['Home', 'Registration', 'Login'],
    icons = ['house', 'book', 'book'],
    menu_icon = 'cast',
    default_index=2,
    orientation = "horizontal"
)


if selected == 'Home':
    switch_page("Home")
elif selected == 'Registration':
    switch_page("Registration")

name, authentication_status, username = authenticator.login("Login", "main")

if len(username) > 0:
    if authentication_status:
        st.session_state['name'] = name
        switch_page("Profile")
    
    elif authentication_status is False:
        st.error('Username/password is incorrect')
        
    elif authentication_status is None:
        st.warning('Please enter your username and password')