__author__ = "Alex DeLorenzo"
from setuptools import setup
from pathlib import Path


PKG_NAME = "onhold-ding"
NAME = 'ding'
VERSION = "0.0.2"
LICENSE = "AGPL-3.0"

DESC = "🔊 Play music after jobs complete"

REQUIREMENTS = \
  Path('requirements.txt') \
    .read_text() \
    .split('\n')

README = Path('README.md').read_text()

ENTRY_POINTS = {
  "console_scripts":
    [f"ding = {NAME}.after:cmd"]
}

setup(
      name=PKG_NAME,
      version=VERSION,
      description=DESC,
      long_description=README,
      long_description_content_type="text/markdown",
      url="https://alexdelorenzo.dev",
      author=__author__,
      license=LICENSE,
      packages=[NAME],
      zip_safe=False,
      install_requires=REQUIREMENTS,
      entry_points=ENTRY_POINTS,
      python_requires='>=3.6',
      include_package_data=True
)
