from setuptools import setup

setup(name='cuzcatlan',
      version='0.0.1',
      description="Edwin Juarez's personal library.",
      url='https://github.com/edjuaro/cuscatlan',
      author='Edwin F. Juarez',
      author_email='ejuarez@ucsd.edu',
      license='MIT',
      packages=['cuzcatlan'],
      zip_safe=False,
      install_requires=[
          'numpy',
          'scipy',
          'pandas',
          'matplotlib',
          ],
      )
