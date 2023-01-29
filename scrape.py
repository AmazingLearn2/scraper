"""
env vars:
URL url to parse
USER
PASS
"""
# Import libraries
import os
import re
import requests
from bs4 import BeautifulSoup
import base64
import dotenv

dotenv.load_dotenv('.env')

# authorization
credentials = base64.b64encode(f"{os.environ.get('USER')}:{os.environ.get('PASS')}".encode('ascii'))
print(credentials)
headers = {
        'Authorization': f"Basic {credentials}",
        }

total = 0

def scrape(url, depth):
    global total

    # Requests URL and get response object
    response = requests.get(url, headers=headers)

    # Parse text obtained
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all hyperlinks present on webpage
    links = soup.find_all('a')

    # From all links check for pdf link and
    # if present download file
    for link in links:
        href = str(link.get('href', []))

        regex_dir = re.compile(r"^([^\/]+)\/$")
        match_dir = regex_dir.search(href)

        if ('.pdf' in href):
            total += 1
            indent = "  " * depth
            print(f"{indent} downloading {url}{href}")

            # Get response object for link
            response = requests.get(f"{url}{href}", headers=headers)

            # Write content in pdf file
            pdf = open("pdfs/pdf"+str(total)+".pdf", 'wb')
            pdf.write(response.content)
            pdf.close()
            print("File ", total, " downloaded")

        elif match_dir:
            child_dir = f"{url}{match_dir.group(1)}/"
            scrape(child_dir, depth+1)

scrape(os.environ.get('URL'), 0)

print(f"{total} PDF files downloaded to dir pdfs/")