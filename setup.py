from setuptools import setup, find_packages
from cutepy import __version__ as version


setup(name='cutepy',
      version=version,
      description='common ui and commands for pyqt5',
      author='kubocker',
      author_email='kubocker@gmail.com',
      maintainer='kubocker',
      maintainer_email='kubocker@gmail.com',
      url='https://github.com/kubocker/cutepy',
      license="MIT",
      packages=find_packages(),
      install_requires=[
          "django-contrib-comments",
          "django >= 1.8, < 1.11",
          "filebrowser_safe >= 0.4.6",
          "grappelli_safe >= 0.4.5",
          "tzlocal >= 1.0",
          "bleach >= 2.0",
          "beautifulsoup4 >= 4.5.3",
          "requests >= 2.1.0",
          "requests-oauthlib >= 0.4",
          "future >= 0.9.0",
          "pillow",
          "chardet",
          "pyqt5",
          "fire",
      ],
      entry_points={
          'console_scripts': [
              'cute = cutepy.manage:create'
          ]
      },)
