"""Phrase txt into document and generate pdf/html

Create document form a plain text file. Eventully the songsheet module
should be only for mechanism to generate pdf/html rather than handling
all the document/slide/section class.

The expected input text format, which is influnced by python syntax:
Title: Title
Author: Author
Data Tag: Data
...

Section 1:
    Song slide 1 line 1
    Song slide 1 line 2

    Song slide 2 line 1
    Song slide 2 line 2

Section 2:
    Song slide 1 line 1
    Song slide 1 line 2
    ...

class:
    Document : container to any sectoin and slides
    Section : a section of slides
    Slide : single slide

Author: Joshua Fung
2019-08-08
"""


class Document:
    """
    A class use to represent document have a filename and title, and
    potentially other data. Store slides by storing a list of sections.

    Attributes:
        filename (str): filename of the document
        location (str): location of the document exclude filename
        title (str): title of the document
        info (dict): a dictionary on other attributes
        section (list): a list of sections
    """

    def __init__(self, filename, title="", location=""):
        """
        Parameters:
            filename (str): filename to save document exclude sufix
            title (str, optional): title of the document (default "")
            location (str, optional): location to save (default "")
        Raises:
        Returns:
        """
        self.filename = filename
        self.title = title
        self.location = location
        self.info = dict()
        self.sections = []
        return


class Section:
    """
    A class that contains section of slides, which defines the defaule
    formatting, quick key, or pdf/html generate attributes.

    Attributes:
        tag (str, optional): tag of a section (default "")
        slides (list): a list of slides
    """

    def __init__(self, tag=""):
        self.tag = tag
        self.slides = []
        return


class Slide:
    """
    A class to represent a single slide
    For now a slide is expected to store only a single text element.
    """

    def __init__(self):
        self.elements = []
        return


class Element:

    def __init__(self):
        return


class TextElement(Element):

    def __init__(self):
        self.supuer()
        self.text = ""
        return

if __name__ == "__main__":
    Song.new_song()
