from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='lightening_alert',
      version='0.0.1',
      description=u"Area Lightning Alert",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Mandy Wu",
      author_email='kitty911007@gmail.com',
      url='https://github.com/Mandy1007/lightning_alert.git',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click', 'quadkey'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      lightning_alert=lightning_alert.scripts.cli:cli
      """
      )
