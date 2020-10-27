!define VERSION "1.0.0"
Unicode True
Name "PyxelRest ${VERSION}"
OutFile "pyxelrest_installer-${VERSION}.exe"
InstallDir "$%APPDATA%\pyxelrest"

!include TextFunc.nsh
!include nsDialogs.nsh

!define DefaultPathToPython "$%USERPROFILE%\AppData\Local\Programs\Python\Python38\pythonw.exe"

Var PathToPythonTextBox
Var BrowsePathToPythonButton
Var NtlmCheckBox
Var CacheToolsCheckBox
Var CertifiCheckBox

Var InstallAddInCheckBox
Var PathToConfigurationTextBox
Var BrowsePathToConfigurationButton

Function pythonOptionsPageCreate
    nsDialogs::Create 1018

    ${NSD_CreateLabel} 0 0u 100% 12u "Python executable"
    Pop $0

    ${NSD_CreateText} 0 15u 80% 12u "${DefaultPathToPython}"
    Pop $PathToPythonTextBox

    ${NSD_CreateBrowseButton} 320 15u 20% 12u "Browse"
    pop $BrowsePathToPythonButton

    ${NSD_CreateCheckbox} 0 50u 100% 10u "Handle custom SSL certificates"
    Pop $CertifiCheckBox

    ${NSD_CreateCheckbox} 0 65u 100% 10u "Handle Microsoft Windows authentication"
    Pop $NtlmCheckBox

    ${NSD_CreateCheckbox} 0 80u 100% 10u "Allow to cache requests results"
    Pop $CacheToolsCheckBox

    ${NSD_OnClick} $BrowsePathToPythonButton browsePathToPython
    nsDialogs::Show
FunctionEnd

Function pythonOptionsPageLeave
FunctionEnd

Function addinOptionsPageCreate
    nsDialogs::Create 1018

    ${NSD_CreateCheckbox} 0 0 100% 10u "&Install Microsoft Excel add-in"
    Pop $InstallAddInCheckBox
    ${NSD_Check} $InstallAddInCheckBox

    ${NSD_CreateLabel} 0 15u 100% 12u "Path to up to date services configurations"
    Pop $0

    ${NSD_CreateText} 0 30u 80% 12u ""
    Pop $PathToConfigurationTextBox

    ${NSD_CreateBrowseButton} 320 30u 20% 12u "Browse"
    pop $BrowsePathToConfigurationButton

    ${NSD_OnClick} $BrowsePathToConfigurationButton browsePathToConfiguration
    nsDialogs::Show

    nsDialogs::Show
FunctionEnd

Function addinOptionsPageLeave
FunctionEnd

Function browsePathToPython

nsDialogs::SelectFileDialog open "${DefaultPathToPython}" "Python executable | pythonw.exe"
Pop $0

FunctionEnd

Function browsePathToConfiguration

nsDialogs::SelectFileDialog open "C:" "YAML configuration file | *.yaml"
Pop $0

FunctionEnd

Section "Creating python virtual environment" create_venv

ExecWait '"$0" "-m" "venv" "$INSTDIR\pyxelrest_venv"'

SectionEnd

Page Directory
Page Custom pythonOptionsPageCreate pythonOptionsPageLeave
Page Custom addinOptionsPageCreate addinOptionsPageLeave
Page InstFiles
