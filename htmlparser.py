from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("encountered a start tag:", tag)
        if(tag == "h2"):
            for name, val in attrs:
                if("secret_flag" in val):
                    print(name)
                    #here I need to check the data since its a flag

        #for attr in attrs:
        #    if "" in attr:
        #        print("     attr:", attr)    

    def handle_endtag(self, tag):
        print("encountered an end tag:", tag )


    def handle_data(self, data):
        if("FLAG" in data):
            print(data)

parser = MyHTMLParser()
parser.feed('<h2 class=secret_flag style="color:red">FLAG: 64-characters-of-random-alphanumerics</h2>')

#goal:
#data one massive string, look for hrefs
string1 = ("""Response: HTTP/1.1 200 OK\r\nDate: Wed, 16 Nov 2022 11:25:45 GMT\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: 1984\r\nConnection: close\r\nServer: gunicorn\r\nVary: Accept-Language, Cookie, Accept-Encoding\r\nContent-Language: en-us\r\n\r\n""")

test = string1.split('\r\n')
for i in test:
    if("Content-Length:" in i):
        print(i[16: len(i)])
        print(len(i))




#print (test)
