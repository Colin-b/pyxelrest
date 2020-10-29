!define VERSION "1.0.0"
Unicode True
Name "PyxelRest ${VERSION}"
BrandingText "Call REST APIs as functions"
OutFile "pyxelrest_installer-${VERSION}.exe"
InstallDir "$%APPDATA%\pyxelrest"

!include TextFunc.nsh
!include nsDialogs.nsh

Var PathToPython
Var PathToPythonTextBox
Var BrowsePathToPythonButton

Var NtlmCheckBox
Var CacheToolsCheckBox
Var CertifiCheckBox


Var InstallAddIn
Var InstallAddInCheckBox

Var PathToConfiguration
Var PathToConfigurationTextBox
Var BrowsePathToConfigurationButton

Var InstallDefaultConfigurationCheckBox

Function .onInit

	StrCpy $PathToPython "$%USERPROFILE%\AppData\Local\Programs\Python\Python38\pythonw.exe"

	StrCpy $InstallAddIn "${BST_CHECKED}"
	StrCpy $PathToConfiguration ""

FunctionEnd

Function pythonOptionsPageCreate
    nsDialogs::Create 1018

    ${NSD_CreateGroupBox} 0 0u 100% 35u "Python executable"
    Pop $0

    ${NSD_CreateText} 5u 15u 72% 12u "$PathToPython"
    Pop $PathToPythonTextBox

    ${NSD_CreateBrowseButton} 205u 13u 20% 15u "Browse..."
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

Function browsePathToPython

    ${NSD_GetText} $PathToPythonTextBox $0
    nsDialogs::SelectFileDialog open $0 "Python executable | pythonw.exe"
    Pop $0
    ${If} $0 != ""
        ${NSD_SetText} $PathToPythonTextBox $0
    ${EndIf}

FunctionEnd

Function pythonOptionsPageLeave

    ${NSD_GetText} $PathToPythonTextBox $PathToPython
    ${IfNot} ${FileExists} $PathToPython
        MessageBox mb_iconstop "The provided path to python does not exists. Please install it or specify an existing path."
        Abort
    ${EndIf}
FunctionEnd

Function addinOptionsPageCreate
    nsDialogs::Create 1018

    ${NSD_CreateCheckbox} 0 0 100% 10u "Install Microsoft Excel add-in"
    Pop $InstallAddInCheckBox
    ${NSD_SetState} $InstallAddInCheckBox $InstallAddIn

    ${NSD_CreateGroupBox} 0 15u 100% 35u "Path to up to date services configurations"
    Pop $0

    ${NSD_CreateText} 5u 30u 72% 12u "$PathToConfiguration"
    Pop $PathToConfigurationTextBox

    ${NSD_CreateBrowseButton} 205u 28u 20% 15u "Browse..."
    pop $BrowsePathToConfigurationButton

    ${NSD_CreateCheckbox} 0 65u 100% 10u "Keep default services (petstore and pyxelrest)"
    Pop $InstallDefaultConfigurationCheckBox
    ${NSD_Check} $InstallDefaultConfigurationCheckBox

    ${NSD_OnClick} $BrowsePathToConfigurationButton browsePathToConfiguration
    nsDialogs::Show

    nsDialogs::Show
FunctionEnd

Function browsePathToConfiguration

    ${NSD_GetText} $PathToConfigurationTextBox $0
    nsDialogs::SelectFileDialog open $0 "YAML configuration file | *.y*ml"
    Pop $0
    ${If} $0 != ""
        ${NSD_SetText} $PathToConfigurationTextBox $0
    ${EndIf}

FunctionEnd

Function addinOptionsPageLeave

    ${NSD_GetText} $PathToConfigurationTextBox $PathToConfiguration
    ${NSD_GetState} $InstallAddInCheckBox $InstallAddIn

FunctionEnd

Section "Creating python virtual environment" create_venv

    AddSize 54000
    ExecWait '"$PathToPython" "-m" "venv" "$INSTDIR\pyxelrest_venv"'

SectionEnd

Page Directory
Page Custom pythonOptionsPageCreate pythonOptionsPageLeave
Page Custom addinOptionsPageCreate addinOptionsPageLeave
Page InstFiles
