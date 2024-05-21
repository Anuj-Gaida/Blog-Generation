import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

## function to fetch response from LLaMA 2 model
def getLlamaresponse(input_text, no_words, blog_style):
    ## llama2 model 
    llm = CTransformers(
        model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type='llama',
        config={'max_new_tokens': 256, 'temperature': 0.01}
    )
    ## prompt template
    template = """
    Write a blog for {style} job profile for the topic {text} within {n_words} words.
    """
    prompt = PromptTemplate(
        input_variables=['style', 'text', 'n_words'],
        template=template
    )

    ## generate the response from the llama 2 model
    response = llm.invoke(prompt.format(style=blog_style, text=input_text, n_words=no_words))
    print(response)
    return response

st.set_page_config(
    page_title="Blog Lekham",
    page_icon=':bear:',
    layout='centered',
    initial_sidebar_state='collapsed'
)
st.header("Blog Lekham :bear:")

input_text = st.text_input("Enter the Blog Topic")

# creating 2 columns for additional 2 fields
col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.text_input("No of Words")
with col2:
    blog_style = st.selectbox("Writing the blog for", ('Researcher', 'Data scientist', 'Common man'), index=0)

submit = st.button("Lekhdim")

# final response
if submit:
    if not input_text or not no_words:
        st.error("Please fill in all fields")
    else:
        try:
            no_words = int(no_words)  # Ensure no_words is an integer
            st.write(getLlamaresponse(input_text, no_words, blog_style))
        except ValueError:
            st.error("No of Words must be a valid number")
