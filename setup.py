from setuptools import setup, find_packages

setup(name='corker',
      version='0.4',
      description='Another WSGI Framework',
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Topic :: Internet :: WWW/HTTP",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   'Programming Language :: Python',
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4",
                   ],
      license='BSD',
      author='Joshua D. Boyd',
      author_email='jdboyd@jdboyd.net',
      url='https://github.com/jd-boyd/corker',
      packages=find_packages(),
      package_data={'': ['README.md', 'LICENSE.txt']},
      install_requires=['webob', 'routes'],
      tests_require=['nose', 'webtest'],
     )
