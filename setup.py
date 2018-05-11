from setuptools import setup, find_packages

setup(name="datalab",
      version="2.0.3",
      url="https://github.noao.edu/datalab/datalab",
      description="Tools for interacting with NOAO Data Lab.",
      author="M.J. Graham",
      author_email="graham@noao.edu",
      long_description="A command line tool for interacting with the NOAO Data Lab including VOSpace FUSE layer",
      packages=find_packages(exclude=['caps', 'scripts', 'test', 'vos', 'dl.excl']),
      #package_data ={
      #  'datalab': ['caps/*']
      #},
      #scripts=['scripts/datalab', 'scripts/mountvofs'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX',
        'Programming Language :: Python',
      ],
      install_requires=['requests>=2.7', 'argparse', 'lxml', 'httplib2'],
      requires=['requests (>=2.7)', 'argparse', 'lxml', 'httplib2']
     )
