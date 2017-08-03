from __future__ import absolute_import, division, print_function

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

import loginurl

setup(name='django-loginurl',
      version=loginurl.__version__,
      description='Allowing an anonymous user to log in by only visiting a URL',
      long_description=open('README.rst').read(),
      author='Fajran Iman Rusadi',
      author_email='fajran@gmail.com',
      url='http://github.com/fajran/django-loginurl/',
      license='BSD',
      download_url='http://github.com/fajran/django-loginurl/tarball/v0.2',
      packages=['loginurl', 'loginurl.management', 'loginurl.management.commands'],
      package_dir={'loginurl': 'loginurl'},
      zip_safe=False,
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      )
