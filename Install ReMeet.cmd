@echo off
echo [Beginning Install]


powershell -Command "& {Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('WARNING: If you have python 3.9, please UNINSTALL it and install python version 3.11 BOTH ACTIONS MUST BE DONE FROM THE MICROSOFT STORE to function.', 'PYTHON WARNING', 'OK', [System.Windows.Forms.MessageBoxIcon]::Information);}"

pip install selenium
