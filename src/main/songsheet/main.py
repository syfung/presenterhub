"""
from reportlab.lib.pagesizes import letter, A4
myCanvas = Canvas('myfile.pdf', pagesize=letter)

width, height = letter  #keep for laterfrom reportlab.pdfgen import canvas
def hello(c):
    c.drawString(100,100,"Hello World")
c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()
"""

"""
We assume the the first block is a data block, all the metadata will be
there, seperated by a newline. Then each song section will be seperated
by a newline, first the tag then a ":" follow by the song. A newline is
not nessary, but encouraged. Chord is indicated by [], with know chord/
unknow chord.

Title
Author
Data Tag: Data
...

Section 1:
Song slide 1 line 1
Song slide 1 line 2
...

Song slide 2 line 1
Song slide 2 line 2

Section 2:
Song slide 1 line 1
Song slide 1 line 2
...

"""
def phrase_song_file(file_name):
    try:
        f = open(file_name, "r")
    except:
        raise
    title = f.readline()
    author = f.readline()
    return

class Song:
    def __init__(self, title = "", author = ""):
        self._title = title
        self._author = author
        self._transpose = 0
        self._sections = []
        return

class SongSection:
    def __init__(self, tag):
        self._tag = tag
        self._slides = []
        return

class Slide:
    def __init__(self, text):
        self._text = text
        return

if __name__ == '__main__':
    pass
