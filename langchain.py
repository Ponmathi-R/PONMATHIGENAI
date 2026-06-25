import os
import streamlit as st # type: ignore
from dotenv import load_dotenv # type: ignore
from langchain_openai import ChatOpenAI # type: ignore
from langchain_core.messages import HumanMessage # type: ignore

load_dotenv()

st.set_page_config(page_title="LangChain + OpenAI + LangSmith", page_icon="🤖")

st.title("🤖 LangChain OpenAI App")
st.write("Send a prompt to an OpenAI chat model using LangChain. Runs are traced in LangSmith.")

required_keys = {
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
    "LANGSMITH_API_KEY": os.getenv("LANGSMITH_API_KEY"),
}

missing_keys = [key for key, value in required_keys.items() if not value]

if missing_keys:
    st.error(f"Missing environment variable(s): {', '.join(missing_keys)}")
    st.stop()

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = os.getenv(
    "LANGSMITH_PROJECT", "langchain-streamlit-demo"
)

prompt = st.text_area("Enter your prompt:", "Explain LangChain in simple words.")

if st.button("Send to Model"):
    try:
        with st.spinner("Getting response..."):
            model = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0.7
            )

            response = model.invoke([
                HumanMessage(content=prompt)
            ])

        st.subheader("Model Response")
        st.success(response.content)

        print("User Input:", prompt)
        print("Model Output:", response.content)

        st.info("Run completed. Check your LangSmith dashboard.")

    except Exception as e:
        st.error(f"Error: {e}")