from setuptools import setup
setup(name='paperboy_analyzer',
      version="0.1",
      description="A python module to read rss feeds and extract text from articles from various news sources",
      url="https://github.com/benfollis/paperboy_analyzer",
      author="Ben Follis",
      license="GPLv3",
      packages=['paperboy_analyzer', 'paperboy_analyzer.extractors', 'paperboy_analyzer.fetchers'],
      install_requires=['beautifulsoup4', 'feedparser'],
      zip_safe=False,
      scripts=['bin/paperboy_analyzer'])