#!/usr/bin/env python

from lxml import html
import requests
from slimit import minify
import fileinput

def _fetch(ref):
    """
    Return the string referenced by a link.

    TODO:                     
    relative links, file links
    """
    if ref.startswith("//"):
        ref = "http:" + ref
    response = requests.get(ref)
    return response.text

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
    for script in scripts:
        src = script.attrib['src']
        del(script.attrib['src'])
        script.attrib['type'] = 'text/javascript'
        contents = _fetch(src)
        # Could go one farther with `mangle_toplevel` too,
        # but this might risk breaking things.
        script.text = minify(contents, mangle=True)
    links = [link for link in tree.findall('.//link')
             if 'href' in link.attrib]
    for link in links:
        href = link.attrib['href']
        for key in link.attrib:
            del(link.attrib[key])
        link.tag = 'style'
        contents = _fetch(href)
        link.text = contents
    # TODO:
    # imgs = tree.findall('.//img')
    return html.tostring(tree)

def main():
    string = "".join([line for line in fileinput.input()])
    # Allow a URL to be passed and fetched
    if string.startswith("http"):
        string = _fetch(string.strip())
    print selfcontain(string)

if __name__ == '__main__':
    main()
