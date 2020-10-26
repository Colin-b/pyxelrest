!define VERSION "1.0.0"
Name "PyxelRest ${VERSION}"
OutFile "pyxelrest_installer-${VERSION}.exe"
InstallDir "$%APPDATA%\pyxelrest"


Section "Creating python virtual environment" create_venv

nsDialogs::SelectFileDialog open "$%USERPROFILE%\AppData\Local\Programs\Python\Python38\pythonw.exe" "Python executable | pythonw.exe"
Pop $0
ExecWait '"$0" "-m" "venv" "$INSTDIR\pyxelrest_venv"'

SectionEnd

Page Directory
Page InstFiles