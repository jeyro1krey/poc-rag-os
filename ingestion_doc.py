from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader



def ingerer_document(fichier):

    loader = PyPDFLoader("db/temp.pdf")
    pages = loader.load()

    return pages

def ingerer_doc(fichier):

    loader = Docx2txtLoader(fichier)
    pages = loader.load()

    return pages