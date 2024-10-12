from setuptools import setup, find_packages

setup(
    name='sense-of-humor',
    version='1.0.0',
    description='A CLI tool to generate jokes based on type, length, and audience.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'joke = sense_of_humor.joke:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: End Users/Desktop',
    ],
)
