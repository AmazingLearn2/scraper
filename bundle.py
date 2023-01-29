# importing required modules
from PyPDF2 import PdfReader
import io
from PIL import Image
import pytesseract
from wand.image import Image as wi
from pathlib import Path

def normalize_text(s: str) -> str:
    return s.replace('\n', ' ')

def get_text_from_image(pdf_path):
    pdf=wi(filename=pdf_path,resolution=300)
    pdfImg=pdf.convert('jpeg')
    imgBlobs=[]
    extracted_text=[]
    for img in pdfImg.sequence:
        page=wi(image=img)
        imgBlobs.append(page.make_blob('jpeg'))

    for imgBlob in imgBlobs:
        im=Image.open(io.BytesIO(imgBlob))
        text=pytesseract.image_to_string(im,lang='deu')
        extracted_text.append(text)

    return (extracted_text)

with open(Path('bundled.txt'), 'a+') as out_file:

    for path in Path('pdfs').rglob('*.pdf'):
        print(path.name)

        # creating a pdf reader object
        reader = PdfReader(path)
        
        # printing number of pages in pdf file
        print(len(reader.pages))
        
        # getting a specific page from the pdf file
        for page in reader.pages:

            # extracting text from page
            text = page.extract_text()

            if not text:
                print(f"img extract {path.name}")
                text = get_text_from_image(path)
                print(f"extracted:\n{text}")

            # write to out_file
            out_file.write(normalize_text(text))
