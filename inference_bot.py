
from langchain_community.vectorstores.chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings



model = "mixedbread-i/mxbai-embed-large-v1"
embedding_function = HuggingFaceEmbeddings()
embedding_function.model_name = model

nom_db = 'db/test_premier'


from appel_phi import ask_phi



# connexion db

#db = Chroma(persist_directory=persist_directory, embedding_function=embedding_function)

def repondre_question(question):
    
    db = Chroma(persist_directory=nom_db, embedding_function=embedding_function)
    test_similarity = db.similarity_search_with_score(question)

    text_all = ""
    source_all = ""

    for i in test_similarity:
        text_synth = i[0].page_content
        text_all = text_all + text_synth


    ### appel LLM

    #reponse = 'ici, on répond à la question'

    reponse = ask_phi(question, text_all)
    print('reponse', reponse)

    return reponse