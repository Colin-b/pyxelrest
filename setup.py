import os
from setuptools import setup, find_packages
from distutils.command.install_data import install_data

this_dir = os.path.abspath(os.path.dirname(__file__))


class CustomInstall(install_data):
    def run(self):
        install_data.run(self)

        self.announce("Performing post installation tasks...")
        from pyxelrest_post_install import PostInstall

        post_install = PostInstall(installation_files_folder=this_dir)
        post_install.perform_post_installation_tasks()


with open(os.path.join(this_dir, "README.md"), "r") as f:
    long_description = f.read()

# More information on properties: https://packaging.python.org/distributing
setup(
    name="pyxelrest",
    version=open("pyxelrest/version.py").readlines()[-1].split()[-1].strip("\"'"),
    author="Colin Bounouar",
    author_email="colin.bounouar.dev@gmail.com",
    maintainer="Colin Bounouar",
    maintainer_email="colin.bounouar.dev@gmail.com",
    url="https://colin-b.github.io/pyxelrest/",
    description="Access REST APIs from Excel using User Defined Functions (UDF)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://pypi.org/project/pyxelrest/",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Microsoft :: Windows :: Windows 7",
    ],
    keywords=["excel", "openapi", "swagger", "rest", "udf", "service"],
    packages=find_packages(exclude=["tests*", "pyxelrest.user_defined_functions.*"]),
    package_data={
        "pyxelrest": [
            "default_logging_configuration.yml.jinja2",
            "default_services_configuration.yml",
            "user_defined_functions.jinja2",
            "user_defined_functions_init.jinja2",
        ]
    },
    data_files=[
        (
            "pyxelrest_addin",
            [
                "addin/AutoLoadPyxelRestAddIn/bin/Release/AutoLoadPyxelRestAddIn.dll",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/AutoLoadPyxelRestAddIn.dll.config",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/AutoLoadPyxelRestAddIn.dll.manifest",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/AutoLoadPyxelRestAddIn.vsto",
                # Package Dependencies to ensure that it will work on any client
                "addin/AutoLoadPyxelRestAddIn/bin/Release/log4net.dll",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/log4net.xml",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.Office.Tools.Common.v4.0.Utilities.dll",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.Office.Tools.Excel.dll",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.Office.Tools.v4.0.Framework.dll",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/Microsoft.VisualStudio.Tools.Applications.Runtime.dll",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/YamlDotNet.dll",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/YamlDotNet.xml",
                # VB Add-in
                "addin/pyxelrest.xlam",
            ],
        ),
        (
            "pyxelrest_resources",
            [
                "pyxelrest_resources/excel_logo_100.png",
                "pyxelrest_resources/excel_logo_error_100.png",
                "pyxelrest_resources/excel_logo_greyscale_100.png",
                "pyxelrest_resources/python_logo_100.png",
                "pyxelrest_resources/python_logo_error_100.png",
                "pyxelrest_resources/python_logo_greyscale_100.png",
                "pyxelrest_resources/settings_logo_100.png",
                "pyxelrest_resources/settings_logo_error_100.png",
                "pyxelrest_resources/settings_logo_greyscale_100.png",
            ],
        ),
        (
            "pyxelrest_addin/resources",
            [
                "addin/AutoLoadPyxelRestAddIn/bin/Release/resources/add-file-16.png",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/resources/data-transfer-download-128.png",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/resources/file-4-16.png",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/resources/folder-3-128.png",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/resources/plus-4-16.png",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/resources/plus-4-16_grey.png",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/resources/plus-5-16.png",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/resources/refresh-128.png",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/resources/settings-8-16.ico",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/resources/settings-8-128.png",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/resources/x-mark-3-16.png",
                "addin/AutoLoadPyxelRestAddIn/bin/Release/resources/x-mark-4-16.png",
            ],
        ),
    ],
    install_requires=[
        # Used to generate UDFs python file from a template
        "jinja2==2.*",
        # Used to communicate with services
        "requests==2.*",
        # Used to communicate with Microsoft Excel (pywin32 dependency is also used to check that Excel is not running)
        "xlwings==0.18.*",
        # Used to parse configuration files
        "pyyaml==5.*",
        "pyaml==19.*",
        # Used to manage authentication
        "requests_auth==5.*",
        # Used to parse all date-time formats in a easy way
        "python-dateutil==2.*",
    ],
    extras_require={
        # Support for NTLM authentication
        "ntlm": ["requests_ntlm==1.*", "requests_negotiate_sspi==0.5.*"],
        # Support for in-memory caching
        "cachetools": ["cachetools==4.*"],
        "testing": [
            # Used to run tests
            "pytest-cov==2.*",
            # Used to mock responses
            "pytest-responses==0.4.*",
            # used for testing cache of results
            "cachetools==4.*",
        ],
    },
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "cross_location_risk=cross_location_risk.main:main",
            "send_market_risk_pam_mail=cross_location_risk.send_report:main",
            "pyxelrest_auto_update=pyxelrest_auto_update:main",
            "pyxelrest_post_install=pyxelrest_post_install:main",
            "pyxelrest_install_addin=pyxelrest_install_addin:main",
            "pyxelrest_update_services_config=pyxelrest_update_services_config:main",
        ]
    },
    scripts=[
        "pyxelrest_auto_update.py",
        "pyxelrest_post_install.py",
        "pyxelrest_install_addin.py",
        "pyxelrest_update_services_config.py",
    ],
    project_urls={
        "GitHub": "https://github.com/Colin-b/pyxelrest",
        "Changelog": "https://github.com/Colin-b/pyxelrest/blob/master/CHANGELOG.md",
        "Issues": "https://github.com/Colin-b/pyxelrest/issues",
    },
    platforms=["Windows"],
    cmdclass={"install_data": CustomInstall},
)
