import os
from setuptools import setup, find_packages
from distutils.command.install_data import install_data
import distutils.sysconfig

this_dir = os.path.abspath(os.path.dirname(__file__))
# Corresponds to Lib\site-packages folder
modules_dir = distutils.sysconfig.get_python_lib()
data_dir = os.path.join(modules_dir, '..', '..')
scripts_dir = os.path.join(modules_dir, '..', '..', 'Scripts')


class install_pyxelrest_data(install_data):
    def run(self):
        install_data.run(self)
        from pyxelrest_post_install import PostInstall
        post_install = PostInstall(os.path.join(data_dir, 'pyxelrest_addin'),
                                   os.path.join(data_dir, 'pyxelrest_vb_addin'),
                                   installation_files_folder=this_dir,
                                   modules_folder=modules_dir,
                                   scripts_folder=scripts_dir)
        post_install.perform_post_installation_tasks()

with open(os.path.join(this_dir, 'README.rst'), 'r') as f:
    long_description = f.read()

# More information on properties: https://packaging.python.org/distributing
setup(name='pyxelrest',
      version=open("pyxelrest/_version.py").readlines()[-1].split()[-1].strip("\"'"),
      author='Engie',
      # TODO Provide a support mailbox for our products
      author_email='colin.bounouar@external.engie.com',
      maintainer='Engie',
      # TODO Provide a support mailbox for our products
      maintainer_email='colin.bounouar@external.engie.com',
      url="http://guru.trading.gdfsuez.net/bitbucket/projects/RMS/repos/pyxelrest",
      description="Access REST APIs from Excel using User Defined Functions (UDF)",
      long_description=long_description,
      # TODO Package to artifactory and assert that bamboo will keep it up to date
      download_url='http://www.engie.com',
      classifiers=[
          "Development Status :: 5 - Production/Stable",
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
      packages=find_packages(exclude=['tests', 'testsutils']),
      package_data={
         'pyxelrest': [
             'authentication_responses_server.jinja2',
             'authentication_responses_servers.jinja2',
             'default_logging_configuration.ini.jinja2',
             'default_services_configuration.ini',
             'user_defined_functions.jinja2'
         ]
      },
      data_files=[
          (
              'pyxelrest_addin', [
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/AutoLoadPyxelRestAddIn.dll',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/AutoLoadPyxelRestAddIn.dll.config',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/AutoLoadPyxelRestAddIn.dll.manifest',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/AutoLoadPyxelRestAddIn.vsto',
                  # Package Dependencies to ensure that it will work on any client
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/INIFileParser.dll',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/INIFileParser.xml',
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
              'pyxelrest_vb_addin', [
                  'addin/pyxelrest.xlam'
              ]
          ),
          (
              'pyxelrest_addin/resources', [
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/resources/data-transfer-download-128.png',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/resources/folder-3-128.png',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/resources/refresh-128.png',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/resources/settings-8-16.ico',
                  'addin/AutoLoadPyxelRestAddIn/bin/Release/resources/settings-8-128.png'
              ]
          )
      ],
      tests_require=[
          # Used to run tests
          'nose',
          # Used to generate a jwt token
          'pyjwt'
      ],
      install_requires=[
          # Used to generate UDFs python file from a template
          'jinja2==2.9.5',
          # Used to communicate with services
          'requests==2.13.0',
          # Used to check that Excel is not running and required by xlwings (220 is only provided for Python 3.6)
          'pypiwin32>=219',
          # Used to send responses to Microsoft Excel by xlwings - Force dependency order as not managed properly by PIP
          'comtypes==1.1.3-2',
          # Used to communicate with Microsoft Excel
          'xlwings==0.10.3',
          # Used to parse logging configuration file
          'pyaml==16.12.2',
          # Used to run authentication services (also used in test cases)
          'flask',
          # Used to parse JSON faster than the embedded json module
          'ujson==1.35'
      ],
      scripts=[
          'pyxelrest_auto_update.py',
          'pyxelrest_post_install.py'
      ],
      platforms=[
          'Windows'
      ],
      cmdclass={
          'install_data': install_pyxelrest_data
      }
      )
