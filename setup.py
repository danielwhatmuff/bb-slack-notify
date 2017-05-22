"""
Setup.py for notifybot
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='notifybot',
    version='0.0.1',
    description='Slack Notifications for Travis Deploys',
    long_description='A CLI to notify Slack on Travis CI deployments by API token or Incoming Webhook URL',
    url='https://github.com/danielwhatmuff/notifybot',
    author='Daniel Whatmuff',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='travis deployment slack notification',
    py_modules=["notifybot"],
    install_requires=['slackclient', 'requests'],
    scripts=['bin/notifybot'],
)
