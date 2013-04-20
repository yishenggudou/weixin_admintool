from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='weixin_admintool',
      version=version,
      description="weixin",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='weixin linux tool',
      author='@timger',
      author_email='yishenggudou@gmail.com',
      url='http://www.timger.info/about',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      data_files = [('/etc/nginx/sites-enabled/',['weinxinadmintool_nginx.conf'])],
      scripts = ['scripts/weixin_admintool.py'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
