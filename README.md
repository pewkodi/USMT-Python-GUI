# USMT-Python-GUI

How to Compile and Use: 
Install Python 2.7.16 x86 and Install py2exe plus any needed libraries: win32api pyad

Adjust the usmt_sid-6-git.py to suit your needs: ie domain or server.
Adjust xml files to suit your needs.
Downloaded latest USMT from Microsoft: https://docs.microsoft.com/en-us/windows-hardware/get-started/adk-install

Install only the usmt tools

Compile the py file with setupuac.py: http://www.py2exe.org/index.cgi/Tutorial

Once it is build double click on require_admin.exe which is the binary to use.
The sample binary will have usmt.exe in it.

Note the directory structure in the sample.

+tcl/

+usmt/amd64/

+Python files

Once everything is working you can place on a usb/network drive etc and run the usmt helper exe.

It will copy the usmt tool to c:\win7usmt

A gui will come up:


