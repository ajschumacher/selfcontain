from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(name = 'selfcontain',
      packages = ['selfcontain'],
      description = 'shoe-horn a web page into a single html file',
      long_description = long_description,
      license = 'MIT',
      author = 'Aaron Schumacher',
      author_email = 'ajschumacher@gmail.com',
      url = 'https://github.com/ajschumacher/selfcontain',
      download_url = 'https://github.com/ajschumacher/selfcontain/tarball/0.2',
      version = '0.2',
      install_requires = ['lxml', 'requests', 'rjsmin', 'rcssmin'],
      scripts = ['bin/selfcontain'])
