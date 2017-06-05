import os

from setuptools import setup, find_packages

setup(name='watchbot_reduce',
      version='0.1',
      description=u"Watchbot reduce mode helpers for python",
      # long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Matthew Perry",
      author_email='perry@mapbox.com',
      url='https://github.com/mapbox/python-watchbot-reduce',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False)
