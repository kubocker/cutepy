
from setuptools import setup, find_packages

setup(name='cutepy',
      version='0.1.0',
      description='common ui and commands for pyqt5',
      author='kubocker',
      author_email='kubocker@gmail.com',
      maintainer='kubocker',
      maintainer_email='kubocker@gmail.com',
      url='https://github.com/kubocker/cutepy',
      packages=find_packages(),
      license="MIT",
      entry_points={
          'console_scripts': [
              'cute.py = cutepy.manage:create'
          ]
      },
      )
