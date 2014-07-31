# selfcontain

Make HTML more self-contained by in-lining:

 * JavaScript (minified)
 * CSS (minified)
 * Images (base-64 encoded)
     * Including (explicitly linked) favicons

For straightforward cases, this will take an HTML document which might
have external dependencies and return an HTML document with no
external dependencies - a single self-contained file that you could
send as an email attachment, or show as a presentation without
worrying about internet connectivity, for example.
