
from setuptools import setup, find_packages

setup(name='cutepy',
      version='0.1.1',
      description='common ui and commands for pyqt5',
      author='kubocker',
      author_email='kubocker@gmail.com',
      maintainer='kubocker',
      maintainer_email='kubocker@gmail.com',
      url='https://github.com/kubocker/cutepy',
      license="MIT",
      packages=find_packages(),
      install_requires=[
          "pyqt5",
          "fire",
      ],
      entry_points={
          'console_scripts': [
              'cute.py = cutepy.manage:create'
          ]
      },)
