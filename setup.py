from setuptools import setup

setup(name = 'selfcontain',
      packages = ['selfcontain'],
      description = 'shoe-horn a web page into a single html file',
      license = 'MIT',
      author = 'Aaron Schumacher',
      author_email = 'ajschumacher@gmail.com',
      url = 'https://github.com/ajschumacher/selfcontain',
      download_url = 'https://github.com/ajschumacher/selfcontain/tarball/0.1.1',
      version = '0.1.1',
      install_requires = ['lxml', 'requests', 'slimit', 'rcssmin'],
      scripts = ['bin/selfcontain'])
