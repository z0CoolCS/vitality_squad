import streamlit as st
from streamlit_image_select import image_select
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page


selected = option_menu(
    menu_title = None,  #"Main Menu",
    options = ['Profile', 'Doctors', 'VideoCall', 'Logout'],
    icons = ['house', 'book', 'book'],
    menu_icon = 'cast',
    default_index=1,
    orientation = "horizontal"
)

if selected == 'Profile':
    switch_page("Profile")
elif selected == 'VideoCall':
    switch_page("VideoCall")
elif selected == 'Logout':
    switch_page("Home")


st.markdown("# Doctors")

imageUrls = [
"https://media.gettyimages.com/id/1352251596/es/foto/m%C3%A9dico-al-frente-de-un-grupo-de-trabajadores-sanitarios-del-hospital.jpg?s=612x612&w=0&k=20&c=GzyiH2FqAJzzoLmxcPc90eYpHH0i6o68ggkKqgFTA8g=",
"https://media.gettyimages.com/id/1307155498/es/foto/smiling-male-doctor-against-gray-background.jpg?s=612x612&w=0&k=20&c=ur7yUkS4ys75Z7ak8ik4seOppCUd4A5kV7nV9oToYWM=",
"https://media.gettyimages.com/id/1139666077/es/foto/doctor-wearing-eyeglasses-on-white-background.jpg?s=612x612&w=0&k=20&c=TOqTntX3Qm-Kecp2zwnosQK2UNDBdbH9egtOvxGPiaQ=",
"https://media.gettyimages.com/id/1400102237/es/foto/african-american-female-doctor-with-arms-crossed-over-white-background.jpg?s=612x612&w=0&k=20&c=EYVFeii8q3WP1Ht0cFd7LQOnCqM8VLkcp6aDA0-Qy2M=",
"https://media.gettyimages.com/id/1342708859/es/foto/retrato-de-un-m%C3%A9dico-var%C3%B3n.jpg?s=612x612&w=0&k=20&c=P3HojVFHOcdCqYTLyvDvFJ1rIWqVtUfiljuwp5T_dho=",
"https://media.gettyimages.com/id/1326131977/es/foto/female-doctor-discussing-while-sitting-at-desk.jpg?s=612x612&w=0&k=20&c=WsaB5xwHX_wJajJNxrYqVFBMQAGVV_Fj1ipeKY2SGis=",
]

doctors_info = [
    { "name":"Dr. John Smith", "age":"40","licence":"12345"},
    { "name":"Dr. Jaime Johnson", "age":"55","licence":"67890"},
    { "name":"Dr. Michael Brown", "age":"45","licence":"24680"},
    { "name":"Dr. Emily Davis", "age":"32","licence":"13579"},
    { "name":"Dr. James Wilson", "age":"50","licence":"75309"},
    { "name":"Dr. Jessica Lee", "age":"38","licence":"86420"},
]

img = image_select("Choose one doctor:", imageUrls)

if img is not None:
    col1, col2 = st.columns(2)
    with col1:
        st.image(img)
    with col2:
        idx =  imageUrls.index(img)
        name_doc =doctors_info[idx]['name']
        age_doc =doctors_info[idx]['age']
        lic_doc =doctors_info[idx]['licence']
        st.text(f"Name: {name_doc}")
        st.text(f"Age: {age_doc}")
        st.text(f"Licence: {lic_doc}")

        btn_appoint = st.button("Book a appointment")

        if btn_appoint:
            st.success('This is a success message!', icon="✅")

 