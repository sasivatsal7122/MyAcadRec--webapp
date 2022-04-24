import streamlit as st
import json
from PIL import Image
from streamlit_option_menu import option_menu
import awesome_streamlit as ast
import dashboard
import json
import os


def main():
    filePath ='user_creds/temp_login.json'
    if os.path.exists(filePath):
        os.remove(filePath)
    
    st.title("Welcome to My Academic Record")
    st.markdown("<p><TT>Designed and Developed by <a style='text-decoration:none;color:red' target='_blank' href='https://github.com/sasivatsal7122'>B.Sasi Vatsal</a></TT></p>", unsafe_allow_html=True)
    st.caption("20L31A5413 , Department of AI&DS")
    
    user_option = option_menu(None, ["Sign-In", "Sign-Up"], 
    icons=['box-arrow-in-left', 'box-arrow-in-right'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
    
    
    if user_option=='Sign-Up':
        st.header("Haven't Sign up yet?")
        sign_up_username = st.text_input("Enter your college roll number: ",'20L31A54')
        name = st.text_input("What is your name ?  ")
        sign_up_password = st.text_input("Enter Your Password :  ",type="password")
        user_uploaded_dp = st.file_uploader("Upload you Profile Picture [square pictures are recommended]   (*optional) ")
        create_acc = st.button("Create My Account")
        if create_acc:
            f = open('user_creds/users_cred.json')
            log_in_creds = json.load(f)
            
            ids = len(log_in_creds['Entries'])
    
            new_user_data = {"User name":f"{sign_up_username}",
                        "Password": f"{sign_up_password}",
                        f'{sign_up_username}':f'{name}',
                        "ID": f"{ids + 1}"
                        }

            with open('user_creds/users_cred.json','r+') as file:
                file_data = json.load(file)
                log_in_creds['Entries'].append(new_user_data)
                file_data.update(log_in_creds)
                file.seek(0)
                json.dump(file_data, file, indent = 4)
            if user_uploaded_dp:
                user_uploaded_dp = Image.open(user_uploaded_dp)
                user_uploaded_dp = user_uploaded_dp.resize((200,200),Image.ANTIALIAS)
                user_uploaded_dp.save(f"user_dp/{sign_up_username}.jpg",optimize=True,quality=95)
            st.balloons()
            st.success("Your Account Has been created Successfully...")        
    else:
        st.header("Log In here")
        username = st.text_input("Enter your college roll number: ",'20L31A54',key='login')
        password = st.text_input("Enter Your Password :  ",type="password",key='login')
        log_in_btn = st.button("Log In")
        if log_in_btn:
            f = open('user_creds/users_cred.json')
            log_in_creds = json.load(f)
            for e in log_in_creds['Entries']:
                if username == e['User name']:
                    
                    if password == e['Password']:
                        name = e[username]
                        login_session = {}
                        login_session.update({username:name})
                        with open('user_creds/temp_login.json', 'w') as f:
                            json.dump(login_session, f)
                        st.success("User Authenctication Success..Redirecting to Dashboard..")
                        break
                    else:
                        st.error("Wrong Password...User Authenctication Failed")
                        break
                
                elif int(e['ID'])<len(log_in_creds['Entries']):
                    continue
                else:
                    st.error(f"No User found with user name '{username}', try sign-up")
              
if __name__=="__main__":
    main()