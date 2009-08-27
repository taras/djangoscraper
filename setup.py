from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='django-scraper',
      version=version,
      description="Django Scraper app integrates scrapy and django to allow task based scraping.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='django scrapy',
      author='Taras Mankovski',
      author_email='tarasm@gmail.com',
      url='http://taras.cc',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
