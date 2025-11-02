from langgraph.graph import StateGraph,START,END
from langchain_groq import ChatGroq
from typing import TypedDict, Annotated,Literal
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import operator
import os

load_dotenv ()
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY") ,
    model="llama-3.3-70b-versatile"
)

class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage],add_messages]

    
def chat_node(state: ChatState):

    #take user query from state
    messages=state['messages']
    #send to llm
    response=llm.invoke(messages)
    #response store state
    return {'messages': [response]}

checkpointer=MemorySaver()
graph=StateGraph(ChatState)

graph.add_node('chat_node',chat_node)
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot=graph.compile(checkpointer=checkpointer)

# thread_id='1'

# while True:

#     user_message=input('Type here:')

#     print('user:',user_message)

#     if user_message.strip().lower() in ['exit','quit','bye']:
#         break

#     config={'configurable':{'thread_id':thread_id}}

#     response=workflow.invoke({'messages':[HumanMessage(content=user_message)]},config=config)

#     print('AI:',response['messages'][-1].content)