import streamlit as st
import streamlit_authenticator as stauth

from PIL import Image
from utils.nav import *
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

import os
# --- USER AUTHENTICATION ---
names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]

hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

import yaml
from yaml.loader import SafeLoader

path_temporal = os.path.dirname(os.path.abspath(__file__)) 
with open(os.path.join(path_temporal, '..','/security/config.yaml') as file:
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
    default_index=1,
    orientation = "horizontal"
)


if selected == 'Home':
    switch_page("Home")
elif selected == 'Login':
    switch_page("Login")    

try:
    if authenticator.register_user('Register user', preauthorization=False):
        with open('../config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
        st.success('User registered successfully')
        switch_page("Login")
except Exception as e:
    st.error(e)