import streamlit as st
import streamlit_authenticator as stauth

from PIL import Image
from utils.nav import *
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from security.utils import upload_names_usernames
from pathlib import Path
import os
names, usernames = upload_names_usernames()

hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

import yaml
from yaml.loader import SafeLoader

path_temporal = Path(__file__).parent
print(os.listdir(path_temporal))
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


selected = option_menu(
    menu_title = None,  #"Main Menu",
    options = ['Profile', 'Doctors', 'VideoCall', 'Logout'],
    icons = ['house', 'book', 'book'],
    menu_icon = 'cast',
    default_index=0,
    orientation = "horizontal"
)

name = st.session_state['name']
#authenticator.logout('Logout', 'main', key='unique_key')
st.markdown(f'# Welcome **{name}**')

col1, col2, col3, col4 = st.columns(4)
col1.markdown("## First name")
col1.markdown(f"### {name} Perez")

col2.markdown("## Address")
col2.markdown(f"### EEUU")

col3.markdown("## Age")
col3.markdown(f"### 78")

#Image.open
col4.image('img/jsmith.jpg', width=400)
#col2.metric("FTEC", "$121.10", "0.46%")
#col3.metric("BTC", "$46,583.91", "+4.87%")



st.markdown("## Dermathologic history")

appointments = ["Appointment 23/04/2022", "Appointment 10/03/2022", "Appointment 03/08/2021"]
doctors = ["Ivan Gonzalez", "Esteban Rodriguez", "Mike Torres"]

for ap, doc in zip (appointments, doctors):
    expander = st.expander(ap)
    expander.text(f"Doctor: {doc}")


# st.title('Some content')
# picture = st.camera_input("Take a picture")

# if picture:
#     st.image(picture)

if selected == 'Doctors':
    switch_page("Doctors")
elif selected == 'VideoCall':
    switch_page("VideoCall")
elif selected == 'Logout':
    switch_page("Home")
