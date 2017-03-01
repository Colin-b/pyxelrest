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
pip install -e . --upgrade --force-reinstall
python pyxelrest_post_install.py addin/AutoLoadPyxelRestAddIn/bin/Release addin
GOTO End

:Update
pip install -e . --upgrade
python pyxelrest_post_install.py addin/AutoLoadPyxelRestAddIn/bin/Release addin
GOTO End

:Install
pip install -e .
python pyxelrest_post_install.py addin/AutoLoadPyxelRestAddIn/bin/Release addin
GOTO End

:End
