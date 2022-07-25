from setuptools import setup

setup(name='jtsstats',
      version='0.1.0',
      description='JTS data analysis',
      url='https://github.com/n10ds/jts/tree/main/py',
      author='Federico Botta',
      author_email='f.botta@exeter.ac.uk',
      license='MIT',
      packages=['jtsstats'],
      install_requires = [
          'pandas','geopandas', 'numpy', 'pkg_resources','matplotlib','descartes',
          ],
      zip_safe=False)