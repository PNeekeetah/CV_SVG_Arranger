from html.parser import HTMLParser

START_TAG = ''
END_TAG = ''
DATA = ''
FILE = open('CV_div_1_new.html','w+') 

def assemble_data_and_print_out():
    global FILE
    string = START_TAG + DATA + END_TAG
    FILE.write(string)


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global START_TAG
        print("Encountered a start tag:", tag, attrs)
        s = '<{}'.format(tag)
        attrs = [f'{attr[0]}="{attr[1]}"' for attr in attrs]
        s += ' ' + ' '.join(attrs) + '>'
        START_TAG = s


    def handle_endtag(self, tag):
        global END_TAG
        print("Encountered an end tag :", tag)
        e = f'</{tag}>'
        END_TAG = e

    def handle_data(self, data):
        global DATA
        DATA = data
        assemble_data_and_print_out()

parser = MyHTMLParser()

with open("CV_div_1.html", 'r') as file:
    parser.feed(file.read())

FILE.close()