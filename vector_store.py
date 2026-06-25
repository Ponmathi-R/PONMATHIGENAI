from langchain_huggingface import HuggingFaceEmbeddings # pyright: ignore[reportMissingImports]
from langchain_community.vectorstores import FAISS # type: ignore

# A small, free, popular embedding model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("Embedding model is ready!")
 

text = "I love programming in Python."

vector = embeddings.embed_query(text)

print("How many numbers in this vector?", len(vector))
print("First 5 numbers:", vector[:5])

texts = [
    "Python is a programming language.",
    "Streamlit is used to build web apps.",
    "Dogs are friendly animals.",
    "Cats like to sleep a lot."
]

vector_store = FAISS.from_texts(texts, embeddings) # type: ignore

print("All texts are stored in the vector store!")

#save the file
vector_store.save_local("vector_store")

#open the file 
#vector_store = FAISS.load_local("my_store", embeddings, allow_dangerous_deserialization=True)

query = "Tell me about pets"

results = vector_store.similarity_search(query, k=2)   # k=2 means top 2 matches

print("Top matches for:", query)
for r in results:
    print("-", r.page_content)

    