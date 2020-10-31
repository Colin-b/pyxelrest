!define VERSION "1.0.0"
Unicode True
Name "PyxelRest ${VERSION}"
BrandingText "Call REST APIs as functions"
CompletedText "PyxelRest is now available to use within Microsoft Excel"
RequestExecutionLevel "user"
OutFile "pyxelrest_installer-${VERSION}.exe"
InstallDir "$%APPDATA%\pyxelrest"

InstType "Full" IT_FULL
InstType "Minimal" IT_MIN

!include TextFunc.nsh
!include nsDialogs.nsh

Var PathToPython
Var PathToPythonTextBox
Var BrowsePathToPythonButton
Var PythonWarningLabel
Var PythonDownloadLink

Var PathToConfiguration
Var PathToConfigurationTextBox
Var BrowsePathToConfigurationButton

Var PathToScriptsFolder
Var NextButton

Function .onInit

	StrCpy $PathToPython "$%USERPROFILE%\AppData\Local\Programs\Python\Python38\pythonw.exe"
	StrCpy $PathToConfiguration ""

FunctionEnd

Function optionsPageCreate
    nsDialogs::Create 1018

    ${NSD_CreateGroupBox} 0 0u 100% 45u "Python executable"
    Pop $0

    ${NSD_CreateText} 5u 15u 72% 12u "$PathToPython"
    Pop $PathToPythonTextBox
    ${NSD_OnChange} $PathToPythonTextBox changePathToPython

    ${NSD_CreateBrowseButton} 205u 13u 20% 15u "Browse..."
    pop $BrowsePathToPythonButton
    ${NSD_OnClick} $BrowsePathToPythonButton browsePathToPython

    ${NSD_CreateLabel} 6u 30u 54% 12u ""
    pop $PythonWarningLabel

    ${NSD_CreateLink} 150u 30u 40% 12u ""
    pop $PythonDownloadLink
    ${NSD_OnClick} $PythonDownloadLink downloadPython

    ${NSD_CreateGroupBox} 0 65u 100% 35u "Path to up to date services configurations"
    Pop $0

    ${NSD_CreateText} 5u 80u 72% 12u "$PathToConfiguration"
    Pop $PathToConfigurationTextBox

    ${NSD_CreateBrowseButton} 205u 78u 20% 15u "Browse..."
    pop $BrowsePathToConfigurationButton
    ${NSD_OnClick} $BrowsePathToConfigurationButton browsePathToConfiguration

    Call changePathToPython

    nsDialogs::Show
FunctionEnd

Function changePathToPython

    ${NSD_GetText} $PathToPythonTextBox $PathToPython
    GetDlgItem $NextButton $HWNDPARENT 1
    ${IfNot} ${FileExists} $PathToPython
        ${NSD_SetText} $PythonWarningLabel "Python cannot be found. Change location or"
        ${NSD_SetText} $PythonDownloadLink "install it now"
        EnableWindow $NextButton 0
    ${Else}
        ${NSD_SetText} $PythonWarningLabel "                                          "
        ${NSD_SetText} $PythonDownloadLink "                                          "
        EnableWindow $NextButton 1
    ${EndIf}

FunctionEnd

Function browsePathToPython

    ${NSD_GetText} $PathToPythonTextBox $0
    nsDialogs::SelectFileDialog open $0 "Python executable | pythonw.exe"
    Pop $0
    ${If} $0 != ""
        ${NSD_SetText} $PathToPythonTextBox $0
    ${EndIf}

FunctionEnd

Function downloadPython

    ${NSD_GetText} $PathToPythonTextBox $PathToPython
    ${IfNot} ${FileExists} $PathToPython
        ExecShell "open" "https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe"
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

    # If python path is in a virtual environment, python executable is in Scripts folder
    ${GetParent} "$PathToPython" $PathToScriptsFolder
    ${GetFileName} $PathToScriptsFolder $0

    # If python path is not in a virtual environment, python executable is at the same level of the Scripts folder
    ${If} $0 != "Scripts"
    	StrCpy $PathToScriptsFolder "$PathToScriptsFolder\Scripts"
    ${EndIf}

    ${NSD_GetText} $PathToConfigurationTextBox $PathToConfiguration

FunctionEnd

SectionGroup /e "Python"

Section "Virtual environment" install_venv

    SectionInstType ${IT_FULL}
    # Approximate venv size is 15MB
    AddSize 15360
    ExecWait '"$PathToPython" "-m" "venv" "$INSTDIR\pyxelrest_venv"'
	StrCpy $PathToPython "$INSTDIR\pyxelrest_venv\Scripts\python.exe"
	StrCpy $PathToScriptsFolder "$INSTDIR\pyxelrest_venv\Scripts"

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

    ${IfNot} ${FileExists} "$PathToScriptsFolder\pyxelrest_install_addin.exe"
        MessageBox mb_iconstop "The add-in installer cannot be located in $PathToScriptsFolder\pyxelrest_install_addin.exe. Open an issue in https://github.com/Colin-b/pyxelrest/issues/new"
        Abort
    ${EndIf}

    ${If} $PathToConfiguration != ""
        ExecWait '"$PathToScriptsFolder\pyxelrest_install_addin.exe" "--path_to_up_to_date_configuration" "$PathToConfiguration"'
    ${Else}
        ExecWait '"$PathToScriptsFolder\pyxelrest_install_addin.exe"'
    ${EndIf}

SectionEnd

SectionGroup /e "Services configuration"

Section "petstore" add_petstore_configuration

    SectionInstType ${IT_FULL}
    ExecWait '"$PathToScriptsFolder\pyxelrest_update_services_config.exe" "https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/samples/petstore.yml" "add"'

SectionEnd

Section "pyxelrest" add_pyxelrest_configuration

    SectionInstType ${IT_FULL}
    ExecWait '"$PathToScriptsFolder\pyxelrest_update_services_config.exe" "https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/samples/pyxelrest.yml" "add"'

SectionEnd

SectionGroupEnd

SectionGroupEnd

Page Components
Page Directory
Page Custom optionsPageCreate optionsPageLeave
Page InstFiles
