import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="JinLim | Generative AI 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**GitHub:**",
"[yvann-hub/Robby-chatbot](https://github.com/yvann-hub/Robby-chatbot)")

    st.write("**Instagram:** [@foojinny__](https://instgram.com/foojinny__)")
    st.write("**Mail** : 1997foo@gmail.com")
    st.write("**Created by Jinny**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>JinLim, your data-aware assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm JinLim, an intelligent chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive interactions. My goal is to help you better understand your data.
    I support PDF, TXT, CSV transcript 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Jinny's Pages
st.subheader("🚀 JinLim's Pages")
st.write("""
- **Jinny-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **Jinny-Sheet** (beta): Chat on tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation
""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""
**JinLim is under regular development. Feel free to contribute and help me make it even more data-aware!**
""", unsafe_allow_html=True)





