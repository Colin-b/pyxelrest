import os
from setuptools import setup, find_packages

this_dir = os.path.abspath(os.path.dirname(__file__))


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
    description="Query REST APIs using Microsoft Excel formulas or python functions",
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
        "Programming Language :: Python :: 3.10",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    keywords=["excel", "openapi", "swagger", "rest", "udf", "service"],
    packages=find_packages(exclude=["tests*", "pyxelrest.generated"]),
    package_data={
        "pyxelrest": [
            "generated_api.jinja2",
            "generated_init.jinja2",
        ]
    },
    data_files=[
        (
            "pyxelrest_addin",
            [
                "addin/PyxelRestAddIn/bin/Release/PyxelRestAddIn.dll",
                "addin/PyxelRestAddIn/bin/Release/PyxelRestAddIn.dll.config",
                "addin/PyxelRestAddIn/bin/Release/PyxelRestAddIn.dll.manifest",
                "addin/PyxelRestAddIn/bin/Release/PyxelRestAddIn.vsto",
                # Package Dependencies to ensure that it will work on any client
                "addin/PyxelRestAddIn/bin/Release/log4net.dll",
                "addin/PyxelRestAddIn/bin/Release/log4net.xml",
                "addin/PyxelRestAddIn/bin/Release/Microsoft.Office.Tools.Common.v4.0.Utilities.dll",
                "addin/PyxelRestAddIn/bin/Release/Microsoft.Office.Tools.Excel.dll",
                "addin/PyxelRestAddIn/bin/Release/Microsoft.Office.Tools.v4.0.Framework.dll",
                "addin/PyxelRestAddIn/bin/Release/Microsoft.VisualStudio.Tools.Applications.Runtime.dll",
                "addin/PyxelRestAddIn/bin/Release/YamlDotNet.dll",
                "addin/PyxelRestAddIn/bin/Release/YamlDotNet.xml",
                # VB Add-in
                "addin/pyxelrest.xlam",
            ],
        ),
        (
            "pyxelrest_addin/resources",
            [
                "addin/PyxelRestAddIn/bin/Release/resources/add-file-16.png",
                "addin/PyxelRestAddIn/bin/Release/resources/data-transfer-download-128.png",
                "addin/PyxelRestAddIn/bin/Release/resources/data-transfer-download-128_grey.png",
                "addin/PyxelRestAddIn/bin/Release/resources/data-transfer-download-128_orange.png",
                "addin/PyxelRestAddIn/bin/Release/resources/file-4-16.png",
                "addin/PyxelRestAddIn/bin/Release/resources/folder-3-128.png",
                "addin/PyxelRestAddIn/bin/Release/resources/help-128.png",
                "addin/PyxelRestAddIn/bin/Release/resources/plus-4-16.png",
                "addin/PyxelRestAddIn/bin/Release/resources/plus-4-16_grey.png",
                "addin/PyxelRestAddIn/bin/Release/resources/plus-5-16.png",
                "addin/PyxelRestAddIn/bin/Release/resources/refresh-128.png",
                "addin/PyxelRestAddIn/bin/Release/resources/refresh-128_orange.png",
                "addin/PyxelRestAddIn/bin/Release/resources/settings-8-16.ico",
                "addin/PyxelRestAddIn/bin/Release/resources/settings-8-128.png",
                "addin/PyxelRestAddIn/bin/Release/resources/x-mark-3-16.png",
                "addin/PyxelRestAddIn/bin/Release/resources/x-mark-4-16.png",
            ],
        ),
    ],
    install_requires=[
        # Used to generate UDFs python file from a template
        "jinja2==3.*",
        # Used to communicate with services
        "requests==2.*",
        # Used to communicate with Microsoft Excel (pywin32 dependency is also used to check that Excel is not running)
        "xlwings==0.27.*",
        # Used to parse configuration files
        "pyyaml==6.*",
        "pyaml==21.*",
        # Used to manage authentication
        "requests_auth==6.*",
        # Used to parse all date-time formats in a easy way
        "python-dateutil==2.*",
    ],
    extras_require={
        "testing": [
            # Used to run tests
            "pytest-cov==4.*",
            # Used to mock responses
            "pytest-responses==0.5.*",
            # Optional dependency: Used to test results caching
            "cachetools==5.*",
        ],
    },
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "pyxelrest_install_addin=pyxelrest.install_addin:main",
            "pyxelrest_add_config=pyxelrest._add_config:main",
        ]
    },
    project_urls={
        "GitHub": "https://github.com/Colin-b/pyxelrest",
        "Changelog": "https://github.com/Colin-b/pyxelrest/blob/master/CHANGELOG.md",
        "Issues": "https://github.com/Colin-b/pyxelrest/issues",
    },
    platforms=["Windows"],
)
