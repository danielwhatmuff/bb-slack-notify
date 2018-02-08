"""
Setup.py for bb-slack-notify
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='bb-slack-notify',
    version='0.0.5',
    description='Slack Notifications for Bitbucket Pipeline deploys',
    long_description='A CLI to notify Slack on pipeline deployments by API token or Incoming Webhook URL',
    url='https://github.com/danielwhatmuff/bb-slack-notify',
    author='Daniel Whatmuff',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='bitbucket pipelines deployment slack notification',
    py_modules=["bb-slack-notify"],
    install_requires=['slackclient', 'requests'],
    scripts=['bin/bb-slack-notify'],
)
