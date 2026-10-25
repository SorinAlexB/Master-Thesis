import os

from langchain_openai import ChatOpenAI


model = ChatOpenAI(
    model=os.environ["OPENAI_COMPATIBLE_MODEL"],
    base_url=os.environ["OPENAI_COMPATIBLE_BASE_URL"],
    api_key=os.environ["OPENAI_COMPATIBLE_API_KEY"],
)

print(model.invoke("Hello!").content)