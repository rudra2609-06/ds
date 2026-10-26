from langchain_text_splitters import CharacterTextSplitter


# chunk_overlap is the number of characters (or tokens, depending on the splitter’s length function) that repeat at the end of one chunk and the start of the next. Its job is to keep context from being lost at the boundaries where the text is cut.

"""
chunk_overlap=0:   [AAAAAAAA][BBBBBBBB][CCCCCCCC]
chunk_overlap=3:   [AAAAAAAA]
                        [AAABBBBB]      <- starts with the last 3 of the previous chunk
                              [BBBCCCCC]
"""
# disadvantage of increasing is that it creates more chunks
# for rag based app 10-20% is good percentage. For 100 chunk size 10 or 20

splitter = CharacterTextSplitter(
	chunk_size=100,
	chunk_overlap=0,
	separator='',
)

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software like Aldus PageMaker and Microsoft Word including versions of Lorem Ipsum."

res = splitter.split_text(text)
print(res[0])