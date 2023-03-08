import os
import io
import re

from setuptools import setup, find_packages, find_namespace_packages

def get_version():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(current_dir, 'fastdi.proj', 'fastdi', '__init__.py')
    with io.open(version_file, encoding='utf-8') as f:
        return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)


LONG_DESCRIPTION = ''
with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name = 'fastdi',
    version = get_version(),
    description = 'Python dependency injection and configuration library.',
    author = 'Anton Vasyaev',
    author_email = 'vasyaevanton@gmail.com',
    license = 'MIT',
    keywords = '',
    url ='https://github.com/Anton-Vasyaev/fastdi',
    packages = find_packages(where='fastdi.proj'),
    package_dir = {'': 'fastdi.proj'},
    install_requires = [
        'nameof>=0.0.1'
    ],
    requires_python='>=3.9.0',
    classifiers = [
        'Development Status :: Alpha - 0.0.1',
        'Environment :: Dependency Injection',
        'Environment :: Serialization'
        'Environment :: Deserialization',
        'Environment :: Service Setup'
    ]
)