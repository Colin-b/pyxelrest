!define VERSION "1.0.0"
Unicode True
Name "PyxelRest ${VERSION}"
BrandingText "Call REST APIs as functions"
RequestExecutionLevel "user"
OutFile "pyxelrest_installer-${VERSION}.exe"
InstallDir "$%APPDATA%\pyxelrest"

InstType "Full" IT_FULL
InstType "Minimal" IT_MIN

# To be able to use GetParent
!include TextFunc.nsh
# To be able to use NSD_*
!include nsDialogs.nsh

Var PathToPython
Var PathToPythonTextBox
Var BrowsePathToPythonButton
Var PythonWarningLabel
Var PythonDownloadLink
Var PythonStatusLabel

Var PathToConfiguration
Var PathToConfigurationTextBox
Var BrowsePathToConfigurationButton

Var PathToPythonFolder
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

    ${NSD_CreateLabel} 6u 30u 54% 12u "Python cannot be found. Change location or"
    pop $PythonWarningLabel
    SetCtlColors $PythonWarningLabel "ff0000" "transparent"

    ${NSD_CreateLink} 149u 30u 15% 12u "install it now"
    pop $PythonDownloadLink
    SetCtlColors $PythonDownloadLink "800000" "transparent"
    ${NSD_OnClick} $PythonDownloadLink downloadAndInstallPython

    ${NSD_CreateLabel} 6u 30u 70% 12u ""
    pop $PythonStatusLabel

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
        ShowWindow $PythonWarningLabel ${SW_SHOW}
        ShowWindow $PythonDownloadLink ${SW_SHOW}
        ShowWindow $PythonStatusLabel ${SW_HIDE}
        EnableWindow $NextButton 0
    ${Else}
        ShowWindow $PythonWarningLabel ${SW_HIDE}
        ShowWindow $PythonDownloadLink ${SW_HIDE}
        ShowWindow $PythonStatusLabel ${SW_HIDE}
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

Function downloadAndInstallPython

    # Hide the button to avoid double installation
    ShowWindow $PythonWarningLabel ${SW_HIDE}
    ShowWindow $PythonDownloadLink ${SW_HIDE}
    ${NSD_SetText} $PythonStatusLabel "Downloading python..."
    ShowWindow $PythonStatusLabel ${SW_SHOW}

    ${NSD_GetText} $PathToPythonTextBox $0
    ${GetParent} "$0" $0

    ${If} ${FileExists} "$%USERPROFILE%\python_for_pyxelrest.exe"
        Delete "$%USERPROFILE%\python_for_pyxelrest.exe"
    ${Else}
    # https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-transfer
    ExecWait '"bitsadmin.exe" "/transfer" "Download Python" "https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe" "$%USERPROFILE%\python_for_pyxelrest.exe"'

    ${IfNot} ${FileExists} "$%USERPROFILE%\python_for_pyxelrest.exe"
        ${NSD_SetText} $PythonStatusLabel "Python could not be downloaded."
    ${Else}
        ${NSD_SetText} $PythonStatusLabel "Installing python..."
        # Perform basic python (only what is required for pyxelrest), see https://docs.python.org/3/using/windows.html#installing-without-ui
        ExecWait '"$%USERPROFILE%\python_for_pyxelrest.exe" "/quiet" "TargetDir=$0" "Include_doc=0" "Include_launcher=0" "InstallLauncherAllUsers=0" "Include_test=0"'
        Delete "$%USERPROFILE%\python_for_pyxelrest.exe"
        # Update the UI once python is supposed to be installed
        Call changePathToPython
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

    ${GetParent} "$PathToPython" $PathToPythonFolder
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
    ${If} ${FileExists} "$INSTDIR\pyxelrest_venv"
        DetailPrint "Removing previous virtual environment"
        RMDir /r "$INSTDIR\pyxelrest_venv"
    ${EndIf}
    DetailPrint "Creating virtual environment"
    ExecWait '"$PathToPython" "-m" "venv" "$INSTDIR\pyxelrest_venv"'
	StrCpy $PathToScriptsFolder "$INSTDIR\pyxelrest_venv\Scripts"
	StrCpy $PathToPythonFolder "$INSTDIR\pyxelrest_venv\Scripts"
	WriteUninstaller "$INSTDIR\pyxelrest_uninstaller-${VERSION}.exe"

SectionEnd

Section "Python module" install_module

    SectionInstType RO
    # Approximate modules size is 37MB
    AddSize 37888
    DetailPrint "Installing pyxelrest python module"
    ExecWait '"$PathToPythonFolder\python.exe" "-m" "pip" "install" "pyxelrest==${VERSION}"' $0
    ${If} $0 != "0"
    	Abort "Python module could not be installed (returned $0). Open an issue in https://github.com/Colin-b/pyxelrest/issues/new"
    ${EndIf}

SectionEnd

SectionGroup "Additional features"

Section "Handle custom SSL certificates" handle_custom_ssl

    SectionInstType ${IT_FULL}
    # Approximate modules size is 650KB
    AddSize 650
    DetailPrint "Installing python-certifi-win32 python module"
    ExecWait '"$PathToPythonFolder\python.exe" "-m" "pip" "install" "python-certifi-win32==1.*"'

SectionEnd

Section "Handle Microsoft Windows authentication" handle_ms_auth

    SectionInstType ${IT_FULL}
    # Approximate modules size is 7MB
    AddSize 7189
    DetailPrint "Installing requests_ntlm and requests_negotiate_sspi python modules"
    ExecWait '"$PathToPythonFolder\python.exe" "-m" "pip" "install" "requests_ntlm==1.*" "requests_negotiate_sspi==0.5.*"'

SectionEnd

Section "Allow to cache requests results" allow_cached_results

    SectionInstType ${IT_FULL}
    # Approximate modules size is 150KB
    AddSize 150
    DetailPrint "Installing cachetools python module"
    ExecWait '"$PathToPythonFolder\python.exe" "-m" "pip" "install" "cachetools==4.*"'

SectionEnd

SectionGroupEnd

SectionGroupEnd

SectionGroup /e "Microsoft Excel"

Section "Microsoft Excel add-in" install_addin

    SectionInstType RO
    # Approximate add-in size is 3MB
    AddSize 3072

    ${IfNot} ${FileExists} "$PathToScriptsFolder\pyxelrest_install_addin.exe"
        Abort "The add-in installer cannot be located in $PathToScriptsFolder\pyxelrest_install_addin.exe. Open an issue in https://github.com/Colin-b/pyxelrest/issues/new"
    ${EndIf}

    DetailPrint "Installing Microsoft Excel add-in"
    ${If} $PathToConfiguration != ""
        ExecWait '"$PathToScriptsFolder\pyxelrest_install_addin.exe" "--path_to_up_to_date_configuration" "$PathToConfiguration"' $0
    ${Else}
        ExecWait '"$PathToScriptsFolder\pyxelrest_install_addin.exe"' $0
    ${EndIf}

    ${If} $0 != "0"
    	Abort "Microsoft Excel add-in could not be installed (returned $0). Open an issue in https://github.com/Colin-b/pyxelrest/issues/new"
    ${EndIf}

SectionEnd

SectionGroup /e "Services configuration"

Section "petstore" add_petstore_configuration

    SectionInstType ${IT_FULL}
    DetailPrint "Adding petstore service configuration"
    ExecWait '"$PathToScriptsFolder\pyxelrest_update_services_config.exe" "https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/samples/petstore.yml" "add"'

SectionEnd

Section "pyxelrest" add_pyxelrest_configuration

    SectionInstType ${IT_FULL}
    DetailPrint "Adding pyxelrest service configuration"
    ExecWait '"$PathToScriptsFolder\pyxelrest_update_services_config.exe" "https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/samples/pyxelrest.yml" "add"'

SectionEnd

SectionGroupEnd

SectionGroupEnd


Page Components
Page Directory
Page Custom optionsPageCreate optionsPageLeave
PageEx instfiles
    CompletedText "PyxelRest is now available to use within Microsoft Excel"
PageExEnd


Var AddInUninstallerPath

Section "Uninstall"

    SectionInstType RO
	StrCpy $AddInUninstallerPath "$%COMMONPROGRAMFILES%\microsoft shared\VSTO\10.0\VSTOInstaller.exe"

    ${IfNot} ${FileExists} "$AddInUninstallerPath"
	    StrCpy $AddInUninstallerPath "$%COMMONPROGRAMFILES(x86)%\microsoft shared\VSTO\10.0\VSTOInstaller.exe"
        ${IfNot} ${FileExists} "$AddInUninstallerPath"
            Abort "The add-in uninstaller cannot be located. Open an issue in https://github.com/Colin-b/pyxelrest/issues/new"
        ${EndIf}
    ${EndIf}

    ${If} ${FileExists} "$%APPDATA%\pyxelrest\excel_addin\PyxelRestAddIn.vsto"
        DetailPrint "Uninstalling Microsoft Excel add-in"
        ExecWait '"$AddInUninstallerPath" "/Uninstall" "$%APPDATA%\pyxelrest\excel_addin\PyxelRestAddIn.vsto"'
        ${If} $0 != ""
            Abort "Microsoft Excel add-in could not be uninstalled (returned $0). Open an issue in https://github.com/Colin-b/pyxelrest/issues/new"
        ${EndIf}
    ${EndIf}

    ${If} ${FileExists} "$%APPDATA%\pyxelrest\excel_addin"
        DetailPrint "Removing Microsoft Excel add-in folder"
        RMDir /r "$%APPDATA%\pyxelrest\excel_addin"
    ${EndIf}

    ${If} ${FileExists} "$%APPDATA%\Microsoft\Excel\XLSTART\pyxelrest.xlam"
        DetailPrint "Removing VBA add-in"
        Delete "$%APPDATA%\Microsoft\Excel\XLSTART\pyxelrest.xlam"
    ${EndIf}

    ${If} ${FileExists} "$INSTDIR\pyxelrest_venv"
        DetailPrint "Removing virtual environment"
        RMDir /r "$INSTDIR\pyxelrest_venv"
    ${EndIf}

    ${If} ${FileExists} "$INSTDIR"
        DetailPrint "Removing installation directory"
        RMDir /r "$INSTDIR"
    ${EndIf}

SectionEnd

PageEx un.instfiles
    CompletedText "PyxelRest is now uninstalled."
PageExEnd