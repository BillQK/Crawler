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
#parser.feed('<html><head><title>Test</title></head>'
#            '<body><input type ="hidden" name = crsfmiddlewaretoken" value = dlkafjadkljfl><input type = "submit" value="Log in"></body></html>')

teststring = "Date: Fri 11 Nov 2022 Content-Type: text/html klafjadkldj Set-Cookie: csrftoken=dja2642632klfjakldsjfklas sessionid=dkalfjadkljflka"
testlist = teststring.split()
for i in testlist:
    if "csrftoken" in i or "sessionid" in i:
        print(i)       
#pattern = re.compile(r'csrftoken=.*')


#pattern2 = re.compile(r'sessionid=.+')
#matches = re.findall(pattern, testlist)
#print(matches)
