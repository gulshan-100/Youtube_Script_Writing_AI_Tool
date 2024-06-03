import streamlit as st                    
from utils import generate_script         
 
if 'API_KEY' not in st.session_state:
    st.session_state['API_KEY'] = ""

st.title("Youtube Script Writing AI Tool")

#Sidebar content
st.sidebar.title("*")
st.session_state['API_KEY'] = st.sidebar.text_input("What's your API key", type = 'password')

#User input content 
prompt = st.text_input('Please provide the topic of the video')
video_length = st.text_input("Expected video length (in minutes)")
creativity = st.slider('Creativity limit', 0.0, 1.0, 0.2, step =0.1)

submit = st.button("Generate script for me")

if submit:
    if st.session_state['API_KEY']:
        search_result, title, script = generate_script(prompt, video_length, creativity, st.session_state['API_KEY'])
        st.success("Hope you like this script")
        
        #Display the title 
        st.subeader("Title:")
        st.write(title)
        
        #Display the script 
        st.subheader('Script:')
        st.write(script)
        
        #Display search result
        st.subheader("Check out: DuckDuckGo Search")
        with st.expander('Show me'):
            st.info(search_result)
    else:
        st.error("Oops!! Please provide the API key.....")