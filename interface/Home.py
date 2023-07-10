import yaml
from yaml.loader import SafeLoader
import streamlit as st 
import streamlit_authenticator as stauth  
from streamlit_chat import message
from streamlit_option_menu import option_menu
from PIL import Image
from security.params import *
from utils.nav import *
import sys
from streamlit_extras.switch_page_button import switch_page
import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
from utils.predict_image_classification_sample import predict_image_classification_sample

import io

path = os.path.dirname(os.path.abspath(__file__)) 
sys.path.append(path)

ico_website = Image.open(open("img/skin_icon.ico", "rb"))
avatar1 = Image.open(open("img/skin_icon.png", "rb"))

st.set_page_config(
    page_title="Vitality Squad - Skincare", 
    page_icon=ico_website, 
    layout="wide", 
    initial_sidebar_state="collapsed"
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
    default_index=0,
    orientation = "horizontal"
)

if selected == 'Registration':
    switch_page("Registration")
elif selected == 'Login':
    switch_page("Login")

@st.cache_resource
def get_chat():
    vertexai.init(project="cosmic-abbey-392222", location="us-central1")
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    
    chat = chat_model.start_chat()
    return chat

if 'message' not in st.session_state:
    st.session_state['message'] = []
    st.session_state['message'].append(('Hello how could I help you', False))

message_history = st.session_state['message'] 



chat = get_chat()
parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }


columns = st.columns(2)
predictions = None
if "predictions" in st.session_state:
    predictions = st.session_state["predictions"]

with columns[0]:
    st.markdown("## Upload an Image here")
    uploaded_file = st.file_uploader("Upload an image", key="image")
    bytes_data = None
    bounding_image = None
    decoded = None

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        decoded = Image.open(io.BytesIO(bytes_data))
        #rgb_im = decoded.convert('RGB')
        newsize = (256, 256)
        decoded = decoded.resize(newsize)
        decoded.save("skin_disease.jpg")

        buf = io.BytesIO()
        decoded.save(buf, format='JPEG')
        bytes_data = buf.getvalue()
        bounding_image = decoded.copy()

        st.image(decoded, caption="Patient's photo")
        
        predictions = predict_image_classification_sample(
                #project="proyectocloud-352601",
                project="cosmic-abbey-392222",
                #endpoint_id="4080467970583691264",
                endpoint_id="2431728294501023744",
                location="us-central1",
                filename="skin_disease.jpg"
            )  
        for prediction in predictions:
                st.session_state["predictions"] = dict(prediction)
                # st.text(pred['displayNames'][0])
                # st.text(pred['confidences'][0])
        
set_messages = set([message_only[0] for message_only in message_history])
with columns[1]:
    placeholder = st.empty()
    input_ = st.text_input("you:", key='text')
    if input_ and input_ not in set_messages:
        message_history.append((input_, True))
        print("LEN", len(message_history))
        if len(message_history) == 7:
            pred = st.session_state["predictions"] 
            # st.text(pred['confidences'][0])
            message_history.append((f"You may have a problem of {pred['displayNames'][0]}. I am {round(pred['confidences'][0] * 100,2)}% sure.", False))
        else:
            response = chat.send_message(
            input_, **parameters
            )
            message_history.append((response.text, False))
        
        if len(message_history) == 5:
            message_history.append(("Could you upload an image? Do you have the option with a control on the left.", False))
        



    with placeholder.container():
        for idx, (message_, is_user) in enumerate(message_history): 
            message(message_, is_user, key=str(idx))


hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

with open('security/config.yaml') as file:
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
