from setuptools import setup, find_packages
setup(name='pyxelrest',
      version=open("pyxelrest/_version.py").readlines()[-1].split()[-1].strip("\"'"),
      description="Python Module to provide access to REST APIs using Swagger from Excel UDFs",
      url="http://rms.gdfsuez.net:8310/stash/projects/RMS/repos/pyxelrest",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers"
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Operating System :: Microsoft :: Windows :: Windows 7"
      ],
      keywords='excel pyxelrest swagger',
      packages=find_packages(),
      package_data={
         '': ['*.ini', '*.tpl'],
      },
      install_requires=[
          'jinja2',
          'requests',
          'xlwings'
        ]
      )
