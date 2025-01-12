from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

# Dividir o Texto em Chunks.
text = "A inteligência artificial é um campo da ciência da computação que se dedica ao estudo e ao desenvolvimento de máquinas e programas computacionais capazes de reproduzir o comportamento humano na tomada de decisões e na realização de tarefas, desde as mais simples até as mais complexas.  É comumente referida pela sigla IA ou AI (em inglês, artificial intelligence)."
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_text(text)

# Gerar Embeddings.
embeddings_model = OpenAIEmbeddings()
embeddings = [embeddings_model.embed(chunk) for chunk in chunks]

# Inserir Embeddings no FAISS.
import faiss
import numpy as np

dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Configuração do RetrievalQA.
from langchain.retrievers import RetrievalQA

retriever = RetrievalQA(index=index, embeddings_model=embeddings_model)

# Pipeline para Perguntas.
def responder_pergunta(pergunta):
    pergunta_embedding = embeddings_model.embed(pergunta)
    D, I = index.search(np.array([pergunta_embedding]), k=1)
    resposta_chunk = chunks[I[0][0]]
    return resposta_chunk

pergunta = "O Que é Inteligência Artificial"
resposta = responder_pergunta(pergunta)
print(resposta)
