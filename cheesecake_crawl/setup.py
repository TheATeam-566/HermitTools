from setuptools import setup

setup(
    name="cheese scraper",
    version="0.1",
    author="Chris Pinkney",
    author_email="hey@chrispinkney.com",
    install_requires=["bs4", "requests", "firebase-admin"],
    entry_points={"console_scripts": ["cheese scraper = main : main"]},
)
