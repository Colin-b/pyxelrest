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
# To be able to use NSD_*, see nsis.sourceforge.io/Docs/nsDialogs/Readme.html
!include nsDialogs.nsh
# To be able to use ${WordFind}
!include "WordFunc.nsh"
# To be able to use ExecDos::exec, see https://nsis.sourceforge.io/ExecDos_plug-in
!addplugindir nsis

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
Var MicrosoftExcelIsRunning

Var AddInUninstallerPath

Function .onInit

    StrCpy $PathToPython "$%USERPROFILE%\AppData\Local\Programs\Python\Python38\python.exe"
    StrCpy $PathToConfiguration ""

FunctionEnd

Function checkMicrosoftExcelStatus

    Pop $0
    # see https://nsis.sourceforge.io/Docs/AppendixE.html#wordfind
    ${WordFind} "$0" "EXCEL.EXE " "E-1" $0
    ${If} $0 != "1"
        StrCpy $MicrosoftExcelIsRunning "1"
    ${Else}
        StrCpy $MicrosoftExcelIsRunning "0"
    ${EndIf}

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
    nsDialogs::SelectFileDialog open $0 "Python executable | python.exe"
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
    ${EndIf}
    # https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-transfer
    ExecDos::exec '"bitsadmin.exe" "/transfer" "Download Python" "https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe" "$%USERPROFILE%\python_for_pyxelrest.exe"'

    ${IfNot} ${FileExists} "$%USERPROFILE%\python_for_pyxelrest.exe"
        ${NSD_SetText} $PythonStatusLabel "Python could not be downloaded."
    ${Else}
        ${NSD_SetText} $PythonStatusLabel "Installing python..."
        # Perform basic python (only what is required for pyxelrest), see https://docs.python.org/3/using/windows.html#installing-without-ui
        ExecDos::exec '"$%USERPROFILE%\python_for_pyxelrest.exe" "/quiet" "TargetDir=$0" "Include_doc=0" "Include_launcher=0" "InstallLauncherAllUsers=0" "Include_test=0"'
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

Function registerUninstaller

    WriteUninstaller "$INSTDIR\pyxelrest_uninstaller-${VERSION}.exe"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest" "DisplayName" "PyxelRest"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest" "UninstallString" '"$INSTDIR\pyxelrest_uninstaller-${VERSION}.exe"'
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest" "InstallLocation" '"$INSTDIR"'
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest" "Publisher" "Bounouar Colin"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest" "HelpLink" "https://github.com/Colin-b/pyxelrest/"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest" "URLUpdateInfo" "https://github.com/Colin-b/pyxelrest/"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest" "URLInfoAbout" "https://github.com/Colin-b/pyxelrest/"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest" "DisplayVersion" "${VERSION}"

FunctionEnd

Section # Ensure Microsoft Excel is closed

    GetFunctionAddress $R2 checkMicrosoftExcelStatus
    ExecDos::exec /TOFUNC 'tasklist /FI "IMAGENAME eq EXCEL.EXE"' "" $R2
    Pop $0
    ${If} $0 != "0"
        DetailPrint "Unable to ensure that Microsoft Excel is closed ($0). Continue anyway..."
    ${ElseIf} $MicrosoftExcelIsRunning != "0"
        Abort "Microsoft Excel is running. Close it and try again."
    ${Else}
        DetailPrint "Microsoft Excel is closed."
    ${EndIf}

SectionEnd

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
    ExecDos::exec /DETAILED '"$PathToPython" "-m" "venv" "$INSTDIR\pyxelrest_venv"'
    Pop $0
    ${If} $0 != "0"
    	Abort "Virtual environment could not be created (returned $0). Open an issue in https://github.com/Colin-b/pyxelrest/issues/new"
    ${EndIf}
    StrCpy $PathToScriptsFolder "$INSTDIR\pyxelrest_venv\Scripts"
    StrCpy $PathToPythonFolder "$INSTDIR\pyxelrest_venv\Scripts"

SectionEnd

Section "Python module" install_module

    SectionInstType RO
    # Approximate modules size is 37MB
    AddSize 37888
    Call registerUninstaller
    DetailPrint "Installing pyxelrest python module"
    ExecDos::exec /DETAILED '"$PathToPythonFolder\python.exe" "-m" "pip" "install" "pyxelrest==${VERSION}" "--disable-pip-version-check" "--verbose"'
    Pop $0
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
    ExecDos::exec /DETAILED '"$PathToPythonFolder\python.exe" "-m" "pip" "install" "python-certifi-win32==1.*" "--disable-pip-version-check"'

SectionEnd

Section "Handle Microsoft Windows authentication" handle_ms_auth

    SectionInstType ${IT_FULL}
    # Approximate modules size is 7MB
    AddSize 7189
    DetailPrint "Installing requests_ntlm and requests_negotiate_sspi python modules"
    ExecDos::exec /DETAILED '"$PathToPythonFolder\python.exe" "-m" "pip" "install" "requests_ntlm==1.*" "requests_negotiate_sspi==0.5.*" "--disable-pip-version-check"'

SectionEnd

Section "Allow to cache requests results" allow_cached_results

    SectionInstType ${IT_FULL}
    # Approximate modules size is 150KB
    AddSize 150
    DetailPrint "Installing cachetools python module"
    ExecDos::exec /DETAILED '"$PathToPythonFolder\python.exe" "-m" "pip" "install" "cachetools==4.*" "--disable-pip-version-check"'

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
        ExecDos::exec /DETAILED '"$PathToScriptsFolder\pyxelrest_install_addin.exe" "--destination" "$INSTDIR" "--path_to_up_to_date_configuration" "$PathToConfiguration"'
    ${Else}
        ExecDos::exec /DETAILED '"$PathToScriptsFolder\pyxelrest_install_addin.exe" "--destination" "$INSTDIR"'
    ${EndIf}

    Pop $0
    ${If} $0 != "0"
    	Abort "Microsoft Excel add-in could not be installed (returned $0). Open an issue in https://github.com/Colin-b/pyxelrest/issues/new"
    ${EndIf}

SectionEnd

SectionGroup /e "Services configuration"

Section "petstore" add_petstore_configuration

    SectionInstType ${IT_FULL}
    DetailPrint "Adding petstore service configuration"
    ExecDos::exec /DETAILED '"$PathToScriptsFolder\pyxelrest_update_services_config.exe" "https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/samples/petstore.yml" "add"'

SectionEnd

Section "pyxelrest" add_pyxelrest_configuration

    SectionInstType ${IT_FULL}
    DetailPrint "Adding pyxelrest service configuration"
    ExecDos::exec /DETAILED '"$PathToScriptsFolder\pyxelrest_update_services_config.exe" "https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/samples/pyxelrest.yml" "add"'

SectionEnd

SectionGroupEnd

SectionGroupEnd

Function .onInstFailed

    ${If} ${FileExists} "$INSTDIR\excel_addin\PyxelRestAddIn.vsto"

        StrCpy $AddInUninstallerPath "$%COMMONPROGRAMFILES%\microsoft shared\VSTO\10.0\VSTOInstaller.exe"

        ${IfNot} ${FileExists} "$AddInUninstallerPath"
            StrCpy $AddInUninstallerPath "$%COMMONPROGRAMFILES(x86)%\microsoft shared\VSTO\10.0\VSTOInstaller.exe"
        ${EndIf}

        ${If} ${FileExists} "$AddInUninstallerPath"
            DetailPrint "Uninstalling Microsoft Excel add-in"
            ExecWait '"$AddInUninstallerPath" "/Silent" "/Uninstall" "$INSTDIR\excel_addin\PyxelRestAddIn.vsto"' $0
            ${If} $0 != "0"
                ExecWait '"$AddInUninstallerPath" "/Uninstall" "$INSTDIR\excel_addin\PyxelRestAddIn.vsto"' $0
                ${If} $0 != "0"
                    DetailPrint "Microsoft Excel add-in could not be uninstalled (returned $0). Open an issue in https://github.com/Colin-b/pyxelrest/issues/new"
                ${EndIf}
            ${EndIf}
        ${EndIf}
    ${EndIf}

    ${If} ${FileExists} "$INSTDIR\excel_addin"
        DetailPrint "Removing Microsoft Excel add-in folder"
        RMDir /r "$INSTDIR\excel_addin"
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

    DeleteRegKey HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest"

FunctionEnd


Page Components
Page Directory
Page Custom optionsPageCreate optionsPageLeave
PageEx instfiles
    CompletedText "PyxelRest is now available to use within Microsoft Excel"
PageExEnd

Function un.checkMicrosoftExcelStatus

    Pop $0
    # see https://nsis.sourceforge.io/Docs/AppendixE.html#wordfind
    ${WordFind} "$0" "EXCEL.EXE " "E-1" $0
    ${If} $0 != "1"
        StrCpy $MicrosoftExcelIsRunning "1"
    ${Else}
        StrCpy $MicrosoftExcelIsRunning "0"
    ${EndIf}

FunctionEnd

Section "un.ensure_excel_is_closed"

    SectionInstType RO

    GetFunctionAddress $R2 un.checkMicrosoftExcelStatus
    ExecDos::exec /TOFUNC 'tasklist /FI "IMAGENAME eq EXCEL.EXE"' "" $R2
    Pop $0
    ${If} $0 != "0"
        DetailPrint "Unable to ensure that Microsoft Excel is closed ($0). Continue anyway..."
    ${ElseIf} $MicrosoftExcelIsRunning != "0"
        Abort "Microsoft Excel is running. Close it and try again."
    ${Else}
        DetailPrint "Microsoft Excel is closed."
    ${EndIf}

SectionEnd

Section "Uninstall"

    SectionInstType RO

    ${If} ${FileExists} "$INSTDIR\excel_addin\PyxelRestAddIn.vsto"

        StrCpy $AddInUninstallerPath "$%COMMONPROGRAMFILES%\microsoft shared\VSTO\10.0\VSTOInstaller.exe"

        ${IfNot} ${FileExists} "$AddInUninstallerPath"
            StrCpy $AddInUninstallerPath "$%COMMONPROGRAMFILES(x86)%\microsoft shared\VSTO\10.0\VSTOInstaller.exe"
            ${IfNot} ${FileExists} "$AddInUninstallerPath"
                Abort "The add-in uninstaller cannot be located. Open an issue in https://github.com/Colin-b/pyxelrest/issues/new"
            ${EndIf}
        ${EndIf}

        DetailPrint "Uninstalling Microsoft Excel add-in"
        ExecWait '"$AddInUninstallerPath" "/Silent" "/Uninstall" "$INSTDIR\excel_addin\PyxelRestAddIn.vsto"' $0
        ${If} $0 != "0"
            ExecWait '"$AddInUninstallerPath" "/Uninstall" "$INSTDIR\excel_addin\PyxelRestAddIn.vsto"' $0
            ${If} $0 != "0"
                Abort "Microsoft Excel add-in could not be uninstalled (returned $0). Open an issue in https://github.com/Colin-b/pyxelrest/issues/new"
            ${EndIf}
        ${EndIf}
    ${EndIf}

    ${If} ${FileExists} "$INSTDIR\excel_addin"
        DetailPrint "Removing Microsoft Excel add-in folder"
        RMDir /r "$INSTDIR\excel_addin"
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

    DeleteRegKey HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest"

SectionEnd

PageEx un.instfiles
    CompletedText "PyxelRest is now uninstalled."
PageExEnd