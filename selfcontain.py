#!/usr/bin/env python

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
    html_string = ""
    return html_string

def main():
    html_string = "".join([line for line in fileinput.input()])
    print selfcontain(html_string)

if __name__ == '__main__':
    main()
