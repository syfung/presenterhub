"""
songsheet
====
Author: Joshua Fung
2019-08-08

We assume the the first block is a data block, all the metadata will be
there, seperated by a newline. Then each song section will be seperated
by a newline, first the tag then a ":" follow by the song. A newline is
nessary, things following the  ":" will be discarded. Chord is indicated
by [], with know chord and unknow chord.

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
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return

    data = []
    for line in f:
        line = line.strip()
        if line == "":
            break
        elif line[0] == "#":
            continue
        data.append(line)
    print("Data: ", data)
    print(Song.new_song(data))

    section = []
    tag = ""
    for line in f:
        line = line.strip()
        if line == "":
            pass
        elif line[0] == "#":
            continue
        elif line.find(":") > 0:
            if len(section) > 0:
                print(tag, ": ", section)
            tag = line.split(":")[0]
            section = []
            continue
        section.append(line)
    if len(section) > 0:
        print(tag, ": ", section)
    f.close()
    return

class Song:
    def __init__(self, title = "", author = ""):
        self.title = title
        self.author = author
        self._transpose = 0
        self._sections = []
        return

    def __str__(self):
        return "Title: " + self.title + " Authour: " + self.author

    """
    factory to create song, given a array of data
    """
    @staticmethod
    def new_song(data):
        no_tag = []
        data_pair = dict()
        for d in data:
            try:
                x, y =  d.split(":")
                data_pair[' '.join(x.strip().capitalize().split())] = ' '.join(y.strip().capitalize().split())
            except ValueError as err:
                no_tag.append(d.strip())

        print(no_tag)
        print(data_pair)
        no_tag.reverse()
        if data_pair.get("Title") == None:
            try:
                data_pair["Title"] = no_tag.pop()
            except IndexError as err:
                print("Missing Title")
                return None
        if data_pair.get("Author") == None:
            try:
                data_pair["Author"] = no_tag.pop()
            except IndexError as err:
                print("Missing Authour")
                return None
        song = Song(data_pair["Title"], data_pair["Author"])
        return song

class SongSection:
    def __init__(self, tag):
        self._tag = tag
        self._slides = []
        return

    def new_slide(self):
        return

    def append_line(self):
        return

class Slide:
    def __init__(self, text):
        self._text = text
        return

if __name__ == '__main__':
    phrase_song_file("test.txt")
    phrase_song_file("test2.txt")
    phrase_song_file("test3.txt")
    print(Song.new_song(["test", "test2", "Test:test", "eSDG  Eewr: sfs     fSDfd    "]))

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
