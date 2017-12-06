from setuptools import setup

setup(name='pages',
      version='0.01',
      description='A directory application for managing contact information.',
      url='https://github.com/BaileyProgramming/pages',
      author='BaileyProgramming',
      author_email='BaileyProgramming.com',
      packages=['pages'],
      install_requires=[
          'kivy','mysqlclient','mailchimp3'
      ],
      zip_safe=False)
