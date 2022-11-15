from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("encountered a start tag:", tag)
        for attr in attrs:
            if "name" in attr:
                print("     attr:", attr)    

    def handle_endtag(self, tag):
        print("encountered an end tag:", tag )


    def handle_data(self, data):
        print("encountered data :" , data)

parser = MyHTMLParser()
parser.feed('<li><a href="/fakebook/9991121/">Edmundo Gresl</a></li>')