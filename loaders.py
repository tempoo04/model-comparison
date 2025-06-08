# WebBaseLoader
# from langchain_community.document_loaders import WebBaseLoader
#
# target_url = "https://isha.sadhguru.org/en/wisdom/article/artificial-intelligence-growth-mean-humanity?gad_source=1&gad_campaignid=22619522147&gbraid=0AAAAADh2_dLcjdMuN9VFO6CTunXrvRkOW&gclid=CjwKCAjw6ZTCBhBOEiwAqfwJd_tw9G8kTRftya4DTbZ_a6BXNdUpMiy8elf1OttunP8ND5GZY_AJqBoCTq8QAvD_BwE"
# loader = WebBaseLoader(target_url)
# raw_documents = loader.load()
#
# with open("URL_Content.txt", "w") as file:
#     file.write(raw_documents[0].page_content)
#
# print("Done.")
# print(raw_documents[0].metadata)


#PyPDFLoader
# from langchain_community.document_loaders import PyPDFLoader
#
# filepath = "./data/timeline.pdf"
# loader = PyPDFLoader(filepath)
# pages = loader.load()
#
# print(pages[39].page_content, pages[39].metadata)
#
# filepath = "./data/digital.pdf"
# loader = PyPDFLoader(filepath, extract_images=True)
# pages = loader.load()
# print(pages[6].page_content)

#UnstructuredExcelLoader
from langchain_community.document_loaders import UnstructuredExcelLoader

file_path = "./data/ai_course.xlsx"
loader = UnstructuredExcelLoader(file_path, mode="elements")
docs = loader.load()

excel_content = docs[0].metadata["text_as_html"]

with open("excel.html", "w", encoding="utf-8") as f:
    f.write(excel_content)










