===========
selfcontain
===========

Make HTML more self-contained by in-lining:

- JavaScript (minified)
- CSS (minified)
- Images (base-64 encoded)

  - Including (explicitly linked) favicons

For straightforward cases, this will take an HTML document which might
have external dependencies and return an HTML document with no
external dependencies - a single self-contained file that you could
send as an email attachment, or show as a presentation without
worrying about internet connectivity, for example.

Cases that are *not* straightforward are those that involve loading
things via JavaScript, ``iframe`` things, fonts, and things I haven't
thought of. Pull requests welcome!


Usage
-----

Loaded as a module, ``selfcontain()`` takes an HTML string and base
path or URL and is the main function to know. Command-line usage wraps
the minor extension ``selfcontain_ref()``, which takes a string
specifying a file path or URL to fetch and process::

  selfcontain test_in.html > test_out.html
  # or
  selfcontain https://raw.githubusercontent.com/ajschumacher/selfcontain/master/test_in.html > test_out.html
