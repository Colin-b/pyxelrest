!define VERSION "1.0.0"
Unicode True
Name "PyxelRest ${VERSION}"
BrandingText "Call REST APIs as functions"
OutFile "pyxelrest_installer-${VERSION}.exe"
InstallDir "$%APPDATA%\pyxelrest"

InstType "Full" IT_FULL
InstType "Minimal" IT_MIN

!include TextFunc.nsh
!include nsDialogs.nsh

Var PathToPython
Var PathToPythonTextBox
Var BrowsePathToPythonButton

Var PathToConfiguration
Var PathToConfigurationTextBox
Var BrowsePathToConfigurationButton

Var PathToAddInInstaller

Function .onInit

	StrCpy $PathToPython "$%USERPROFILE%\AppData\Local\Programs\Python\Python38\pythonw.exe"
	StrCpy $PathToConfiguration ""

FunctionEnd

Function optionsPageCreate
    nsDialogs::Create 1018

    ${NSD_CreateGroupBox} 0 0u 100% 35u "Python executable"
    Pop $0

    ${NSD_CreateText} 5u 15u 72% 12u "$PathToPython"
    Pop $PathToPythonTextBox

    ${NSD_CreateBrowseButton} 205u 13u 20% 15u "Browse..."
    pop $BrowsePathToPythonButton
    ${NSD_OnClick} $BrowsePathToPythonButton browsePathToPython

    ${NSD_CreateGroupBox} 0 50u 100% 35u "Path to up to date services configurations"
    Pop $0

    ${NSD_CreateText} 5u 65u 72% 12u "$PathToConfiguration"
    Pop $PathToConfigurationTextBox

    ${NSD_CreateBrowseButton} 205u 63u 20% 15u "Browse..."
    pop $BrowsePathToConfigurationButton
    ${NSD_OnClick} $BrowsePathToConfigurationButton browsePathToConfiguration

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

Function browsePathToConfiguration

    ${NSD_GetText} $PathToConfigurationTextBox $0
    nsDialogs::SelectFileDialog open $0 "YAML configuration file | *.y*ml"
    Pop $0
    ${If} $0 != ""
        ${NSD_SetText} $PathToConfigurationTextBox $0
    ${EndIf}

FunctionEnd

Function optionsPageLeave

    ${NSD_GetText} $PathToPythonTextBox $PathToPython
    ${IfNot} ${FileExists} $PathToPython
        MessageBox mb_iconstop "The provided path to python does not exists. Please install it or specify an existing path."
        Abort
    ${EndIf}
    # TODO Extract the folder from the executable path
	StrCpy $PathToAddInInstaller "$PathToPythonFolder\pyxelrest_install_addin.exe"

    ${NSD_GetText} $PathToConfigurationTextBox $PathToConfiguration

FunctionEnd

SectionGroup /e "Python"

Section "Virtual environment" install_venv

    SectionInstType ${IT_FULL}
    # Approximate venv size is 15MB
    AddSize 15360
    ExecWait '"$PathToPython" "-m" "venv" "$INSTDIR\pyxelrest_venv"'
	StrCpy $PathToPython "$INSTDIR\pyxelrest_venv\Scripts\python.exe"
	StrCpy $PathToAddInInstaller "$INSTDIR\pyxelrest_venv\Scripts\pyxelrest_install_addin.exe"

SectionEnd

Section "Python module" install_module

    SectionInstType RO
    # Approximate modules size is 37MB
    AddSize 37888
    ExecWait '"$PathToPython" "-m" "pip" "install" "pyxelrest==${VERSION}"'

SectionEnd

SectionGroup "Additional features"

Section "Handle custom SSL certificates" handle_custom_ssl

    SectionInstType ${IT_FULL}
    # Approximate modules size is 650KB
    AddSize 650
    ExecWait '"$PathToPython" "-m" "pip" "install" "python-certifi-win32==1.*"'

SectionEnd

Section "Handle Microsoft Windows authentication" handle_ms_auth

    SectionInstType ${IT_FULL}
    # Approximate modules size is 7MB
    AddSize 7189
    ExecWait '"$PathToPython" "-m" "pip" "install" "requests_ntlm==1.*" "requests_negotiate_sspi==0.5.*"'

SectionEnd

Section "Allow to cache requests results" allow_cached_results

    SectionInstType ${IT_FULL}
    # Approximate modules size is 150KB
    AddSize 150
    ExecWait '"$PathToPython" "-m" "pip" "install" "cachetools==4.*"'

SectionEnd

SectionGroupEnd

SectionGroupEnd

SectionGroup /e "Microsoft Excel"

Section "Microsoft Excel add-in" install_addin

    SectionInstType RO
    # Approximate add-in size is 3MB
    AddSize 3072

    ${If} $PathToConfiguration != ""
        ExecWait '"$PathToAddInInstaller" "--path_to_up_to_date_configuration" "$PathToConfiguration"'
    ${Else}
        ExecWait '"$PathToAddInInstaller"'
    ${EndIf}

SectionEnd

SectionGroup /e "Services configuration"

Section "petstore" add_petstore_configuration

    SectionInstType RO
#    SectionInstType ${IT_FULL}

SectionEnd

Section "pyxelrest" add_pyxelrest_configuration

    SectionInstType RO
#    SectionInstType ${IT_FULL}

SectionEnd

SectionGroupEnd

SectionGroupEnd

Page Components
Page Directory
Page Custom optionsPageCreate optionsPageLeave
Page InstFiles
