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
python -m pip install . --upgrade --force-reinstall
python pyxelrest_post_install.py
SET /P "path_to_conf=Please provide path to the up to date configuration:"
python pyxelrest_install_addin.py --add_in_directory addin/AutoLoadPyxelRestAddIn/bin/Release --path_to_up_to_date_configuration "%path_to_conf%"
GOTO End

:Update
python -m pip install . --upgrade
python pyxelrest_post_install.py
SET /P "path_to_conf=Please provide path to the up to date configuration:"
python pyxelrest_install_addin.py --add_in_directory addin/AutoLoadPyxelRestAddIn/bin/Release --path_to_up_to_date_configuration "%path_to_conf%"
GOTO End

:Install
python -m pip install .
python pyxelrest_post_install.py
SET /P "path_to_conf=Please provide path to the up to date configuration:"
python pyxelrest_install_addin.py --add_in_directory addin/AutoLoadPyxelRestAddIn/bin/Release --path_to_up_to_date_configuration "%path_to_conf%"
GOTO End

:End
