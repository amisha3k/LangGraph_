# import streamlit as st
# from backend import chatbot
# from langchain_core.messages import BaseMessage,HumanMessage

# CONFIG={'configurable':{'thread_id':'thread-1'}}

# if 'message_history' not in st.session_state:
#     st.session_state['message_history']=[]

# #loading the conversation history
# for message in st.session_state['message_history'] :
#     with st.chat_message(message['role']):
#         st.text(message['content'])


# user_input=st.chat_input('Type_here')

# if user_input:
    
#     st.session_state['message_history'].append({'role':'user','content':user_input})
#     with st.chat_message('user'):
#         st.text(user_input)

#     response=chatbot.invoke({'messages':[HumanMessage(content=user_input)]},config=CONFIG)
#     ai_message=response['messages'][-1].content
#     st.session_state['message_history'].append({'role':'assistant','content':ai_message})
#     with st.chat_message('assistant'):
#         st.text(ai_message)    

import streamlit as st
from backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

# Initialize message history
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Display conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# Get user input
user_input = st.chat_input('Type your message here...')

if user_input:
    # Add user message
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # Invoke chatbot
    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)

    # Handle different response formats
    ai_message = response['messages'][-1].content if isinstance(response, dict) else response.content

    # Add AI message
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)
