import os
from setuptools import setup, find_packages
from distutils.command.install_data import install_data
import subprocess
import distutils.sysconfig

this_dir = os.path.abspath(os.path.dirname(__file__))
modules_dir = distutils.sysconfig.get_python_lib()


class install_pyxelrest_data(install_data):
    def run(self):
        install_data.run(self)
        subprocess.check_call(['python', 'pyxelrest_post_install.py', '--installdirectory', this_dir, '--modulesdirectory', modules_dir])

with open(os.path.join(this_dir, 'README.rst'), 'r') as f:
    long_description = f.read()

setup(name='pyxelrest',
      version=open("pyxelrest/_version.py").readlines()[-1].split()[-1].strip("\"'"),
      author='Engie',
      # TODO Provide a support mailbox for our products
      author_email='colin.bounouar@external.engie.com',
      maintainer='Engie',
      # TODO Provide a support mailbox for our products
      maintainer_email='colin.bounouar@external.engie.com',
      url="http://rms.gdfsuez.net:8310/stash/projects/RMS/repos/pyxelrest",
      description="Access REST APIs from Excel using User Defined Functions (UDF)",
      long_description=long_description,
      # TODO Package to artifactory and assert that bamboo will keep it up to date
      download_url='http://www.engie.com',
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers"
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Operating System :: Microsoft :: Windows :: Windows 7"
      ],
      keywords=[
          'excel',
          'openapi',
          'swagger',
          'rest',
          'udf',
          'service'
      ],
      packages=find_packages(exclude=['tests']),
      package_data={
         'pyxelrest': ['default_configuration.ini', 'user_defined_functions.tpl']
      },
      data_files=[
          (
              'pyxelrest_addin', [
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/AutoLoadPyxelRestAddIn.dll',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/AutoLoadPyxelRestAddIn.dll.config',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/AutoLoadPyxelRestAddIn.dll.manifest',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/AutoLoadPyxelRestAddIn.vsto',
                  # Package Dependencies to ensure that it will work on any client
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/log4net.dll',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/log4net.xml',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.Office.Tools.Common.dll',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.Office.Tools.Common.v4.0.Utilities.dll',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.Office.Tools.Common.v4.0.Utilities.xml',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.Office.Tools.Common.xml',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.Office.Tools.dll',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.Office.Tools.Excel.dll',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.Office.Tools.Excel.xml',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.Office.Tools.v4.0.Framework.dll',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.Office.Tools.v4.0.Framework.xml',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.VisualStudio.Tools.Applications.Runtime.dll',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.VisualStudio.Tools.Applications.Runtime.xml'
              ]
          ),
          (
              'pyxelrest_addin/resources', [
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/resources/openapi_logo.png'
              ]
          )
      ],
      install_requires=[
          'jinja2>=2.8',
          'requests>=2.12.2',
          'xlwings==0.10.1'
      ],
      scripts=[
          'pyxelrest_post_install.py'
      ],
      platforms=[
          'Windows'
      ],
      cmdclass={
          'install_data': install_pyxelrest_data
      }
      )
