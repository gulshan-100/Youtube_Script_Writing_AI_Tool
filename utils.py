from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.tools import DuckDuckGoSearchRun

import os 
os.environ['GOOGLE_API_KEY'] = "api_key"

def generate_script(prompt, video_length, creativity, api_key):
    
    title_template = PromptTemplate(
        input_variables=['subject'],
        template = 'Please come up with the title for youtube video'
    )
    
    script_template = PromptTemplate(
        input_variables=['title', 'DuckDuckGo_Search', 'duration'],
        template = 'Create a script for a youtube video based on this title for me. TITLE: {title} of duration: {duration} minutes using this search data {DuckDuckGo_Search}'
    )
    
    llm = ChatGoogleGenerativeAI(temperature= creativity, model = 'gemini-pro')
    
    title_chain = LLMChain(llm = llm, prompt = title_template, verbose = True)
    script_chain = LLMChain(llm = llm, prompt = script_template, verbose = True)
    
    search = DuckDuckGoSearchRun()
    
    title = title_chain.invoke(prompt)
    
    search_result = search.run(prompt)
    
    script = script_chain.run(title, DuckDuckGoSearchRun = search_result, duration = video_length)
    
    return search_result, title, script
    
    