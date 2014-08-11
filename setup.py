from setuptools import setup

setup(name = 'selfcontain',
      packages = ['selfcontain'],
      description = 'shoe-horn a web page into a single html file',
      license = 'MIT',
      author = 'Aaron Schumacher',
      author_email = 'ajschumacher@gmail.com',
      url = 'https://github.com/ajschumacher/selfcontain',
      download_url = 'https://github.com/ajschumacher/selfcontain/tarball/0.2',
      version = '0.2',
      install_requires = ['lxml', 'requests', 'rjsmin', 'rcssmin'],
      scripts = ['bin/selfcontain'])
