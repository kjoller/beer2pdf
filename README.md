# Beer2PDF

This is a tool to create nicely formatted pdf files from
BeerXML-recipes. The first goal is to make an A6-sized
(105mm x 148mm) sheet for a small brew journal

## Installation

Since this currently uses a customised PyBeerXML, it is
best to install it using a virtual environment. In the 
future, it should probably be made into a PyPI package

```sh
git clone https://github.com/kjoller/beer2pdf.git
cd beer2pdf
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

With the virtual environment activated, it is run like this:

```sh
./beer2pdf -t <template> <recipe.xml> <outputfile.pdf>
```

