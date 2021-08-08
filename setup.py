import io
from setuptools import find_packages, setup


# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(name='project0',
      version='0.1',
      description='project0',
      long_description=long_description(),
      url='https://github.com/sghan811/project0',
      author='sghan811',
      author_email='sghan811@gmail.com',
      license='DASTY',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          ],
      zip_safe=False)