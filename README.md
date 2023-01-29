# HGB Scraper

## Setup (MacOS)

Requirement: homebrew

```
# install tesseract:

brew install tesseract
brew install tesseract-lang

# install ImageMagick:

brew install freetype imagemagick

# install python virtual environment
python -m venv venv

# activate virtual environment
source venv/bin/activate

pip install -r requirements.txt
```

## Run

activate virtual environment...

```
export URL=http://example.com/pdfs/
export USER=user
export PASS=password

python scrape.py

python bundle.py
```