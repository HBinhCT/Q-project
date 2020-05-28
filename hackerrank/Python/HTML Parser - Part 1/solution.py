from abc import ABC
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser, ABC):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        self.attr_value(attrs)

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        self.attr_value(attrs)

    @staticmethod
    def attr_value(attrs=None):
        if attrs:
            for attr, val in attrs:
                print('->', attr, '>', val)


if __name__ == '__main__':
    parser = MyHTMLParser()
    for _ in range(int(input())):
        parser.feed(input())
