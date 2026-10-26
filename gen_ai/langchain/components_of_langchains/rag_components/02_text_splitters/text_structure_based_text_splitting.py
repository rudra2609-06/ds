from langchain_text_splitters import RecursiveCharacterTextSplitter

# "\n\n"  -> paragraph break (blank line)
# "\n"    -> new line
# ". "    -> sentence end (full stop followed by a space)
# " "     -> space (between words)
# ""      -> single character (last resort)

# it tries to cut the line while not cutting the word in b/w

text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. 


It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software like Aldus PageMaker and Microsoft Word including versions of Lorem Ipsum."""

splitter = RecursiveCharacterTextSplitter(
	separators=['\n\n','\n','.',' ',''],
	chunk_size = 400,
	chunk_overlap = 0
)

chunks = splitter.split_text(text)
# print(len(chunks))
print(chunks[0])