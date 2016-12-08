import os
from setuptools import setup, find_packages, command

this_dir = os.path.abspath(os.path.dirname(__file__))


class CustomInstall(command.install):
    def run(self):
        command.install.run(self)
        filename = os.path.join(self.prefix, "Scripts", "pyxelrest_post_install.py")
        if not os.path.isfile(filename):
            raise RuntimeError("Cannot find post installation script: '%s'" % (filename,))
        exec(filename)


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
      packages=find_packages(),
      package_data={
         '': ['*.ini', '*.tpl', '*.rst'],
      },
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
          'install': CustomInstall
      }
      )
