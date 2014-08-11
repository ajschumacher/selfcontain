### Fairly minimal notes on publishing to PyPI

First, set things up nicely. Check out the `.gitignore` and `setup.py`
here. The README could be in whatever format, but just use
[reStructuredText][] and life will be easier. Make the package in some
reasonable way.

[reStructuredText]: http://docutils.sourceforge.net/rst.html

With the package set up some reasonable way, it's useful to have it
available for testing on the local machine:

```
python setup.py develop
```

Second, get set up with a [PyPI][] account. Then you're ready to
register the package with PyPI!!

[PyPI]: https://pypi.python.org/pypi

```
python setup.py register
```

You can either let the registratoin step make it, or you can yourself
put your username and password in `~/.pypirc`. Here's a minimal one:

```
[server-login]
username:FILL_IN
password:FILL_IN
```

(You can get away with not keeping a `.pypirc` for registering, but it
didn't seem to work for uploading.)

Now to do an actual release, ensure that everything is in place, make
sure version numbers are the right way everywhere, and:

```
python setup.py sdist upload
```

That should do it!

I found these references useful in getting up and running:

 * Scott Torborg's [How To Package Your Python Code](http://www.scotttorborg.com/python-packaging/)
 * Peter Downs' [How to submit a package to PyPI](http://peterdowns.com/posts/first-time-with-pypi.html)
