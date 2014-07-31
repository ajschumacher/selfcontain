#!/usr/bin/env python

from urlparse import urljoin
import os.path
from lxml import html
import requests
from slimit import minify
from rcssmin import cssmin
from base64 import b64encode
import sys

def _read_file(filename):
    """Return a string, for a filename"""
    with open(filename) as f:
        return f.read()

def _pathjoin(base, ref):
    return os.path.join(os.path.dirname(base), ref)

def _fetch(ref, base="", content_type="text"):
    """Return the thing referenced by a URL or filepath.

    Parameters:
    base : String; the original URL or filepath

    content_type : Default "text" returns unicode,
                   "binary" returns (binary) string
    """
    if content_type not in ['text', 'binary']:
        raise ValueError("Unrecognized value for argument 'content_type'")
    if base.startswith("//"):
        base = "http:" + base
    if ref.startswith("//"):
        ref = "http:" + ref
    print base, ref
    if base.startswith("http") or ref.startswith("http"):
        target = urljoin(base, ref)
        response = requests.get(target)
        if content_type == "text":
            return response.text
        else: # (content_type == "binary")
            return response.content
    else:
        target = _pathjoin(base, ref)
        return _read_file(target)

def selfcontain(html_string, base):
    """Make HTML self-contained

    Take an HTML string and return an HTML string with external
    dependencies as much as possible removed.

    Parameter:
    html_string : str, required
        HTML text, possibly with links to JavaScript, CSS, and images
        that would require HTTP calls for rendering

    base : str, required
        The original URL or filepath to use for resolving relative
        links and filepaths
    """
    tree = html.fromstring(html_string)
    scripts = [script for script in tree.findall('.//script')
               if 'src' in script.attrib]
    for script in scripts:
        src = script.attrib['src']
        del(script.attrib['src'])
        script.attrib['type'] = 'text/javascript'
        contents = _fetch(src, base)
        # Could go one farther with `mangle_toplevel` too,
        # but this might risk breaking things.
        script.text = minify(contents, mangle=True)
    links = [link for link in tree.findall('.//link')
             if 'href' in link.attrib and
                'style' == link.attrib.get('rel')]
    for link in links:
        href = link.attrib['href']
        for key in link.attrib:
            del(link.attrib[key])
        link.tag = 'style'
        contents = _fetch(href, base)
        link.text = cssmin(contents)
    imgs = [img for img in tree.findall('.//img')
            if 'src' in img.attrib]
    for img in imgs:
        src = img.attrib['src']
        image = _fetch(src, base, content_type="binary")
        encoded = b64encode(image)
        extension = src.split(".")[-1]
        src = "data:image/" + extension + ";base64," + encoded
        img.attrib['src'] = src
    return html.tostring(tree)

def selfcontain_ref(target):
    """
    selfcontain the HTML referenced by the argument

    Parameters:
    target : str, required
        The URL or filepath to fetch and process
    """
    string = _fetch(target)
    return selfcontain(string, target)

def main():
    """
    selfcontain the HTML referenced by a command-line argument,
    either online or on local disk
    """
    print selfcontain_ref(sys.argv[1])

if __name__ == '__main__':
    main()
