import pickle
import os
def upload_names_usernames():
    
    names = usernames = None
    path = os.path.dirname(os.path.abspath(__file__)) 
    with open(os.path.join(path ,'names.pkl'), 'rb') as input_file:
        names = pickle.load(input_file)
    with open(os.path.join(path, 'usernames.pkl'), 'rb') as input_file:
        usernames = pickle.load(input_file)

    
    return names, usernames