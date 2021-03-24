from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='UnicodeParser',
  version='0.0.1',
  description='This is simplified configparser but it works with unicode!',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Yaros',
  author_email='siubaiev@gmail.org',
  license='MIT', 
  classifiers=classifiers,
  keywords='conifigrarser', 
  packages=find_packages(),
  install_requires=['codecs'] 
)
