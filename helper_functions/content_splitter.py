from langchain.text_splitter import RecursiveCharacterTextSplitter

with open("content.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=250, 
    chunk_overlap=35 
)

chunks = splitter.split_text(raw_text)
content_in_chunks = [chunk for chunk in chunks]
