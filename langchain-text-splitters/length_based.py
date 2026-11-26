from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0, ## overlap characters, if chunk size=100 then chunk_overlap=10-20 will be better.
    separator=''
)

result = splitter.split_documents(docs)

print(result[1].page_content)