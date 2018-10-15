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

A working installation of Inkscape is also required, although
a later version should implement using something more portable.

## Usage

With the virtual environment activated, it is run like this:

```sh
./beer2pdf -t <template> <recipe.xml> <outputfile.pdf>
```

## A6 overview template

This templates uses the "Carlito" and "Bitstream Charter" fonts. The Bitstream
Charter font seems to be standard on Ubuntu. If not already present, the
carlito font is installable (in Ubuntu 18.04) with:

```
apt install fonts-crosextra-carlito
```

