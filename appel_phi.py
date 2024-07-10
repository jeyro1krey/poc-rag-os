import ollama

from langchain_community.vectorstores.chroma import Chroma


from langchain_community.embeddings import HuggingFaceEmbeddings



model = "mixedbread-i/mxbai-embed-large-v1"
embedding_function = HuggingFaceEmbeddings()
embedding_function.model_name = model


nom_db = 'db/test_premier'



def ask_phi(question, text_all):

    
    output = ollama.generate(
        model="phi3",
        prompt=f"En utilisant seulement ces données: {text_all}, réponds à cette question : {question}"
    )

    plouf = output['response']

    return plouf