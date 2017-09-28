' ConvertToNTM.vbs
'
' Copyright (c) Konstantin Galichsky (kg@...), 2004-2007
' All rights reserved.
' This script uses GPSMapEdit to convert multiple maps to NTM format.
'
' USAGE:
' Input files should be put into .\Maps folder (relative to the script file).
' Log.txt file is created to log progress.
'
' Connect to GPSMapEdit.
'
' Modificado por Michel Metran, sendo possivel converter os arquivos IMG para MP...

Dim a
Set a = CreateObject ("GPSMapEdit.Application.1")
a.MinimizeWindow

' Check version of GPSMapEdit
If a.Version < "1.0.30.3" Then
MsgBox "Obsolete version of GPSMapEdit is used. Please upgrade."
WScript.Quit
End If

Dim fso
Set fso = CreateObject ("Scripting.FileSystemObject")

Dim strRoot
strRoot = fso.GetAbsolutePathName (WScript.ScriptFullName + "\..\")

Dim log
Set log = fso.CreateTextFile (strRoot + "\Log.txt")

Dim pMapsFolder

If Not fso.FolderExists (strRoot + "\Maps") Then
MsgBox "Couldn't find '\Maps' folder."
WScript.Quit
End if
Set pMapsFolder = fso.GetFolder (strRoot + "\Maps")

Dim pFile
For Each pFile In pMapsFolder.Files
Dim strExt
strExt = LCase (fso.GetExtensionName (pFile.Path))
If strExt = "img" Or strExt = "rus" Or strExt = "mp" Then
a.Open pFile.Path, False

Dim strOutFile
'strOutFile = fso.GetParentFolderName(pFile.Path) + "\" + fso.GetBaseName (pFile.Path) + ".nm2"
'a.SaveAs strOutFile, "navitel-nm2"
strOutFile = fso.GetParentFolderName(pFile.Path) + "\" + fso.GetBaseName (pFile.Path) + ".mp"
a.SaveAs strOutFile, "polish"

End if

log.WriteLine strOutFile
Next

a.Exit

MsgBox "Converting maps is completed!"
