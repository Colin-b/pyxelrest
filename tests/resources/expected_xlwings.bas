Attribute VB_Name = "xlwings"
#Const App = "Microsoft Excel" 'Adjust when using outside of Excel
'Version: 0.28.9

'xlwings is distributed under a BSD 3-clause license.
'
'Copyright (C) 2014-present, Zoomer Analytics LLC.
'All rights reserved.
'
'Redistribution and use in source and binary forms, with or without modification,
'are permitted provided that the following conditions are met:
'
'* Redistributions of source code must retain the above copyright notice, this
'  list of conditions and the following disclaimer.
'
'* Redistributions in binary form must reproduce the above copyright notice, this
'  list of conditions and the following disclaimer in the documentation and/or
'  other materials provided with the distribution.
'
'* Neither the name of the copyright holder nor the names of its
'  contributors may be used to endorse or promote products derived from
'  this software without specific prior written permission.
'
'THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
'ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
'WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
'DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
'ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
'(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
'LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
'ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
'(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
'SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'Attribute VB_Name = "Main"



#If VBA7 Then
    #If Mac Then
        Private Declare PtrSafe Function system Lib "libc.dylib" (ByVal Command As String) As Long
    #End If
    #If Win64 Then
        Const XLPyDLLName As String = "xlwings64-0.28.9.dll"
        Declare PtrSafe Function XLPyDLLActivateAuto Lib "xlwings64-0.28.9.dll" (ByRef Result As Variant, Optional ByVal Config As String = "", Optional ByVal mode As Long = 1) As Long
        Declare PtrSafe Function XLPyDLLNDims Lib "xlwings64-0.28.9.dll" (ByRef src As Variant, ByRef dims As Long, ByRef transpose As Boolean, ByRef dest As Variant) As Long
        Declare PtrSafe Function XLPyDLLVersion Lib "xlwings64-0.28.9.dll" (tag As String, VERSION As Double, arch As String) As Long
    #Else
        Private Const XLPyDLLName As String = "xlwings32-0.28.9.dll"
        Declare PtrSafe Function XLPyDLLActivateAuto Lib "xlwings32-0.28.9.dll" (ByRef Result As Variant, Optional ByVal Config As String = "", Optional ByVal mode As Long = 1) As Long
        Private Declare PtrSafe Function XLPyDLLNDims Lib "xlwings32-0.28.9.dll" (ByRef src As Variant, ByRef dims As Long, ByRef transpose As Boolean, ByRef dest As Variant) As Long
        Private Declare PtrSafe Function XLPyDLLVersion Lib "xlwings32-0.28.9.dll" (tag As String, VERSION As Double, arch As String) As Long
    #End If
    Private Declare PtrSafe Function LoadLibrary Lib "KERNEL32" Alias "LoadLibraryA" (ByVal lpLibFileName As String) As Long
#Else
    #If Mac Then
        Private Declare Function system Lib "libc.dylib" (ByVal Command As String) As Long
    #End If
    Private Const XLPyDLLName As String = "xlwings32-0.28.9.dll"
    Private Declare Function XLPyDLLActivateAuto Lib "xlwings32-0.28.9.dll" (ByRef Result As Variant, Optional ByVal Config As String = "", Optional ByVal mode As Long = 1) As Long
    Private Declare Function XLPyDLLNDims Lib "xlwings32-0.28.9.dll" (ByRef src As Variant, ByRef dims As Long, ByRef transpose As Boolean, ByRef dest As Variant) As Long
    Private Declare Function LoadLibrary Lib "KERNEL32" Alias "LoadLibraryA" (ByVal lpLibFileName As String) As Long
    Declare Function XLPyDLLVersion Lib "xlwings32-0.28.9.dll" (tag As String, VERSION As Double, arch As String) As Long
#End If

Public Const XLWINGS_VERSION As String = "0.28.9"
Public Const PROJECT_NAME As String = "xlwings"

Public Function RunPython(PythonCommand As String)
    ' Public API: Runs the Python command, e.g.: to run the function foo() in module bar, call the function like this:
    ' RunPython "import bar; bar.foo()"
    
    Dim i As Integer
    Dim SourcePythonCommand As String, interpreter As String, PYTHONPATH As String, licenseKey, ActiveFullName As String, ThisFullName As String, AddExcelDir As String
    Dim OPTIMIZED_CONNECTION As Boolean, uses_embedded_code As Boolean
    Dim wb As Workbook
    Dim sht As Worksheet
    
    SourcePythonCommand = PythonCommand
    
    #If Mac Then
        interpreter = GetConfig("INTERPRETER_MAC", "")
    #Else
        interpreter = GetConfig("INTERPRETER_WIN", "")
    #End If
    If interpreter = "" Then
        ' Legacy
        interpreter = GetConfig("INTERPRETER", "python")
    End If

    ' Check for embedded Python code
    uses_embedded_code = False
    For i = 1 To 2
        If i = 1 Then
            Set wb = ActiveWorkbook
        Else
            Set wb = ActiveWorkbook
        End If
        For Each sht In wb.Worksheets
            If Right$(sht.Name, 3) = ".py" Then
                uses_embedded_code = True
                Exit For
            End If
        Next
    Next i

    If uses_embedded_code = True Then
        AddExcelDir = "false"
    Else
        AddExcelDir = GetConfig("ADD_WORKBOOK_TO_PYTHONPATH", "true")
    End If

    ' The first 5 args are not technically part of the PYTHONPATH, but it's just easier to add it here (used by xlwings.utils.prepare_sys_path)
    #If Mac Then
        If InStr(ActiveWorkbook.FullName, "://") = 0 Then
            ActiveFullName = ToPosixPath(ActiveWorkbook.FullName)
            ThisFullName = ToPosixPath(ActiveWorkbook.FullName)
        Else
            ActiveFullName = ActiveWorkbook.FullName
            ThisFullName = ActiveWorkbook.FullName
        End If
    #Else
        ActiveFullName = ActiveWorkbook.FullName
        ThisFullName = ActiveWorkbook.FullName
    #End If
    
    #If Mac Then
        PYTHONPATH = AddExcelDir & ";" & ActiveFullName & ";" & ThisFullName & ";" & GetConfig("ONEDRIVE_CONSUMER_MAC") & ";" & GetConfig("ONEDRIVE_COMMERCIAL_MAC") & ";" & GetConfig("SHAREPOINT_MAC") & ";" & GetConfig("PYTHONPATH")
    #Else
        PYTHONPATH = AddExcelDir & ";" & ActiveFullName & ";" & ThisFullName & ";" & GetConfig("ONEDRIVE_CONSUMER_WIN") & ";" & GetConfig("ONEDRIVE_COMMERCIAL_WIN") & ";" & GetConfig("SHAREPOINT_WIN") & ";" & GetConfig("PYTHONPATH")
    #End If

    OPTIMIZED_CONNECTION = GetConfig("USE UDF SERVER", False)

    ' PythonCommand with embedded code
    If uses_embedded_code = True Then
        licenseKey = GetConfig("LICENSE_KEY")
        If licenseKey = "" Then
            MsgBox "Embedded code requires a valid LICENSE_KEY."
            Exit Function
        Else
            PythonCommand = "import xlwings.pro;xlwings.pro.runpython_embedded_code('" & SourcePythonCommand & "')"
        End If
    End If

    ' Handle module execute permission (for embedded code that happens in Python)
    If LCase(GetConfig("PERMISSION_CHECK_ENABLED", , source:="user")) = "true" And uses_embedded_code = False Then
        PythonCommand = "import xlwings.pro;xlwings.pro.verify_execute_permission('" & SourcePythonCommand & "');" & PythonCommand
    End If

    ' Call Python platform-dependent
    #If Mac Then
        Application.StatusBar = "Running..."  ' Non-blocking way of giving feedback that something is happening
        ExecuteMac PythonCommand, interpreter, PYTHONPATH
    #Else
        If OPTIMIZED_CONNECTION = True Then
            Py.SetAttr Py.Module("xlwings._xlwindows"), "BOOK_CALLER", ActiveWorkbook
            
            On Error GoTo err_handling
            
            Py.Exec "" & PythonCommand & ""
            GoTo end_err_handling
err_handling:
            ShowError "", Err.Description
            RunPython = -1
            On Error GoTo 0
end_err_handling:
        Else
            RunPython = ExecuteWindows(False, PythonCommand, interpreter, PYTHONPATH)
        End If
    #End If
End Function


Sub ExecuteMac(PythonCommand As String, PYTHON_MAC As String, Optional PYTHONPATH As String)
    #If Mac Then
    Dim PythonInterpreter As String, RunCommand As String, Log As String
    Dim ParameterString As String, ExitCode As String, CondaCmd As String, CondaPath As String, CondaEnv As String, LOG_FILE As String

    ' Transform paths
    PYTHONPATH = Replace(PYTHONPATH, "'", "\'") ' Escaping quotes

    If PYTHON_MAC <> "" Then
        If PYTHON_MAC <> "python" And PYTHON_MAC <> "pythonw" Then
            PythonInterpreter = ToPosixPath(PYTHON_MAC)
        Else
            PythonInterpreter = PYTHON_MAC
        End If
    Else
        PythonInterpreter = "python"
    End If

    ' Sandbox location that requires no file access confirmation
    ' TODO: Use same logic with GUID like for Windows. Only here the GUID will need to be passed back to CleanUp()
    LOG_FILE = Environ("HOME") + "/xlwings.log" '/Users/<User>/Library/Containers/com.microsoft.Excel/Data/xlwings.log

    ' Delete Log file just to make sure we don't show an old error
    On Error Resume Next
        Kill LOG_FILE
    On Error GoTo 0

    ' ParameterSting with all paramters (AppleScriptTask only accepts a single parameter)
    ParameterString = PYTHONPATH + ";"
    ParameterString = ParameterString + "|" + PythonInterpreter
    ParameterString = ParameterString + "|" + PythonCommand
    ParameterString = ParameterString + "|" + ActiveWorkbook.Name
    ParameterString = ParameterString + "|" + Left(Application.Path, Len(Application.Path) - 4)
    ParameterString = ParameterString + "|" + LOG_FILE

    On Error GoTo AppleScriptErrorHandler
        ExitCode = AppleScriptTask("xlwings-" & XLWINGS_VERSION & ".applescript", "VbaHandler", ParameterString)
    On Error GoTo 0

    ' If there's a log at this point (normally that will be from the shell only, not Python) show it and reset the StatusBar
    On Error Resume Next
        Log = ReadFile(LOG_FILE)
        If Log = "" Then
            Exit Sub
        Else
            ShowError (LOG_FILE)
            Application.StatusBar = False
        End If
        Exit Sub
    On Error GoTo 0

AppleScriptErrorHandler:
    MsgBox "To enable RunPython, please run 'xlwings runpython install' in a terminal once and try again.", vbCritical
    #End If
End Sub

Function ExecuteWindows(IsFrozen As Boolean, PythonCommand As String, PYTHON_WIN As String, _
                        Optional PYTHONPATH As String, Optional FrozenArgs As String) As Integer
    ' Call a command window and change to the directory of the Python installation or frozen executable
    ' Note: If Python is called from a different directory with the fully qualified path, pywintypesXX.dll won't be found.
    ' This seems to be a general issue with pywin32, see http://stackoverflow.com/q/7238403/918626
    Dim ShowConsole As Integer
    Dim TempDir As String
    If GetConfig("SHOW CONSOLE", False) = True Then
        ShowConsole = 1
    Else
        ShowConsole = 0
    End If

    Dim WaitOnReturn As Boolean: WaitOnReturn = True
    Dim WindowStyle As Integer: WindowStyle = ShowConsole
    Dim DriveCommand As String, RunCommand, condaExcecutable As String
    Dim PythonInterpreter As String, PythonDir As String, CondaCmd As String, CondaPath As String, CondaEnv As String
    Dim ExitCode As Long
    Dim LOG_FILE As String
    
    TempDir = GetConfig("TEMP DIR", Environ("Temp")) 'undocumented setting
    
    LOG_FILE = TempDir & "\xlwings-" & CreateGUID() & ".log"

    If Not IsFrozen And (PYTHON_WIN <> "python" And PYTHON_WIN <> "pythonw") Then
        If FileExists(PYTHON_WIN) Then
            PythonDir = ParentFolder(PYTHON_WIN)
        Else
            MsgBox "Could not find Interpreter!", vbCritical
            Exit Function
        End If
    Else
        PythonDir = ""  ' TODO: hack
    End If

    If Left$(PYTHON_WIN, 2) Like "[A-Za-z]:" Then
        ' If Python is installed on a mapped or local drive, change to drive, then cd to path
        DriveCommand = Left$(PYTHON_WIN, 2) & " & cd """ & PythonDir & """ & "
    ElseIf Left$(PYTHON_WIN, 2) = "\\" Then
        ' If Python is installed on a UNC path, temporarily mount and activate a drive letter with pushd
        DriveCommand = "pushd """ & PythonDir & """ & "
    End If

    ' Run Python with the "-c" command line switch: add the path of the python file and run the
    ' Command as first argument, then provide the Name and "from_xl" as 2nd and 3rd arguments.
    ' Then redirect stderr to the LOG_FILE and wait for the call to return.

    If PYTHON_WIN <> "python" And PYTHON_WIN <> "pythonw" Then
        PythonInterpreter = Chr(34) & PYTHON_WIN & Chr(34)
    Else
        PythonInterpreter = "python"
    End If

    CondaPath = GetConfig("CONDA PATH")
    CondaEnv = GetConfig("CONDA ENV")
    
    ' Handle spaces in path (for UDFs, this is handled via nested quotes instead, see XLPyCommand)
    CondaPath = Replace(CondaPath, " ", "^ ")
    
    ' Handle ampersands and backslashes in file paths
    PYTHONPATH = Replace(PYTHONPATH, "&", "^&")
    PYTHONPATH = Replace(PYTHONPATH, "\", "\\")
    
    If CondaPath <> "" And CondaEnv <> "" Then
        If CheckConda(CondaPath) = False Then
            Exit Function
        End If
        CondaCmd = CondaPath & "\condabin\conda activate " & CondaEnv & " && "
    Else
        CondaCmd = ""
    End If

    If IsFrozen = False Then
        RunCommand = CondaCmd & PythonInterpreter & " -B -c ""import xlwings.utils;xlwings.utils.prepare_sys_path(\""" & PYTHONPATH & "\""); " & PythonCommand & """ "
    ElseIf IsFrozen = True Then
        RunCommand = Chr(34) & PythonCommand & Chr(34) & " " & FrozenArgs & " "
    End If
    
    ExitCode = WScript.Run("cmd.exe /C " & DriveCommand & _
                       RunCommand & _
                       " --wb=" & """" & ActiveWorkbook.Name & """ --from_xl=1" & " --app=" & Chr(34) & _
                       Application.Path & "\" & Application.Name & Chr(34) & " --hwnd=" & Chr(34) & Application.Hwnd & Chr(34) & _
                       " 2> """ & LOG_FILE & """ ", _
                       WindowStyle, WaitOnReturn)

    'If ExitCode <> 0 then there's something wrong
    If ExitCode <> 0 Then
        Call ShowError(LOG_FILE)
        ExecuteWindows = -1
    End If

    ' Delete file after the error message has been shown
    On Error Resume Next
        Kill LOG_FILE
    On Error GoTo 0
End Function

Public Function RunFrozenPython(Executable As String, Optional Args As String)
    ' Runs a Python executable that has been frozen by PyInstaller and the like. Call the function like this:
    ' RunFrozenPython "C:\path\to\frozen_executable.exe", "arg1 arg2". Currently not implemented for Mac.

    ' Call Python
    #If Mac Then
        MsgBox "This functionality is not yet supported on Mac." & vbNewLine & _
               "Please run your scripts directly in Python!", vbCritical + vbOKOnly, "Unsupported Feature"
    #Else
        ExecuteWindows True, Executable, ParentFolder(Executable), , Args
    #End If
End Function

#If App = "Microsoft Excel" Then
Function GetUdfModules(Optional wb As Workbook) As String
#Else
Function GetUdfModules(Optional wb As Variant) As String
#End If
    Dim i As Integer
    Dim UDF_MODULES As String
    Dim sht As Worksheet

    GetUdfModules = GetConfig("UDF MODULES")
    ' Remove trailing ";"
    If Right$(GetUdfModules, 1) = ";" Then
        GetUdfModules = Left$(GetUdfModules, Len(GetUdfModules) - 1)
    End If
    
    ' Automatically add embedded code sheets
    For Each sht In wb.Worksheets
        If Right$(sht.Name, 3) = ".py" Then
            If GetUdfModules = "" Then
                GetUdfModules = Left$(sht.Name, Len(sht.Name) - 3)
            Else
                GetUdfModules = GetUdfModules & ";" & Left$(sht.Name, Len(sht.Name) - 3)
            End If
        End If
    Next

    ' Default
    If GetUdfModules = "" Then
        GetUdfModules = Left$(wb.Name, Len(wb.Name) - 5) ' assume that it ends in .xls*
    End If
    
End Function

Private Sub CleanUp()
    'On Mac only, this function is being called after Python is done (using Python's atexit handler)
    Dim LOG_FILE As String

    #If MAC_OFFICE_VERSION >= 15 Then
        LOG_FILE = Environ("HOME") + "/xlwings.log" '~/Library/Containers/com.microsoft.Excel/Data/xlwings.log
    #Else
        LOG_FILE = "/tmp/xlwings.log"
    #End If

    'Show the LOG_FILE as MsgBox if not empty
    On Error Resume Next
    If ReadFile(LOG_FILE) <> "" Then
        Call ShowError(LOG_FILE)
    End If
    On Error GoTo 0

    'Clean up
    Application.StatusBar = False
    Application.ScreenUpdating = True
    On Error Resume Next
        #If MAC_OFFICE_VERSION >= 15 Then
            Kill LOG_FILE
        #Else
            KillFileOnMac ToMacPath(ToPosixPath(LOG_FILE))
        #End If
    On Error GoTo 0
End Sub

Function XLPyCommand()
    'TODO: the whole python vs. pythonw should be obsolete now that the console is shown/hidden by the dll
    Dim PYTHON_WIN As String, PYTHONPATH As String, LOG_FILE As String, tail As String, licenseKey As String, LicenseKeyEnvString As String, AddExcelDir As String
    Dim CondaCmd As String, CondaPath As String, CondaEnv As String, ConsoleSwitch As String, FName As String

    Dim DEBUG_UDFS As Boolean
    #If App = "Microsoft Excel" Then
    Dim wb As Workbook
    #End If

    ' TODO: Doesn't automatically check if code is embedded
    AddExcelDir = GetConfig("ADD_WORKBOOK_TO_PYTHONPATH", "true")

    ' The first 6 args are not technically part of the PYTHONPATH, but it's just easier to add it here (used by xlwings.utils.prepare_sys_path)
    #If App = "Microsoft Excel" Then
        PYTHONPATH = AddExcelDir & ";" & ActiveWorkbook.FullName & ";" & ActiveWorkbook.FullName & ";" & GetConfig("ONEDRIVE_CONSUMER_WIN") & ";" & GetConfig("ONEDRIVE_COMMERCIAL_WIN") & ";" & GetConfig("SHAREPOINT_WIN") & ";" & GetConfig("PYTHONPATH")
    #Else
        ' Other office apps
        #If App = "Microsoft Word" Then
            FName = ThisDocument.FullName
        #ElseIf App = "Microsoft Access" Then
            FName = CurrentProject.FullName
        #ElseIf App = "Microsoft PowerPoint" Then
            FName = ActivePresentation.FullName
        #End If
        PYTHONPATH = FName & ";" & ";" & GetConfig("ONEDRIVE_CONSUMER_WIN") & ";" & GetConfig("ONEDRIVE_COMMERCIAL_WIN") & ";" & GetConfig("SHAREPOINT_WIN") & ";" & GetConfig("PYTHONPATH")
    #End If

    ' Escaping backslashes and quotes
    PYTHONPATH = Replace(PYTHONPATH, "\", "\\")
    PYTHONPATH = Replace(PYTHONPATH, "'", "\'")
    PYTHONPATH = Replace(PYTHONPATH, "&", "^&")
    
    PYTHON_WIN = GetConfig("INTERPRETER_WIN", "")
    If PYTHON_WIN = "" Then
        ' Legacy
        PYTHON_WIN = GetConfig("INTERPRETER", "pythonw")
    End If
    DEBUG_UDFS = GetConfig("DEBUG UDFS", False)

    ' /showconsole is a fictitious command line switch that's ignored by cmd.exe but used by CreateProcessA in the dll
    ' It's the only setting that's sent over like this at the moment
    If GetConfig("SHOW CONSOLE", False) = True Then
        ConsoleSwitch = "/showconsole"
    Else
        ConsoleSwitch = ""
    End If

    CondaPath = GetConfig("CONDA PATH")
    CondaEnv = GetConfig("CONDA ENV")

    If (PYTHON_WIN = "python" Or PYTHON_WIN = "pythonw") And (CondaPath <> "" And CondaEnv <> "") Then
        CondaCmd = Chr(34) & Chr(34) & CondaPath & "\condabin\conda" & Chr(34) & " activate " & CondaEnv & " && "
        PYTHON_WIN = "cmd.exe " & ConsoleSwitch & " /K " & CondaCmd & "python"
    Else
        PYTHON_WIN = "cmd.exe " & ConsoleSwitch & " /K " & Chr(34) & Chr(34) & PYTHON_WIN & Chr(34)
    End If

    licenseKey = GetConfig("LICENSE_KEY", "")
    If licenseKey <> "" Then
        LicenseKeyEnvString = "os.environ['XLWINGS_LICENSE_KEY']='" & licenseKey & "';"
    Else
        LicenseKeyEnvString = ""
    End If

    If DEBUG_UDFS = True Then
        XLPyCommand = "{506e67c3-55b5-48c3-a035-eed5deea7d6d}"
    Else
        ' Spaces in path of python.exe require quote around path AND quotes around whole command, see:
        ' https://stackoverflow.com/questions/6376113/how-do-i-use-spaces-in-the-command-prompt
        tail = " -B -c ""import sys, os;" & LicenseKeyEnvString & "import xlwings.utils;xlwings.utils.prepare_sys_path(\""" & PYTHONPATH & "\"");import xlwings.server; xlwings.server.serve('$(CLSID)')"""
        XLPyCommand = PYTHON_WIN & tail & Chr(34)
    End If
End Function

Private Sub XLPyLoadDLL()
    Dim PYTHON_WIN As String, CondaCmd As String, CondaPath As String, CondaEnv As String

    PYTHON_WIN = GetConfig("INTERPRETER_WIN", "")
    If PYTHON_WIN = "" Then
        ' Legacy
        PYTHON_WIN = GetConfig("INTERPRETER", "pythonw")
    End If
    CondaPath = GetConfig("CONDA PATH")
    CondaEnv = GetConfig("CONDA ENV")

    If (PYTHON_WIN = "python" Or PYTHON_WIN = "pythonw") And (CondaPath <> "" And CondaEnv <> "") Then
        ' This only works if the envs are in their default location
        ' Otherwise you'll have to add the full path for the interpreter in addition to the conda infos
        If CondaEnv = "base" Then
            PYTHON_WIN = CondaPath & "\" & PYTHON_WIN
        Else
            PYTHON_WIN = CondaPath & "\envs\" & CondaEnv & "\" & PYTHON_WIN
        End If
    End If

    If (PYTHON_WIN <> "python" And PYTHON_WIN <> "pythonw") Or (CondaPath <> "" And CondaEnv <> "") Then
        If LoadLibrary(ParentFolder(PYTHON_WIN) + "\" + XLPyDLLName) = 0 Then  ' Standard installation
            If LoadLibrary(ParentFolder(ParentFolder(PYTHON_WIN)) + "\" + XLPyDLLName) = 0 Then  ' Virtualenv
                Err.Raise 1, Description:= _
                    "Could not load " + XLPyDLLName + " from either of the following folders: " _
                    + vbCrLf + ParentFolder(PYTHON_WIN) _
                    + vbCrLf + ", " + ParentFolder(ParentFolder(PYTHON_WIN))
            End If
        End If
    End If
End Sub

Function NDims(ByRef src As Variant, dims As Long, Optional transpose As Boolean = False)
    XLPyLoadDLL
    If 0 <> XLPyDLLNDims(src, dims, transpose, NDims) Then Err.Raise 1001, Description:=NDims
End Function

Function Py()
    XLPyLoadDLL
    If 0 <> XLPyDLLActivateAuto(Py, XLPyCommand, 1) Then Err.Raise 1000, Description:=Py
End Function

Sub KillPy()
    XLPyLoadDLL
    Dim unused
    If 0 <> XLPyDLLActivateAuto(unused, XLPyCommand, -1) Then Err.Raise 1000, Description:=unused
End Sub

Sub ImportPythonUDFsBase(Optional addin As Boolean = False)
    ' This is called from the Ribbon button
    Dim tempPath As String, errorMsg As String
    Dim wb As Workbook

    If GetConfig("CONDA PATH") <> "" And CheckConda(GetConfig("CONDA PATH")) = False Then
        Exit Sub
    End If

    If addin = True Then
        Set wb = ThisWorkbook
    Else
        Set wb = ThisWorkbook
    End If

    On Error GoTo ImportError
        tempPath = Py.Str(Py.Call(Py.Module("xlwings"), "import_udfs", Py.Tuple(GetUdfModules(wb), wb)))
    Exit Sub
ImportError:
    errorMsg = Err.Description & " " & Err.Number
    ShowError "", errorMsg
End Sub

Sub ImportPythonUDFs()
    ImportPythonUDFsBase
End Sub

Sub ImportPythonUDFsToAddin()
    ImportPythonUDFsBase addin:=True
End Sub

Sub ImportXlwingsUdfsModule(tf As String)
    ' Fallback: This is called from Python as direct pywin32 calls were sometimes failing, see comments in the Python code
    On Error Resume Next
    ThisWorkbook.VBProject.VBComponents.Remove ThisWorkbook.VBProject.VBComponents("xlwings_udfs")
    On Error GoTo 0
    ThisWorkbook.VBProject.VBComponents.Import tf
End Sub

Private Sub GetDLLVersion()
    ' Currently only for testing
    Dim tag As String, arch As String
    Dim ver As Double
    XLPyDLLVersion tag, ver, arch
    Debug.Print tag
    Debug.Print ver
    Debug.Print arch
End Sub




'Attribute VB_Name = "Config"



#If App = "Microsoft Excel" Then
Function GetDirectoryPath(Optional wb As Workbook) As String
#Else
Function GetDirectoryPath(Optional wb As Variant) As String
#End If
    ' Leaving this here for now because we currently don't have #Const App in Utils
    Dim Path As String
    #If App = "Microsoft Excel" Then
        On Error Resume Next 'On Mac, this is called when exiting the Python interpreter
            Path = GetDirectory(GetFullName(wb))
        On Error GoTo 0
    #ElseIf App = "Microsoft Word" Then
        Path = ThisDocument.Path
    #ElseIf App = "Microsoft Access" Then
        Path = CurrentProject.Path ' Won't be transformed for standalone module as ThisProject doesn't exit
    #ElseIf App = "Microsoft PowerPoint" Then
        Path = ActivePresentation.Path ' Won't be transformed for standalone module ThisPresentation doesn't exist
    #Else
        Exit Function
    #End If
    GetDirectoryPath = Path
End Function

Function GetConfigFilePath() As String
    #If Mac Then
        ' ~/Library/Containers/com.microsoft.Excel/Data/xlwings.conf
        GetConfigFilePath = GetMacDir("$HOME", False) & "/" & PROJECT_NAME & ".conf"
    #Else
        GetConfigFilePath = Environ("USERPROFILE") & "\." & PROJECT_NAME & "\" & PROJECT_NAME & ".conf"
    #End If
End Function

Function GetDirectoryConfigFilePath() As String
    Dim pathSeparator As String
    
    #If Mac Then ' Application.PathSeparator doesn't seem to exist in Access...
        pathSeparator = "/"
    #Else
        pathSeparator = "\"
    #End If
    
    GetDirectoryConfigFilePath = GetDirectoryPath(ActiveWorkbook) & pathSeparator & PROJECT_NAME & ".conf"
End Function

#If App = "Microsoft Excel" Then
Function GetConfigFromSheet(wb As Workbook)
    Dim lastCell As Range, cell As Range
    #If Mac Then
    Dim d As Dictionary
    Set d = New Dictionary
    #Else
    Dim d As Object
    Set d = CreateObject("Scripting.Dictionary")
    #End If
    Dim sht As Worksheet

    Set sht = wb.Sheets(PROJECT_NAME & ".conf")

    If sht.Range("A2") = "" Then
        Set lastCell = sht.Range("A1")
    Else
        Set lastCell = sht.Range("A1").End(xlDown)
    End If

    For Each cell In Range(sht.Range("A1"), lastCell)
        d.Add UCase(cell.Value), cell.Offset(0, 1).Value
    Next cell
    Set GetConfigFromSheet = d
End Function
#End If

Function GetConfig(configKey As String, Optional default As String = "", Optional source As String = "") As Variant
    Dim configValue As String

    If Application.Name = "Microsoft Excel" Then
        If configKey = "INTERPRETER_WIN" Then
            GetConfig = "test_python_path\pythonw.exe"
        ElseIf configKey = "UDF MODULES" Then
            GetConfig = "pyxelrest._generator"
        End If
    End If

    If GetConfig = "" Then
        GetConfig = default
    End If
End Function

Function SaveConfigToFile(sFileName As String, sName As String, Optional sValue As String) As Boolean
'Adopted from http://peltiertech.com/save-retrieve-information-text-files/

  Dim iFileNumA As Long, iFileNumB As Long, lErrLast As Long
  Dim sFile As String, sXFile As String, sVarName As String, sVarValue As String
      
    
  #If Mac Then
    If Not FileOrFolderExistsOnMac(ParentFolder(sFileName)) Then
  #Else
    If Len(Dir(ParentFolder(sFileName), vbDirectory)) = 0 Then
  #End If
     MkDir ParentFolder(sFileName)
  End If

  ' assume false unless variable is successfully saved
  SaveConfigToFile = False

  ' temporary file
  sFile = sFileName
  sXFile = sFileName & "_temp"

  ' open text file to read settings
  If FileExists(sFile) Then
    'replace existing settings file
    iFileNumA = FreeFile
    Open sFile For Input As iFileNumA
    iFileNumB = FreeFile
    Open sXFile For Output As iFileNumB
      Do While Not EOF(iFileNumA)
        Input #iFileNumA, sVarName, sVarValue
        If sVarName <> sName Then
          Write #iFileNumB, sVarName, sVarValue
        End If
      Loop
      Write #iFileNumB, sName, sValue
      SaveConfigToFile = True
    Close #iFileNumA
    Close #iFileNumB
    FileCopy sXFile, sFile
    Kill sXFile
  Else
    ' make new file
    iFileNumB = FreeFile
    Open sFile For Output As iFileNumB
      Write #iFileNumB, sName, sValue
      SaveConfigToFile = True
    Close #iFileNumB
  End If

End Function

Function GetConfigFromFile(sFile As String, sName As String, Optional sValue As String) As Boolean
'Based on http://peltiertech.com/save-retrieve-information-text-files/

  Dim iFileNum As Long, lErrLast As Long
  Dim sVarName As String, sVarValue As String


  ' assume false unless variable is found
  GetConfigFromFile = False

  ' open text file to read settings
  If FileExists(sFile) Then
    iFileNum = FreeFile
    Open sFile For Input As iFileNum
      Do While Not EOF(iFileNum)
        Input #iFileNum, sVarName, sVarValue
        If LCase(sVarName) = LCase(sName) Then
          sValue = sVarValue
          GetConfigFromFile = True
          Exit Do
        End If
      Loop
    Close #iFileNum
  End If

End Function

'Attribute VB_Name = "Extensions"
Function sql(query, ParamArray tables())
        If TypeOf Application.Caller Is Range Then On Error GoTo failed
        ReDim argsArray(1 To UBound(tables) - LBound(tables) + 2)
        argsArray(1) = query
        For K = LBound(tables) To UBound(tables)
        argsArray(2 + K - LBound(tables)) = tables(K)
        Next K
        If has_dynamic_array() Then
            sql = Py.CallUDF("xlwings.ext", "sql_dynamic", argsArray, ActiveWorkbook, Application.Caller)
        Else
            sql = Py.CallUDF("xlwings.ext", "sql", argsArray, ActiveWorkbook, Application.Caller)
        End If
        Exit Function
failed:
        sql = Err.Description
End Function

'Attribute VB_Name = "Utils"



Function WScript(Optional CreateNew As Boolean) As Object
  Static Value As Object
  If CreateNew Or Value Is Nothing Then Set Value = CreateObject("WScript.Shell")
  Set WScript = Value
End Function

Function IsFullName(sFile As String) As Boolean
  ' if sFile includes path, it contains path separator "\" or "/"
  IsFullName = InStr(sFile, "\") + InStr(sFile, "/") > 0
End Function

Function FileExists(ByVal FileSpec As String) As Boolean
    #If Mac Then
        FileExists = FileOrFolderExistsOnMac(FileSpec)
    #Else
        FileExists = FileExistsOnWindows(FileSpec)
    #End If
End Function

Function FileExistsOnWindows(ByVal FileSpec As String) As Boolean
   ' by Karl Peterson MS MVP VB
   Dim Attr As Long
   ' Guard against bad FileSpec by ignoring errors
   ' retrieving its attributes.
   On Error Resume Next
   Attr = GetAttr(FileSpec)
   If Err.Number = 0 Then
      ' No error, so something was found.
      ' If Directory attribute set, then not a file.
      FileExistsOnWindows = Not ((Attr And vbDirectory) = vbDirectory)
   End If
End Function


Function FileOrFolderExistsOnMac(FileOrFolderstr As String) As Boolean
'Ron de Bruin : 26-June-2015
'Function to test whether a file or folder exist on a Mac in office 2011 and up
'Uses AppleScript to avoid the problem with long names in Office 2011,
'limit is max 32 characters including the extension in 2011.
    Dim ScriptToCheckFileFolder As String
    Dim TestStr As String
    
    #If Mac Then
    If Val(Application.VERSION) < 15 Then
        ScriptToCheckFileFolder = "tell application " & Chr(34) & "System Events" & Chr(34) & _
         "to return exists disk item (" & Chr(34) & FileOrFolderstr & Chr(34) & " as string)"
        FileOrFolderExistsOnMac = MacScript(ScriptToCheckFileFolder)
    Else
        On Error Resume Next
        TestStr = Dir(FileOrFolderstr, vbDirectory)
        On Error GoTo 0
        If Not TestStr = vbNullString Then FileOrFolderExistsOnMac = True
    End If
    #End If
End Function

Function ParentFolder(ByVal Folder)
  #If Mac Then
      ParentFolder = Left$(Folder, InStrRev(Folder, "/") - 1)
  #Else
      ParentFolder = Left$(Folder, InStrRev(Folder, "\") - 1)
  #End If
End Function

Function GetDirectory(Path)
    #If Mac Then
    GetDirectory = Left(Path, InStrRev(Path, "/"))
    #Else
    GetDirectory = Left(Path, InStrRev(Path, "\"))
    #End If
End Function

Function KillFileOnMac(Filestr As String)
    'Ron de Bruin
    '30-July-2012
    'Delete files from a Mac.
    'Uses AppleScript to avoid the problem with long file names (on 2011 only)

    Dim ScriptToKillFile As String
    
    #If Mac Then
    ScriptToKillFile = "tell application " & Chr(34) & "Finder" & Chr(34) & Chr(13)
    ScriptToKillFile = ScriptToKillFile & "do shell script ""rm "" & quoted form of posix path of " & Chr(34) & Filestr & Chr(34) & Chr(13)
    ScriptToKillFile = ScriptToKillFile & "end tell"

    On Error Resume Next
        MacScript (ScriptToKillFile)
    On Error GoTo 0
    #End If
End Function

Function ToMacPath(PosixPath As String) As String
    ' This function transforms a Posix Path into a MacOS Path
    ' E.g. "/Users/<User>" --> "MacintoshHD:Users:<User>"
    #If Mac Then
    ToMacPath = MacScript("set mac_path to POSIX file " & Chr(34) & PosixPath & Chr(34) & " as string")
    #End If
End Function

Function GetMacDir(Name As String, Normalize As Boolean) As String
    #If Mac Then
        Select Case Name
            Case "$HOME"
                Name = "home folder"
            Case "$APPLICATIONS"
                Name = "applications folder"
            Case "$DOCUMENTS"
                Name = "documents folder"
            Case "$DOWNLOADS"
                Name = "downloads folder"
            Case "$DESKTOP"
                Name = "desktop folder"
            Case "$TMPDIR"
                Name = "temporary items"
        End Select
        GetMacDir = MacScript("return POSIX path of (path to " & Name & ") as string")
        If Normalize = True Then
            'Normalize Excel sandbox location
            GetMacDir = Replace(GetMacDir, "/Library/Containers/com.microsoft.Excel/Data", "")
        End If
    #Else
    #End If
End Function


Function ToPosixPath(ByVal MacPath As String) As String
    'This function accepts relative paths with backward and forward slashes: ActiveWorkbook & "\test"
    ' E.g. "MacintoshHD:Users:<User>" --> "/Users/<User>"

    Dim s As String
    Dim LeadingSlash As Boolean
    
    #If Mac Then
    If MacPath = "" Then
        ToPosixPath = ""
    Else
        ToPosixPath = Replace(MacPath, "\", "/")
        ToPosixPath = MacScript("return POSIX path of (" & Chr(34) & MacPath & Chr(34) & ") as string")
    End If
    #End If
End Function

Sub ShowError(FileName As String, Optional Message As String = "")
    ' Shows a MsgBox with the content of a text file

    Dim Content As String
    Dim ErrorSheet As Worksheet

    Const OK_BUTTON_ERROR = 16
    Const AUTO_DISMISS = 0
    
    If Message = "" Then
        Content = ReadFile(FileName)
    Else
        Content = Message
    End If
    

    If GetConfig("SHOW_ERROR_POPUPS", "True") = "False" Then
        If SheetExists(ActiveWorkbook, "Error") = False Then
            Set ErrorSheet = ActiveWorkbook.Sheets.Add()
            ErrorSheet.Name = "Error"
        Else
            Set ErrorSheet = ActiveWorkbook.Sheets("Error")
        End If
        ErrorSheet.Range("A1").Value = Content
    Else
        #If Mac Then
            MsgBox Content, vbCritical, "Error"
        #Else
            Content = Content & vbCrLf
            Content = Content & "Press Ctrl+C to copy this message to the clipboard."
    
            WScript.Popup Content, AUTO_DISMISS, "Error", OK_BUTTON_ERROR
        #End If
    End If
End Sub

Function ExpandEnvironmentStrings(ByVal s As String)
    ' Expand environment variables
    Dim EnvString As String
    Dim PathParts As Variant
    Dim i As Integer
    #If Mac Then
        If Left(s, 1) = "$" Then
            PathParts = Split(s, "/")
            EnvString = PathParts(0)
            ExpandEnvironmentStrings = GetMacDir(EnvString, True)
            For i = 1 To UBound(PathParts)
                If Right$(ExpandEnvironmentStrings, 1) = "/" Then
                    ExpandEnvironmentStrings = ExpandEnvironmentStrings & PathParts(i)
                Else
                    ExpandEnvironmentStrings = ExpandEnvironmentStrings & "/" & PathParts(i)
                End If
            Next i
        Else
            ExpandEnvironmentStrings = s
        End If
    #Else
        ExpandEnvironmentStrings = WScript.ExpandEnvironmentStrings(s)
    #End If
End Function

Function ReadFile(ByVal FileName As String)
    ' Read a text file

    Dim Content As String
    Dim Token As String
    Dim FileNum As Integer
    Dim objShell As Object
    Dim LineBreak As Variant

    #If Mac Then
        FileName = ToMacPath(FileName)
        LineBreak = vbLf
    #Else
        FileName = ExpandEnvironmentStrings(FileName)
        LineBreak = vbCrLf
    #End If

    FileNum = FreeFile
    Content = ""

    ' Read Text File
    Open FileName For Input As #FileNum
        Do While Not EOF(FileNum)
            Line Input #FileNum, Token
            Content = Content & Token & LineBreak
        Loop
    Close #FileNum

    ReadFile = Content
End Function

#If App = "Microsoft Excel" Then
Function SheetExists(wb As Workbook, sheetName As String) As Boolean
    Dim sht As Worksheet
    On Error Resume Next
        Set sht = wb.Sheets(sheetName)
    On Error GoTo 0
    SheetExists = Not sht Is Nothing
End Function
#End If

Function GetBaseName(wb As String) As String
    Dim extension As String
    extension = LCase$(Right$(wb, 4))
    If extension = ".xls" Or extension = ".xla" Or extension = ".xlt" Then
        GetBaseName = Left$(wb, Len(wb) - 4)
    Else
        GetBaseName = Left$(wb, Len(wb) - 5)
    End If
End Function

Function has_dynamic_array() As Boolean
    has_dynamic_array = False
    On Error GoTo ErrHandler
        Application.WorksheetFunction.Unique ("dummy")
        has_dynamic_array = True
    Exit Function
ErrHandler:
    has_dynamic_array = False
End Function

Public Function CreateGUID() As String
    Randomize Timer() + Application.Hwnd
    ' https://stackoverflow.com/a/46474125/918626
    Do While Len(CreateGUID) < 32
        If Len(CreateGUID) = 16 Then
            '17th character holds version information
            CreateGUID = CreateGUID & Hex$(8 + CInt(Rnd * 3))
        End If
        CreateGUID = CreateGUID & Hex$(CInt(Rnd * 15))
    Loop
    CreateGUID = Mid(CreateGUID, 1, 8) & "-" & Mid(CreateGUID, 9, 4) & "-" & Mid(CreateGUID, 13, 4) & "-" & Mid(CreateGUID, 17, 4) & "-" & Mid(CreateGUID, 21, 12)
End Function

Function CheckConda(CondaPath As String) As Boolean
    ' Check if the conda executable exists.
    ' If it doesn't, conda is too old and the Interpreter setting has to be used instead of Conda settings
    Dim condaExecutable As String
    Dim condaExists As Boolean
    #If Mac Then
        condaExecutable = CondaPath & "\condabin\conda"
    #Else
        condaExecutable = CondaPath & "\condabin\conda.bat"
    #End If
    ' Replace space escape character ^ to check if path exists
    condaExists = FileExists(Replace(condaExecutable, "^", ""))
    If condaExists = False And CondaPath <> "" Then
        MsgBox "Your Conda version seems to be too old for the Conda settings. Use the Interpreter setting instead."
    End If
    CheckConda = condaExists
End Function

#If App = "Microsoft Excel" Then
Function GetFullName(wb As Workbook) As String
    ' The only case where this is still used is for directory-based config files, otherwise this is now handled in Python
    ' Unlike the Python version, this doesn't work for SharePoint and will just ignore a directory-based config file silently

    Dim total_found, i_parsing, i_env_var, slash_number As Integer
    Dim found_path, one_drive_path, full_path_name, this_found_path As String

    ' In the majority of cases, ActiveWorkbook.FullName will provide the path of the
    ' Excel workbook correctly. Unfortunately, when the user is using OneDrive
    ' this doesn't work. This function will attempt to find the LOCAL path.
    ' This uses code from Daniel Guetta and
    ' https://stackoverflow.com/questions/33734706/excels-fullname-property-with-onedrive
    
    If InStr(wb.FullName, "://") = 0 Or wb.Path = "" Then
        GetFullName = wb.FullName
        Exit Function
    End If
        
    ' According to the link above, there are three possible environment variables
    ' the user's OneDrive folder could be located in
    '      "OneDriveCommercial", "OneDriveConsumer", "OneDrive"
    '
    ' Furthermore, there are two possible formats for OneDrive URLs
    '    1. "https://companyName-my.sharepoint.com/personal/userName_domain_com/Documents" & file.FullName
    '    2. "https://d.docs.live.net/d7bbaa#######1/" & file.FullName
    ' In the first case, we can find the true path by just looking for everything after /Documents. In the
    ' second, we need to look for the fourth slash in the URL
    '
    ' The code below will try every combination of the three environment variables above, and
    ' each of the two methods of parsing the URL. The file is found in *exactly* one of those
    ' locations, then we're good to go.
    '
    ' Note that this still leaves a gap - if this file (file A) is in a location that is NOT covered by the
    ' eventualities above AND a file of the exact same name (file B) exists in one of the locations that is
    ' covered above, then this function will identify File B's location as the location of this workbook,
    ' which would be wrong
    total_found = 0
    
    For i_parsing = 1 To 2
        If i_parsing = 1 Then
            ' Parse using method 1 above; find /Documents and take everything after, INCLUDING the
            ' leading slash
            If InStr(1, wb.FullName, "/Documents") Then
                full_path_name = Mid(wb.FullName, InStr(1, wb.FullName, "/Documents") + Len("/Documents"))
            Else
                full_path_name = ""
            End If
        Else
            ' Parse using method 2; find everything after the fourth slash, including that fourth
            ' slash
            Dim i_pos As Integer
            
            ' Start at the last slash in https://
            i_pos = 8

            For slash_number = 1 To 2
                i_pos = InStr(i_pos + 1, wb.FullName, "/")
            Next slash_number
            
            full_path_name = Mid(wb.FullName, i_pos)
        End If
        
        ' Replace forward slahes with backslashes on Windows
        full_path_name = Replace(full_path_name, "/", Application.pathSeparator)
        
        
        If full_path_name <> "" Then
            #If Not Mac Then
            For i_env_var = 1 To 3
                    one_drive_path = Environ(Choose(i_env_var, "OneDriveCommercial", "OneDriveConsumer", "OneDrive"))
                
                    If (one_drive_path <> "") And FileExists(one_drive_path & full_path_name) Then
                        this_found_path = one_drive_path & full_path_name
                        
                        If this_found_path <> found_path Then
                            total_found = total_found + 1
                            found_path = this_found_path
                        End If
                    End If
            Next i_env_var
            #End If
        End If
    Next i_parsing
        
    If total_found = 1 Then
        GetFullName = found_path
        Exit Function
    End If

End Function
#End If





'Attribute VB_Name = "Remote"

Function RunRemotePython( _
    url As String, _
    Optional apiKey As String, _
    Optional include As String, _
    Optional exclude As String, _
    Optional headers As Variant, _
    Optional timeout As Integer, _
    Optional proxyServer As String, _
    Optional proxyBypassList As String, _
    Optional proxyUsername As String, _
    Optional proxyPassword As String, _
    Optional enableAutoProxy As String, _
    Optional insecure As String, _
    Optional followRedirects As String _
)

    Dim wb As Workbook
    Set wb = ActiveWorkbook

    ' Config
    ' takes the first value it finds in this order:
    ' func arg, sheet config, directory config, user config
    If include = "" Then
        include = GetConfig("INCLUDE")
    End If
    Dim includeArray() As String
    If include <> "" Then
        includeArray = Split(include, ",")
    End If

    If exclude = "" Then
        exclude = GetConfig("EXCLUDE")
    End If
    Dim excludeArray() As String
    If exclude <> "" Then
        excludeArray = Split(exclude, ",")
    End If

    If include <> "" And exclude <> "" Then
        MsgBox "Either use 'include' or 'exclude', but not both!", vbCritical
        Exit Function
    End If

    If include <> "" Then
        Dim i As Integer
        For i = 1 To wb.Worksheets.Count
            If Not IsInArray(wb.Worksheets(i).Name, includeArray) Then
                ReDim Preserve excludeArray(0 To i)
                excludeArray(i) = wb.Worksheets(i).Name
            End If
        Next
    End If

    If timeout = 0 Then
        timeout = GetConfig("TIMEOUT", 0)
    End If
    If enableAutoProxy = "" Then
        enableAutoProxy = GetConfig("ENABLE_AUTO_PROXY", False)
    End If
    If insecure = "" Then
        insecure = GetConfig("INSECURE", False)
    End If
    If followRedirects = "" Then
        followRedirects = GetConfig("FOLLOW_REDIRECTS", False)
    End If
    If proxyPassword = "" Then
        proxyPassword = GetConfig("PROXY_PASSWORD", "")
    End If
    If proxyUsername = "" Then
        proxyUsername = GetConfig("PROXY_USERNAME", "")
    End If
    If proxyServer = "" Then
        proxyServer = GetConfig("PROXY_SERVER", "")
    End If
    If proxyBypassList = "" Then
        proxyBypassList = GetConfig("PROXY_BYPASS_LIST", "")
    End If
    If apiKey = "" Then
        apiKey = GetConfig("API_KEY", "")
    End If

    ' Request payload
    Dim payload As New Dictionary
    payload.Add "client", "VBA"
    payload.Add "version", XLWINGS_VERSION
    
    Dim bookPayload As New Dictionary
    bookPayload.Add "name", ActiveWorkbook.Name
    bookPayload.Add "active_sheet_index", ActiveSheet.Index - 1
    If TypeOf Selection Is Range Then
        bookPayload.Add "selection", Application.Selection.Address(False, False)
    Else
        bookPayload.Add "selection", Null
    End If
    payload.Add "book", bookPayload

    ' Names
    Dim myname As Name
    Dim mynames() As Dictionary
    Dim nNames As Integer
    Dim iName As Integer
    nNames = wb.Names.Count
    If nNames > 0 Then
        ReDim mynames(nNames - 1)
        For iName = 1 To nNames
            Set myname = wb.Names(iName)
            Dim nameDict As Dictionary
            Set nameDict = New Dictionary
            nameDict.Add "name", myname.Name
            Dim isNamedRange As Boolean
            Dim testRange As Range
            isNamedRange = False
            On Error Resume Next
            Set testRange = myname.RefersToRange
            If Err.Number = 0 Then isNamedRange = True
            On Error GoTo 0
            If isNamedRange Then
                nameDict.Add "sheet_index", myname.RefersToRange.Parent.Index - 1
                nameDict.Add "address", myname.RefersToRange.Address(False, False)
                nameDict.Add "book_scope", TypeOf myname.Parent Is Workbook
            Else
                ' Named constants and formulas
                nameDict.Add "sheet_index", Null
                nameDict.Add "address", Null
                nameDict.Add "book_scope", Null
            End If
            Set mynames(iName - 1) = nameDict
        Next
        payload.Add "names", mynames
    Else
        payload.Add "names", Array()
    End If

    Dim sheetsPayload() As Dictionary
    ReDim sheetsPayload(wb.Worksheets.Count - 1)
    For i = 1 To wb.Worksheets.Count
        Dim sheetDict As Dictionary
        Set sheetDict = New Dictionary
        sheetDict.Add "name", wb.Worksheets(i).Name

        ' Pictures
        Dim pic As Picture
        Dim pics() As Dictionary
        Dim nPics As Integer
        Dim iPic As Integer
        nPics = wb.Worksheets(i).Pictures.Count
        If nPics > 0 Then
            ReDim pics(nPics - 1)
            For iPic = 1 To nPics
                Set pic = wb.Worksheets(i).Pictures(iPic)
                Dim picDict As Dictionary
                Set picDict = New Dictionary
                picDict.Add "name", pic.Name
                picDict.Add "height", pic.Height
                picDict.Add "width", pic.Width
                Set pics(iPic - 1) = picDict
            Next
            sheetDict.Add "pictures", pics
        Else
            sheetDict.Add "pictures", Array()
        End If

        ' Values
        Dim values As Variant
        If IsInArray(wb.Worksheets(i).Name, excludeArray) Then
            values = Array(Array())
        ElseIf IsEmpty(wb.Worksheets(i).UsedRange.Value) Then
            values = Array(Array())
        Else
            Dim startRow As Integer, startCol As Integer
            Dim nRows As Integer, nCols As Integer
            Dim myUsedRange As Range
            With wb.Worksheets(i).UsedRange
                startRow = .Row
                startCol = .Column
                nRows = .Rows.Count
                nCols = .Columns.Count
            End With
            With wb.Worksheets(i)
                Set myUsedRange = .Range( _
                    .Cells(1, 1), _
                    .Cells(startRow + nRows - 1, startCol + nCols - 1) _
                )
                values = myUsedRange.Value
                If myUsedRange.Count = 1 Then
                    values = Array(Array(values))
                End If
            End With
        End If
        sheetDict.Add "values", values
        Set sheetsPayload(i - 1) = sheetDict
    Next
    payload.Add "sheets", sheetsPayload
    
    Dim myRequest As New WebRequest
    Set myRequest.Body = payload

    ' Debug.Print myRequest.Body

    ' Headers
    ' Expected as Dictionary and currently not supported via xlwings.conf
    ' Providing the Authorization header will ignore the API_KEY
    Dim authHeader As Boolean
    authHeader = False
    If Not IsMissing(headers) Then
        Dim myKey As Variant
        For Each myKey In headers.myKeys
            myRequest.AddHeader CStr(myKey), headers(myKey)
        Next
        If headers.Exists("Authorization") Then
            authHeader = True
        End If
    End If

    If authHeader = False Then
        If apiKey <> "" Then
            myRequest.AddHeader "Authorization", apiKey
        End If
    End If

    ' API call
    myRequest.Method = WebMethod.HttpPost
    myRequest.Format = WebFormat.Json

    Dim myClient As New WebClient
    myClient.BaseUrl = url
    If timeout <> 0 Then
        myClient.TimeoutMs = timeout
    End If
    If proxyBypassList <> "" Then
        myClient.proxyBypassList = proxyBypassList
    End If
    If proxyServer <> "" Then
        myClient.proxyServer = proxyServer
    End If
    If proxyUsername <> "" Then
        myClient.proxyUsername = proxyUsername
    End If
    If proxyPassword <> "" Then
        myClient.proxyPassword = proxyPassword
    End If
    If enableAutoProxy <> False Then
        myClient.enableAutoProxy = enableAutoProxy
    End If
    If insecure <> False Then
        myClient.insecure = insecure
    End If
    If followRedirects <> False Then
        myClient.followRedirects = followRedirects
    End If

    Dim myResponse As WebResponse
    Set myResponse = myClient.Execute(myRequest)
    
    ' Debug.Print myResponse.Content
    
    ' Parse JSON response and run functions
    If myResponse.StatusCode = WebStatusCode.Ok Then
        Dim action As Dictionary
        For Each action In myResponse.Data("actions")
            Application.Run action("func"), wb, action
        Next
    Else
        If myResponse.Content <> "" Then
            MsgBox myResponse.Content, vbCritical, "Error"
        Else
            MsgBox myResponse.StatusDescription & " (" & myResponse.StatusCode & ")", vbCritical, "Error"
        End If
    End If

End Function

' Helpers
Function GetRange(wb As Workbook, action As Dictionary)
    If action("row_count") = 1 And action("column_count") = 1 Then
        Set GetRange = wb.Worksheets( _
            action("sheet_position") + 1).Cells(action("start_row") + 1, _
            action("start_column") + 1 _
        )
    Else
        With wb.Worksheets(action("sheet_position") + 1)
            Set GetRange = .Range( _
                .Cells(action("start_row") + 1, action("start_column") + 1), _
                .Cells( _
                    action("start_row") + action("row_count"), _
                    action("start_column") + action("column_count") _
                ) _
            )
        End With
    End If
End Function

Function Utf8ToUtf16(ByVal strText As String) As String
    ' macOs only: apparently, Excel uses UTF-16 to represent string literals
    ' Taken from https://stackoverflow.com/a/64624336/918626
    Dim i&, l1&, l2&, l3&, l4&, l&
    For i = 1 To Len(strText)
        l1 = Asc(Mid(strText, i, 1))
        If i + 1 <= Len(strText) Then l2 = Asc(Mid(strText, i + 1, 1))
        If i + 2 <= Len(strText) Then l3 = Asc(Mid(strText, i + 2, 1))
        If i + 3 <= Len(strText) Then l4 = Asc(Mid(strText, i + 3, 1))
        Select Case l1
        Case 1 To 127
            l = l1
        Case 194 To 223
            l = ((l1 And &H1F) * 2 ^ 6) Or (l2 And &H3F)
            i = i + 1
        Case 224 To 239
            l = ((l1 And &HF) * 2 ^ 12) Or ((l2 And &H3F) * 2 ^ 6) Or (l3 And &H3F)
            i = i + 2
        Case 240 To 255
            l = ((l1 And &H7) * 2 ^ 18) Or ((l2 And &H3F) * 2 ^ 12) Or ((l3 And &H3F) * 2 ^ 6) Or (l4 And &H3F)
            i = i + 4
        Case Else
            l = 63 ' question mark
        End Select
        Utf8ToUtf16 = Utf8ToUtf16 & IIf(l < 55296, WorksheetFunction.Unichar(l), "?")
    Next i
End Function

Function HexToRgb(ByVal hexColor As String) As Variant
    ' Based on https://stackoverflow.com/a/63779233/918626
    Dim red As String, green As String, blue As String
    hexColor = Replace(hexColor, "#", "")
    red = Val("&H" & Mid(hexColor, 1, 2))
    green = Val("&H" & Mid(hexColor, 3, 2))
    blue = Val("&H" & Mid(hexColor, 5, 2))
    HexToRgb = RGB(red, green, blue)
End Function

Function IsInArray(stringToBeFound As String, arr As Variant) As Boolean
    ' Based on https://stackoverflow.com/a/38268261/918626
    If IsEmpty(arr) Then
        IsInArray = False
        Exit Function
    End If
    Dim i As Integer
    On Error GoTo ErrHandler
    For i = LBound(arr) To UBound(arr)
        If Trim(arr(i)) = stringToBeFound Then
            IsInArray = True
            Exit Function
        End If
    Next i
    On Error GoTo 0
    IsInArray = False
ErrHandler:
    IsInArray = False
End Function

Function base64ToPic(base64string As Variant) As String
    Dim tempPath As String
    ' TODO: handle other image formats than png
    #If Mac Then
        tempPath = GetMacDir("$HOME", False) & "xlwings-" & CreateGUID() & ".png"
        Dim rv As Variant
        rv = ExecuteInShell("echo """ & base64string & """ | base64 -d > " & tempPath).Output
    #Else
        tempPath = Environ("Temp") & "\xlwings-" & CreateGUID() & ".png"
        Open tempPath For Binary As #1
           Put #1, 1, Base64Decode(base64string)
        Close #1
    #End If
    base64ToPic = tempPath
End Function

' Functions
Sub setValues(wb As Workbook, action As Dictionary)
    Dim arr() As Variant
    Dim i As Long, j As Long
    Dim values As Collection, valueRow As Collection

    Set values = action("values")
    ReDim arr(values.Count, values(1).Count)

    For i = 1 To values.Count
        Set valueRow = values(i)
        For j = 1 To valueRow.Count
            On Error Resume Next
                ' TODO: will be replaced when backend sends location of dates
                arr(i - 1, j - 1) = WebHelpers.ParseIso(valueRow(j))
            If Err.Number <> 0 Then
                #If Mac Then
                If Application.IsText(valueRow(j)) Then
                    arr(i - 1, j - 1) = Utf8ToUtf16(valueRow(j))
                Else
                    arr(i - 1, j - 1) = valueRow(j)
                End If
                #Else
                    arr(i - 1, j - 1) = valueRow(j)
                #End If
            End If
            On Error GoTo 0
        Next j
    Next i
    GetRange(wb, action).Value = arr
End Sub

Sub clearContents(wb As Workbook, action As Dictionary)
    GetRange(wb, action).clearContents
End Sub

Sub addSheet(wb As Workbook, action As Dictionary)
    Dim mysheet As Worksheet
    Set mysheet = wb.Sheets.Add
    mysheet.Move After:=Worksheets(action("args")(1) + 1)
End Sub

Sub setSheetName(wb As Workbook, action As Dictionary)
    wb.Sheets(action("sheet_position") + 1).Name = action("args")(1)
End Sub

Sub setAutofit(wb As Workbook, action As Dictionary)
    If action("args")(1) = "columns" Then
        GetRange(wb, action).Columns.AutoFit
    Else
        GetRange(wb, action).Rows.AutoFit
    End If
End Sub

Sub setRangeColor(wb As Workbook, action As Dictionary)
    GetRange(wb, action).Interior.Color = HexToRgb(action("args")(1))
End Sub

Sub activateSheet(wb As Workbook, action As Dictionary)
    wb.Sheets(action("args")(1) + 1).Activate
End Sub

Sub addHyperlink(wb As Workbook, action As Dictionary)
    GetRange(wb, action).Hyperlinks.Add _
        Anchor:=GetRange(wb, action), _
        Address:=action("args")(1), _
        TextToDisplay:=action("args")(2), _
        ScreenTip:=action("args")(3)
End Sub

Sub setNumberFormat(wb As Workbook, action As Dictionary)
    GetRange(wb, action).NumberFormat = action("args")(1)
End Sub

Sub setPictureName(wb As Workbook, action As Dictionary)
    wb.Sheets(action("sheet_position") + 1).Pictures(action("args")(1) + 1).Name = action("args")(2)
End Sub

Sub setPictureHeight(wb As Workbook, action As Dictionary)
    wb.Sheets(action("sheet_position") + 1).Pictures(action("args")(1) + 1).Height = action("args")(2)
End Sub

Sub setPictureWidth(wb As Workbook, action As Dictionary)
    wb.Sheets(action("sheet_position") + 1).Pictures(action("args")(1) + 1).Width = action("args")(2)
End Sub

Sub deletePicture(wb As Workbook, action As Dictionary)
    wb.Sheets(action("sheet_position") + 1).Pictures(action("args")(1) + 1).Delete
End Sub

Sub addPicture(wb As Workbook, action As Dictionary)
    Dim tempPath As String
    Dim anchorCell As Range
    Dim imgLeft, imgTop, imgWidth, imgHeight As Long

    tempPath = base64ToPic(action("args")(1))
    With wb.Sheets(action("sheet_position") + 1)
        Set anchorCell = .Cells(action("args")(3) + 1, action("args")(2) + 1)
    End With
    If action("args")(4) > 0 Then
        imgLeft = action("args")(4)
    Else
        imgLeft = anchorCell.Left
    End If
    If action("args")(5) > 0 Then
        imgTop = action("args")(5)
    Else
        imgTop = anchorCell.Top
    End If

    wb.Sheets(action("sheet_position") + 1).Shapes.addPicture tempPath, False, True, imgLeft, imgTop, -1, -1
    On Error Resume Next
        Kill tempPath
    On Error GoTo 0
End Sub

Sub updatePicture(wb As Workbook, action As Dictionary)
    Dim img As Picture
    Dim newImg As Shape
    Dim tempPath, imgName As String
    Dim imgLeft, imgTop, imgWidth, imgHeight As Long
    tempPath = base64ToPic(action("args")(1))
    Set img = wb.Sheets(action("sheet_position") + 1).Pictures(action("args")(2) + 1)
    imgName = img.Name
    imgLeft = img.Left
    imgTop = img.Top
    imgWidth = img.Width
    imgHeight = img.Height
    img.Delete
    Set newImg = wb.Sheets(action("sheet_position") + 1).Shapes.addPicture(tempPath, False, True, imgLeft, imgTop, imgWidth, imgHeight)
    newImg.Name = imgName
    On Error Resume Next
        Kill tempPath
    On Error GoTo 0
End Sub

Sub alert(wb As Workbook, action As Dictionary)
    Dim myPrompt As String, myTitle As String, myButtons As String, myMode As String, myCallback As String
    Dim myStyle As Integer, rv As Integer
    Dim buttonResult As String

    myPrompt = action("args")(1)
    myTitle = action("args")(2)
    myButtons = action("args")(3)
    myMode = action("args")(4)
    myCallback = action("args")(5)

    Select Case myButtons
    Case "ok"
        myStyle = VBA.vbOKOnly
    Case "ok_cancel"
        myStyle = VBA.vbOKCancel
    Case "yes_no"
        myStyle = VBA.vbYesNo
    Case "yes_no_cancel"
        myStyle = VBA.vbYesNoCancel
    End Select

    If myMode = "info" Then
        myStyle = myStyle + VBA.vbInformation
    ElseIf myMode = "critical" Then
        myStyle = myStyle + VBA.vbCritical
    End If

    rv = MsgBox(Prompt:=myPrompt, Title:=myTitle, Buttons:=myStyle)

    Select Case rv
    Case 1
        buttonResult = "ok"
    Case 2
        buttonResult = "cancel"
    Case 6
        buttonResult = "yes"
    Case 7
        buttonResult = "no"
    End Select


    If myCallback <> "" Then
        Application.Run myCallback, buttonResult
    End If

End Sub
