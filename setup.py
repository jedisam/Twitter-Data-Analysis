#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['mock==4.0.3', 'pytest==7.1.1']

test_requirements = ['textblob', 'pandas', 'matplotlib', 'sklearn', 'nltk', 'gensim', 'stemmer', 'wordcloud', 'streamlit', 'sql', 'pytest>=3', ]

setup(
    author="Yididiya Samuel",
    email="yidisam18@gmail.com",
    python_requires='>=3.6',
    description="Scripts for controlling Twitter Analysis",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='Topic_modeling, Sentiment_analysis, EDA, Data_Preprocessing, unit_testing, hot_issues, pytest',
    name='Twitter Data Analysis',
    packages=find_packages(include=['src', 'src.*']),
    test_suite='Tests',
    tests_require=test_requirements,
    url='https://github.com/jedisam/Twitter-Data-Analysis',
    version='0.1.0',
    zip_safe=False,
)
