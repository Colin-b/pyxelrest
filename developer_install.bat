@ECHO OFF
CLS

python -m pip install . --upgrade --force-reinstall
SET /P "path_to_conf=Please provide path to the up to date configuration:"
python pyxelrest/install_addin.py --source addin/PyxelRestAddIn/bin/Release --check_pre_releases --path_to_up_to_date_configuration "%path_to_conf%"
