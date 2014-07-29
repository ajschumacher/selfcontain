#!/usr/bin/env python

from lxml import html
import fileinput

def selfcontain(html_string):
    """Make HTML self-contained

    Take an HTML string and return an HTML string with external
    dependencies as much as possible removed.

    Parameter:
    html_string : str, required
        HTML text, possibly with links to JavaScript, CSS, and images
        that would require HTTP calls for rendering
    """
    tree = html.fromstring(html_string)
    scripts = tree.findall('.//script')
    links = tree.findall('.//link')
    imgs = tree.findall('.//img')
    return html.tostring(tree)

def main():
    html_string = "".join([line for line in fileinput.input()])
    print selfcontain(html_string)

if __name__ == '__main__':
    main()
