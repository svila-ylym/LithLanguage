# setup.py

from setuptools import setup, find_packages

setup(
    name='lith',
    version='0.1.1',
    author='UNREAL',
    author_email='3775359187@qq.com',
    description='A lightweight programming language based on Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/UNREAL/Lith-Language',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)