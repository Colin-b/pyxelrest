@ECHO OFF
CLS
ECHO 1.Install
ECHO 2.Update
ECHO 3.Update (force reinstall)
ECHO.

CHOICE /C 123 /M "Enter your choice:"

:: Note - list ERRORLEVELS in decreasing order
IF ERRORLEVEL 3 GOTO ForceUpdate
IF ERRORLEVEL 2 GOTO Update
IF ERRORLEVEL 1 GOTO Install

:ForceUpdate
pip install pypiwin32 --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple --upgrade
pip install -e . --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple --upgrade --force-reinstall
python pyxelrest_post_install.py --addindirectory addin/AutoLoadPyxelRestAddIn/bin/Release --vbaddindirectory addin
GOTO End

:Update
pip install pypiwin32 --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple --upgrade
pip install -e . --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple --upgrade
python pyxelrest_post_install.py --addindirectory addin/AutoLoadPyxelRestAddIn/bin/Release --vbaddindirectory addin
GOTO End

:Install
pip install pypiwin32 --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple
pip install -e . --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple
python pyxelrest_post_install.py --addindirectory addin/AutoLoadPyxelRestAddIn/bin/Release --vbaddindirectory addin
GOTO End

:End
