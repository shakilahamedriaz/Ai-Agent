import requests
import fitz  # PyMuPDF
from phidata.app import App
from phidata.infra.storage.file import File
from phidata.infra.storage.lake import Lake
import typer
import io

class PDFassistant:
    def __init__(self, url: str):
        self.url = url
        self.content = self.fetch_pdf(url)
        self.knowledge = self.extract_knowledge()

    def fetch_pdf(self, url: str) -> bytes:
        response = requests.get(url)
        response.raise_for_status()
        return response.content

    def extract_knowledge(self) -> str:
        pdf_document = fitz.open(stream=io.BytesIO(self.content), filetype="pdf")
        text = ""
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
        return text

    def store_knowledge(self, storage: Lake):
        knowledge_file = File(name="knowledge.txt", content=self.knowledge)
        storage.add_file(knowledge_file)

def main(url: str):
    app = App()
    lake = Lake(name="knowledge_lake")
    app.add_lake(lake)

    assistant = PDFassistant(url)
    assistant.store_knowledge(lake)
    print("Knowledge stored successfully.")

if __name__ == "__main__":
    typer.run(main)
