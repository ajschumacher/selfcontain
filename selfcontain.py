#!/usr/bin/env python

from lxml import html
import requests
from slimit import minify
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
    scripts = [script for script in tree.findall('.//script')
               if 'src' in script.attrib]
    # TODO:
    # links = tree.findall('.//link')
    # imgs = tree.findall('.//img')
    for script in scripts:
        src = script.attrib['src']
        del(script.attrib['src'])
        script.attrib['type'] = 'text/javascript'
        if src.startswith("//"):
            src = "http:" + src
        # TODO:
        # relative links, file links
        response = requests.get(src)
        # Could go one farther with `mangle_toplevel` too,
        # but this might risk breaking things.
        script.text = minify(response.text, mangle=True)
    return html.tostring(tree)

def main():
    html_string = "".join([line for line in fileinput.input()])
    print selfcontain(html_string)

if __name__ == '__main__':
    main()
