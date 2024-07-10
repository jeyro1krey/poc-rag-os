### première partie : ajout des données
from langchain_community.vectorstores.chroma import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import TokenTextSplitter, NLTKTextSplitter, SpacyTextSplitter

from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings



model = "sentence-transformers/distiluse-base-multilingual-cased-v2"
embedding_function = HuggingFaceEmbeddings()
embedding_function.model_name = model

model_spacy = "fr_core_news_lg"
nom_db = 'db/test_premier'

def portion_doc(pages, model_spacy):

    text_split = SpacyTextSplitter(separator='\n\n\t\t', pipeline=model_spacy, chunk_size=500, chunk_overlap=50)
    chunks = text_split.split_documents(pages)

    return chunks


def ecrire_db(chunks, nom_db):

    db = Chroma.from_documents(documents=chunks, embedding=embedding_function, persist_directory=nom_db)
    print('done')
    return db
