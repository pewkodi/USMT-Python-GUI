

try: 
    from pyad import aduser,adgroup,adcontainer,addomain,adquery
except:
    print "No Connected to Domain"
import string

from Tkinter import *
from StringIO import StringIO 
import tkMessageBox
import time
import re
import os
import subprocess
from win32com.shell import shell, shellcon
import win32api
import win32security
from _winreg import *
import socket


global name
global users
global x

cwd = os.getcwd()
users = []
netpath = r'\\server\share\USMT_files\usmt\amd64'
netpath = cwd+r'\usmt\amd64'
print "Starting App in this directory "+cwd
print "Copying USMT Binaries to C:\win7mig"
print "Use this Console to Find Users to Migrate"

import win32api
import win32file
import wmi

############## Tech USB #########################################
try:
 c=wmi.WMI()
 for disk in c.query('SELECT * FROM Win32_DiskDrive WHERE MediaType LIKE "External hard disk media"'):
     deviceID = disk.DeviceID

     for partition in c.query('ASSOCIATORS OF {Win32_DiskDrive.DeviceID="' + deviceID + '"} WHERE AssocClass = Win32_DiskDriveToDiskPartition'):

        for logical_disk in c.query('ASSOCIATORS OF {Win32_DiskPartition.DeviceID="' + partition.DeviceID + '"} WHERE AssocClass = Win32_LogicalDiskToPartition'):
	     remap_from, remap_to = logical_disk.DeviceID+'\\', "G:\\"
	     volume_name = win32file.GetVolumeNameForVolumeMountPoint (remap_from)
	     win32file.DeleteVolumeMountPoint (remap_from)
	     win32file.SetVolumeMountPoint (remap_to, volume_name)

 print ('Local USB Drive letter: {}'.format(remap_to)) + " To Not Interfere With Local Drive Data Transfer D:,E:,F:"

except:
 print "No Local USB Drive Found"	




#################################################################
def usb():
# DRIVE_TYPES = """
#  0 	Unknown
#  1 	No Root Directory
#  2 	Removable Disk
#  3 	Local Disk
#  4 	Network Drive
#  5 	Compact Disc
#  6 	RAM Disk
#"""
# drive_types = dict((int (i), j) for (i, j) in (l.split ("\t") for l in DRIVE_TYPES.splitlines () if l))
# drives = (drive for drive in win32api.GetLogicalDriveStrings ().split ("\000") if drive)
# for drive in drives:
  #print drive, "=>", drive_types[win32file.GetDriveType (drive)]
#  if drive_types[win32file.GetDriveType (drive)] == 'Local Disk':
#	  print drive
 #disks = wmi.WMI().Win32_DiskDrive(MediaType="External hard disk media")
 #for disk in disks:
 #      for disk1 in wmi.WMI().Win32_LogicalDisk():
 #       print disk
 #       print disk1
#	             e2.delete(0, END)
#	             e2.insert(0, drive+r'USMT_Store')
 c=wmi.WMI()
 for disk in c.query('SELECT * FROM Win32_DiskDrive WHERE MediaType LIKE "External hard disk media"'):
     deviceID = disk.DeviceID

     for partition in c.query('ASSOCIATORS OF {Win32_DiskDrive.DeviceID="' + deviceID + '"} WHERE AssocClass = Win32_DiskDriveToDiskPartition'):

        for logical_disk in c.query('ASSOCIATORS OF {Win32_DiskPartition.DeviceID="' + partition.DeviceID + '"} WHERE AssocClass = Win32_LogicalDiskToPartition'):
            #print('USB Drive letter: {}'.format(logical_disk.DeviceID))

	    if logical_disk.VolumeName == 'Win7MIG':
	     remap_from, remap_to = logical_disk.DeviceID+'\\', "g:\\"
	     volume_name = win32file.GetVolumeNameForVolumeMountPoint (remap_from)
	     win32file.DeleteVolumeMountPoint (remap_from)
	     win32file.SetVolumeMountPoint (remap_to, volume_name)			    
	     e2.delete(0, END)
	     #e2.insert(0, logical_disk.DeviceID+r'\USMT_Store')
	     e2.insert(0, remap_to+r'USMT_Store')
     	    else:
		    print "Volume Name is Incorrect: Manually Enter the Local Drive Path"	    





 return 










##################################################################
def callback():
	 window.destroy()
	 btn['state']="active"
 	 btn.update()
         return "Exiting"

def refresh():
 	
 #T.delete('1.0',END)
 #T.edit_reset()
 #window.option_clear()
 #T.pack_forget()
 
 
 #T.mark_unset()
 
 drive = os.environ['systemdrive']

 if state1 == 'scan':
   logfile = open(drive+r'\win7usmt\amd64\usmt.log','r') 
 #  print logfile
 if state1 == 'load':
   logfile = open(drive+r'\win7usmt\amd64\load.log','r')
 #T.dump('1.0',END,T.delete('1.0',END))
 #T = Text(window, height=50, width=150) 
 #T.pack()
 T = Text(window, height=50, width=150)
 T.pack()
 T.insert('1.0',logfile.read())
 T.config(yscrollcommand=scrollbar.set)
 scrollbar.config(command=T.yview) 
 #T.config(yscrollcommand=scrollbar.set)
 #scrollbar.config(command=T.yview)
 #T.edit_reset()
 logfile.close()
 #T = Text(window, height=50, width=150)
 #T.pack()
 #T.insert(1.0,logfile.read())
 T.see(END)
 btn['state']="disable"
 btn.update()
 window.protocol("WM_DELETE_WINDOW", callback)
 window.after(5000,T.destroy) 
 window.after(5000,refresh)
 
 #return "Running"
 

def tail(x):
 #print state1
 drive = os.environ['systemdrive']
 if state1 == 'scan':
   logfile = open(drive+r'\win7usmt\amd64\usmt.log','r') 
 #  print logfile
 if state1 == 'load':
   logfile = open(drive+r'\win7usmt\amd64\load.log','r')
   
 global window
 #global T
 global scrollbar
 
 window = Toplevel(master)
 
 scrollbar = Scrollbar(window)
 scrollbar.pack(side=RIGHT, fill=Y)
 window.geometry("1000x700+300+300") 
 T = Text(window, height=50, width=150)
 T.pack()
 
 T.insert(END,logfile.read())
 T.config(yscrollcommand=scrollbar.set)
 scrollbar.config(command=T.yview)
 T.see(END)
 x=1
 logfile.close()
 #
 btn['state']="disable"
 btn.update()
 window.protocol("WM_DELETE_WINDOW", callback)
 window.after(5000,T.destroy)
 window.after(5000,refresh)
  
 
 return "Exiting"
 #root.after(5000,tail,x)
 #root.after(5000,root.destroy)
 
 
 
 #root.after(30000,root.destroy) 
 #log = open(r'c:\win7usmt\amd64\usmt.log','r')	
 
 
 
  
 



####################################################################
def extractstate(usmtcmd,des,astate):
 try:
	  drive = os.environ['systemdrive']
	  os.mkdir(drive+r'\recovery_usmt')
 except:
          print "Recovery Folder Already Created"
 try:     
	  drive = os.environ['systemdrive']
	  os.chdir(drive+r'\win7usmt\amd64')
	  
	  print os.getcwd()
          aa=r'/i:MigDocs.xml'
	  bb=r'/i:MigApp.xml'
	  aaa=r'/i:Note.xml'
	  bbb=r'/i:Win10.xml'
	  cc=r'/progress:prog.log'
	  dd=r'/v:13'
	  ee=r'/l:load.log'
          ff=r'/decrypt:AES_256'
	  gg=r'/key:"SomePassword"'
	  hh=r'/ue:*'
	  #ii = usmtcmd
          x=chr(92)
	  domain=r'domainname'+x
	  ii = r'/ui:'
	  jj = des
	  kk=r'/all'
	  ll=r'/lac'
	  mm=r'/lae'
	  nn=r'/c'
	  oo=r'/extract'
	  rr=drive+r'\recovery_usmt'
	  astate = astate
          ##############
	  cmdarray= [r'usmtutils.exe',oo,jj,rr,ff,gg]
	  index=0
	   
          for uu in usmtcmd:
	  # print users[index]
	  #x=chr(92)
	  #domain=r'domainname'+x
	  #usmtcmd = usmtcmd + r'/ui:'+domain+users[index]+r' '
	    cmdarray.append(ii+usmtcmd[index])
	    index += 1

          if astate == 'all':
           btn1['state']="disable"
           btn1.update()
	   btn2['state']="disable"
	   btn2.update()
	   btn['state']="disable"
	   btn.update()
           startupinfo = subprocess.STARTUPINFO()		  
	   subprocess.Popen([r'usmtutils.exe',oo,jj,rr,ff,gg,])
          else:
	    btn1['state']="disable"
            btn1.update()
	    btn2['state']="disable"
	    btn2.update()
	    btn['state']="disable"
	    btn.update()
            startupinfo = subprocess.STARTUPINFO()		  
	    #subprocess.Popen([r'loadstate.exe',jj,aa,bb,cc,dd,ee,ff,gg,kk,ll,mm,hh,ii])
	    subprocess.Popen(cmdarray)
	     
	 #print "c:\win7usmt\\amd64\loadstate.exe "+usmtcmd
	 #master.destroy()
	 #sys.exit()
 except:
	 print "Failed to launch Extract USMT"


def loadstate(usmtcmd,des,astate):
 try:     
	  drive = os.environ['systemdrive']
	  os.chdir(drive+r'\win7usmt\amd64')
	  print os.getcwd()
          aa=r'/i:MigDocs.xml'
	  bb=r'/i:MigApp.xml'
	  aaa=r'/i:Note.xml'
	  bbb=r'/i:Win10.xml'
	  cc=r'/progress:prog.log'
	  dd=r'/v:13'
	  ee=r'/l:load.log'
          ff=r'/decrypt:AES_256'
	  gg=r'/key:"SomePassword"'
	  hh=r'/ue:*\*'
	  #ii = usmtcmd
          x=chr(92)
	  domain=r'domainname'+x
	  ii = r'/ui:'
	  jj = des
	  kk=r'/all'
	  ll=r'/lac'
	  mm=r'/lae'
	  nn=r'/c'
	  astate = astate
          ##############
	  cmdarray= [r'loadstate.exe',jj,aa,bb,aaa,bbb,cc,dd,ee,ff,gg,ll,mm,nn,hh]
	  index=0
	   
          for uu in usmtcmd:
	  # print users[index]
	  #x=chr(92)
	  #domain=r'domainname'+x
	  #usmtcmd = usmtcmd + r'/ui:'+domain+users[index]+r' '
	    cmdarray.append(ii+usmtcmd[index])
	    index += 1

          if astate == 'all':
           btn1['state']="disable"
           btn1.update()
	   btn2['state']="disable"
	   btn2.update()
	   btn['state']="active"
	   btn.update()
           startupinfo = subprocess.STARTUPINFO()		  
	   subprocess.Popen([r'loadstate.exe',jj,aa,bb,aaa,bbb,cc,dd,ee,ff,gg,kk,ll,mm,nn])
           #print "Going to Run"
          else:
	    btn1['state']="disable"
            btn1.update()
	    btn2['state']="disable"
	    btn2.update()
	    btn['state']="active"
	    btn.update()
            startupinfo = subprocess.STARTUPINFO()		  
	    #subprocess.Popen([r'loadstate.exe',jj,aa,bb,cc,dd,ee,ff,gg,kk,ll,mm,hh,ii])
	    subprocess.Popen(cmdarray)
            #print "Going to individual"
	     
	 #print "c:\win7usmt\\amd64\loadstate.exe "+usmtcmd
	 #master.destroy()
	 #sys.exit()
 except:
	 print "Failed to launch USMT"


def runusmt(usmtcmd,des,astate):
 try:    
	  drive = os.environ['systemdrive']
	  os.chdir(drive+r'\win7usmt\amd64')
	  print os.getcwd()
	  #print os.listdir(r'c:\win7usmt\amd64')
	  aa=r'/i:MigDocs.xml'
	  bb=r'/i:MigApp.xml'
	  aaa=r'/i:Note.xml'
	  bbb=r'/i:Win10.xml'
	  ccc=r'/config:config.xml'
	   
	  cc=r'/progress:prog.log'
	  dd=r'/v:13'
	  ee=r'/l:usmt.log'
          ff=r'/encrypt:AES_256'
	  gg=r'/key:"SomePassword"'
	  hh=r'/ue:*\*'
	  x=chr(92)
	  domain=r'domainname'+x
	  ii = r'/ui:'
	  jj = des
	  kk = r'/c'
	  ll = r'/localonly'
	  astate = astate
	  cmdarray= [r'scanstate.exe',jj,aa,bb,aaa,bbb,ccc,cc,dd,ee,ff,gg,kk,hh,ll]
	  index=0

          for uu in usmtcmd:
	  # print users[index]
	  #x=chr(92)
	  #domain=r'domainname'+x
	  #usmtcmd = usmtcmd + r'/ui:'+domain+users[index]+r' '
	    cmdarray.append(ii+usmtcmd[index])
	    index += 1

	  if astate == 'all':
	    btn1['state']="disable"
            btn1.update()
	    btn2['state']="disable"
	    btn2.update()
	    btn['state']="active"
	    btn.update()

	    startupinfo = subprocess.STARTUPINFO()
	    subprocess.Popen([r'scanstate.exe',jj,aa,bb,aaa,bbb,ccc,cc,dd,ee,ff,gg,kk,ll])
          else:
	    btn1['state']="disable"
            btn1.update()
	    btn2['state']="disable"
	    btn2.update()
	    btn['state']="active"
	    btn.update()
            startupinfo = subprocess.STARTUPINFO()
	    #subprocess.Popen([r'scanstate.exe',jj,aa,bb,cc,dd,ee,ff,gg,hh,ii])
	    
            
	    
	     
	    subprocess.Popen(cmdarray)
	    
	  #print "c:\win7usmt\\amd64\scanstate.exe "+usmtcmd
	 # master.destroy()
	 # sys.exit()
 except:
	  print "Failed to launch USMT"

def var_states(sidlist,des,astate,userlist):
	       	 
		#print map((lambda v1: v1.get()), boxlist)
                templist = list(map((lambda v1: v1.get()), boxlist))
		#print templist
                #print sidlist
		ix=0
		for ss in templist:
			#print ss
			if ss == 1:
			   #print sidlist[ix]
			   users.append(sidlist[ix])
			   print "Migrating This User: "+userlist[ix]
			ix += 1
		usmtcmd = users
		print usmtcmd
 		if len(usmtcmd) == 0:
   		 print "Please Re-Run! No Users Found on this PC to Migrate"
   		 return "Exiting"
		else:
		 window1.destroy() 	
		 runusmt(usmtcmd,des,astate)
  		 btn1['state']="disable"
  		 btn1.update()
		
		 return "Exiting"

def callback4():
 	 window1.destroy()
	 btn1['state']="active"
 	 btn1.update()
         return "Exiting"



def local(usmtcmd,des,astate):
 global window1 	
 window1 = Toplevel(master)
 btn1['state']="disable"
 btn1.update()
 btn2['state']="disable"
 btn2.update() 
 window1.protocol("WM_DELETE_WINDOW", callback4) 
 #window1.geometry("50x250+50+50")
 TT = Text(window1)
 TT.grid(row=0, column=0)
 scrollbar = Scrollbar(window1,orient=VERTICAL,command=TT.yview)
 scrollbar.grid(row=0,column=1,sticky='ns') 
 TT.config(yscrollcommand=scrollbar.set)
 
 #scrollbar.config(command=TT.yview)
 index1 = 1
 index2 = 0
 global boxlist
 boxlist = []
 sidlist = []
 userlist = []
 v = {}
 drive = os.environ['systemdrive']
 for directories in os.listdir(drive+r'\Users'):
      #print "Looking up: "+directories
      
      try:	
	           #localdir, domain, type = win32security.LookupAccountName("", directories)
		   #print iiii
		   
		   #sid_l = win32security.ConvertSidToStringSid(localdir)
		   aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

		   aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList")
		   
		   for i in range(1024):
    			try:
        		   asubkey_name=EnumKey(aKey,i)
        	           asubkey1=OpenKey(aKey,asubkey_name)
			   val=QueryValueEx(asubkey1, "ProfileImagePath")
			   val = val[0]
			   val = val.lower()
			   x1 = chr(92)
			   pathname = drive+r'\Users'+x1+directories
			   pathname = pathname.lower()
			   #print pathname
			   #print val
			   if val == pathname:
				
				#v["var{0}".format(index1)]=IntVar()
				var = IntVar()
			        #print index1
				
				#print sorted(v)
				
				#vv = sorted(v)
				#print vv
				#global vv1
				#vv1 = sorted(v)
				#v1 = (vv.pop(index2))	
			        
				#print v1
				
					
				  
				print "User found: "+directories+" and has this SID: "+asubkey_name
				box = Checkbutton(TT, text=directories, variable=var).grid(row=index2, sticky=W)
				boxlist.append(var)
				sidlist.append(asubkey_name)
				userlist.append(directories)
				index1 += 1
				index2 += 1
				break
    			except EnvironmentError:
				break    
      except:
	          print "Error No SID Found"
 #var1 = IntVar()
 #Checkbutton(T, text="male", variable=var1).grid(row=1, sticky=W)
 #var2 = IntVar()
 #Checkbutton(T, text="female", variable=var2).grid(row=2, sticky=W)
 
 
 Button(TT, text='Quit', command=callback4).grid(row=index2+1, sticky=W, pady=4)
 Button(TT, text='Create USMT', command=lambda:var_states(sidlist,des,astate,userlist)).grid(row=index2+2, sticky=W, pady=4)
 window1.resizable(False,False)

def mkdir(dtest):
	global msg3
	global i
	drive = os.environ['systemdrive']
	if (dtest == False):
		msg3 = 'Making '+drive+' win7usmt \n'
		os.mkdir(drive+r'\win7usmt')
	#i = r'C:'
	i = drive	
	shell.SHFileOperation ((0, shellcon.FO_COPY, netpath, drive+r'\win7usmt',shellcon.FOF_NOCONFIRMATION,None,None))
			#os.system ("xcopy /s %s %s" % ( r'C:\ptctemp', r'C:\ptcstart'))
	msg3 = msg3 + " Copying USMT\n"
	#i = r'C:'
	i = drive
	print "SystemDrive: "+drive
	return


def userinput():
 while True:	
  name = raw_input("Is this the user?(n)")
 
  if name == "y" or name == "n":
    	   
        print name 
  	return name
  if name == "":
	name = "" 
	print name
        return name	 
  print "Please (y) for Yes and (n) for No"  	
 #userinput()


def creategroup(state1):
 #bb =  raw_input("Enter users last names with commas spearating the names?")
 btn3['state']="disable"
 btn3.update()
 btn2['state']="disable"
 btn2.update()
 btn1['state']="disable"
 btn1.update()
 bb = e1.get()
 des = e2.get()
 bb = bb.lower()
 astate = ''
 usmtcmd = ''

 if bb == '' and state1 == 'extract':
    #usmtcmd = " /i:MigDocs.xml /i:migapp.xml " + des + " /progress:prog.log /v:13 /all /lac /lae /l:load.log /decrypt /key:\"Windows10\""
    astate = 'all'
    btn['state']="active"
    btn.update()
    extractstate(usmtcmd,des,astate)
    return "Exiting"	


 
 if bb == '' and state1 == 'load':
    #usmtcmd = " /i:MigDocs.xml /i:migapp.xml " + des + " /progress:prog.log /v:13 /all /lac /lae /l:load.log /decrypt /key:\"Windows10\""
    astate = 'all'
    btn['state']="active"
    btn.update()
    loadstate(usmtcmd,des,astate)
    return "Exiting"

 if bb == '' and state1 == 'scan':
    #usmtcmd = " /i:migdocs.xml /i:migapp.xml " + des + " /progress:prog.log /v:13 /l:usmt.log /encrypt /key:\"Windows10\""
    astate = 'all'
    btn['state']="active"
    btn.update()
    runusmt(usmtcmd,des,astate)
    return "Exiting"
 if bb == 'local' and state1 == 'scan':
    local(usmtcmd,des,astate)
    return "Exiting"
 bb = bb.split(';')
 
# check_group(group)
# group = group.upper()
# owner = e3.get()
# owner = owner.upper()
# try:
#   new_group = adgroup.ADGroup.create(group, ou, security_enabled=True, scope='UNIVERSAL', optional_attributes = {"description":owner})
#   print "Just Created The New Group " +group 
# except:
#   print "The group already exists!"
#   new_group = group
 for i in range(len(bb)):
   str = bb[i]
   str = str[ str.find("<")+1 : str.find(">") ]
   str = str.lower()
   print "Looking UP "+bb[i].title() +" and "+ bb[i].lower()
   u = bb[i].title()
   sa = bb[i].lower()
   if "@battelle.org" in str:
     u = str.lower()
     sa = str.lower()
   try:  
     q = adquery.ADQuery()
   except:
     print "Cannot Not Query Domain  "

   try:
     q.execute_query(
       attributes = ["cn","sAMAccountName","userPrincipalName"],
       where_clause = "objectClass = '*'",
       base_dn = "DC=domain, DC=domain, DC=domain"
       )
   except:
       print "Query Failed" 
 
   for row in q.get_results():
	try:
		i = row["cn"]
		ii = row ["sAMAccountName"].lower()
		iii = row["userPrincipalName"].lower()
		
		i2 = u
		i3 = sa
		if i2 in i or i3 in iii:
		  print "Name:"+i
		  print "Email:"+ii
		  print "Logon:"+iii
		   
		  name = userinput()
		  
		  
	          if name == "n" or name == "":
	           print "You answered No"		  
		   name = "n"	  
                   name2 = name.lower()
		   #print  "Answered No: "+name2
                  name2 = name.lower()
		  if name2 == "y": 
		   b = i
		   print "Answered Yes, Looking up user: "+b
		   user1 = aduser.ADUser.from_cn(b)
		   print user1
		   iiii, domain, type = win32security.LookupAccountName("", ii)
		   print iiii
		   
		   sid_ = win32security.ConvertSidToStringSid(iiii)
		   aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
                   print sid_
                   if state1 == 'scan':
		    aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList")
		    for i in range(1024):
    			try:
        		   asubkey_name=EnumKey(aKey,i)
        	            
			   if asubkey_name == sid_:
				print "User found: "+ii+" and has this SID: "+sid_
				users.append(sid_)
				break
    			except EnvironmentError:
				break        

		
                   
	       #	   try:
	       #       new_group.add_members([user1])
		      #new_group.sync_membership([user1])
		#   except:
	        #      print "Adding New Users "+b
		#      new_group1 =  adgroup.ADGroup.from_cn(group)
		#      isthere = new_group1.check_contains_member(user1)
		#     if isthere == True:
		#        print "User Already in Group"	      
	              #new_group1 =  adgroup.ADGroup.from_cn(group)
	      	#      else:
		#        new_group1.add_members([user1])
		   
		   
		   
		   #print sid_
		   if state1 == 'load':

	             users.append(sid_)	   
		     break

        except:
	        a = ""
 #listgroup(new_group,group)
 print users
 #len(users)
 #print len(users)
 if state1 == 'scan':
	 #aa=r'/i:MigDocs.xml '
	 #bb==r'/i:MigDocs.xml '
	 #cc=r'/progress:prog.log '
	 #dd=r'/v:13 '
	 #ee=r'/l:usmt.log '
	 #ff=r'/encrypt '
	 #gg=r' /key:\"Windows10\" '
	 #hh=r' /ue:*\*'
	 
	 #usmtcmd = r'/i:MigDocs.xml /i:MigApp.xml /progress:prog.log /v:13 /l:usmt.log /encrypt /key:\"Windows10\" /ue:*\*'
	 usmtcmd = ""
 if state1 == 'load':
  #usmtcmd = " /i:migdocs.xml /i:migapp.xml " + des + " /progress:prog.log /v:13 /lac /lae /l:load.log /decrypt /key:\"Windows10\" /ue:*"
   usmtcmd = ""
 #index=0
 #for uu in users:
	  #print users[index]
	  #x=chr(92)
	  #domain=r'domainname'+x
	  #usmtcmd = usmtcmd + r'/ui:'+domain+users[index]+r' '
	  #usmtcmd = users[index]
	  #index += 1
 usmtcmd = users

 if len(usmtcmd) == 0:
   print "Please Re-Run! No Users Found on this PC to Migrate"
   btn3['state']="active"
   btn3.update()
   btn1['state']="active"
   btn1.update()
   return "Exiting" 	 
  

 #print usmtcmd
 if state1 == 'scan':
  runusmt(usmtcmd,des,astate)
  btn['state']="active"
  btn.update()
  btn3['state']="disable"
  btn3.update()
  return "Exiting"
 if state1 == 'load':
  loadstate(usmtcmd,des,astate)
  btn['state']="active"
  btn.update()
  btn3['state']="disable"
  btn3.update()
  return "Exiting"
 print "Finished! Please Run Again or Quit!"
	 
	 

 
 
	 

dirs = ['C:', 'D:', 'E:', 'F:', 'G:' , 'H:', 'I:', 'J:', 'K:']

for i in dirs:
	if os.path.exists(i+'/win7usmt'):
	 msg3 = i + "\win7usmt exists" + '\n'
	 #e = Win32Environment(scope="user")
	 #e.setenv('START', i + '\ptcstart' )
	 break

dtest = os.path.exists(i+'/win7usmt')	

mkdir(dtest)

def state():
 global state1 	
 state1 = e3.get()
 #if state1 == '':
 # print "Please type a state:Load or Scan"
  
 state1 = state1.lower()
 if state1 == 'scan':
   drive = os.environ['systemdrive']	  
   logfile = drive+r'\win7usmt\amd64\usmt.log'	  
   
   creategroup(state1)
   return "Exiting" 
 if state1 == 'load':
   creategroup(state1)
   return "Exiting"
 if state1 == 'extract':
   creategroup(state1)
   return "Exiting" 
 else:
  print "Type Load or Scan"
  
#############################################################################
drive = os.environ['systemdrive']
for directories in os.listdir(drive+r'\Users'):
      #print "Looking up: "+directories
      
      try:	
	           #localdir, domain, type = win32security.LookupAccountName("", directories)
		   #print iiii
		   
		   #sid_l = win32security.ConvertSidToStringSid(localdir)
		   aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

		   aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList")
		   for i in range(1024):
    			try:
        		   asubkey_name=EnumKey(aKey,i)
        	           asubkey1=OpenKey(aKey,asubkey_name)
			   val=QueryValueEx(asubkey1, "ProfileImagePath")
			   val = val[0]
			   val = val.lower()
			   x1 = chr(92)
			   drive = os.environ['systemdrive']
			   pathname = drive+r'\Users'+x1+directories
			   pathname = pathname.lower()
			   #print pathname
			   #print val
			   if val == pathname:
				#print "User found: "+directories+" and has this SID: "+asubkey_name
				
				break
    			except EnvironmentError:
				break    
      except:
	          print "Error No SID Found"


def callback1():
	 ans.destroy()
	 btn3['state']="active"
 	 btn.update()
         return "Exiting"



def autofill(e1,e2,e3):
	def scan(e1,e2,e3):
	    e1.delete(0,END)	
	    e1.insert(0,r'Local')
	    path = e2.get()
	    path1 = path.lower()
	    pc = chr(92)+(socket.gethostname())
	    
	    pc = pc.lower()
	    val = path1.find(pc)
	    if val > 0:
		    
		    e2.delete(0,END)
		    e2.insert(0,path)
		    e3.delete(0,END)
	    	    e3.insert(0,r'scan')
		    btn3['state']="active"
  	   	    btn3.update()
	            ans.destroy()

		    return 
		
			
	    e2.insert(END,pc)
	    e3.delete(0,END)
	    e3.insert(0,r'scan')
	    btn3['state']="active"
  	    btn3.update()
	    ans.destroy()
	
	def load(e1,e2,e3):
	    e1.delete(0,END)	
	    e1.insert(0,r'')
	    path = e2.get()
	    
	    
	    
		
	    e2.delete(0,END)			
	    e2.insert(END,path)
	    e3.delete(0,END)
	    e3.insert(0,r'load')
	    btn3['state']="active"
  	    btn3.update()
	    ans.destroy()	
	
	global ans
	ans = Toplevel(master)
	ans.title("AutoFill Helper Window")
	msg = Message(ans, text="Choose between Scan(capture data) or Load(load data back)?")
	msg.grid(row=0,column=0, columnspan=2, sticky=E+N+S+W)
	ans.protocol("WM_DELETE_WINDOW", callback1)

	b1 = Button(ans, text="Scan", command = lambda:scan(e1,e2,e3))
	b1.grid(row=1,column=0,sticky=E+N+S+W)
	b2 = Button(ans, text="Load", command= lambda:load(e1,e2,e3))
	b2.grid(row=1,column=1,sticky=E+N+S+W)
	
	ans.rowconfigure(0,weight=1)
	ans.rowconfigure(1,weight=1)

	ans.columnconfigure(0,weight=1)
	ans.columnconfigure(1,weight=1)

	msg.rowconfigure(0,weight=1)
	b1.rowconfigure(1,weight=1)
	b2.rowconfigure(1,weight=1)
	msg.columnconfigure(0,weight=1)
	b1.columnconfigure(0,weight=1)
	b2.columnconfigure(1,weight=1)
        btn3['state']="disable"
  	btn3.update()

def term1():
	pid1 = e3.get()
	pid1 = pid1.lower()
	
	b = wmi.WMI ()
	if pid1 == 'scan':
	  try:	
		for process in b.Win32_Process (caption="scanstate.exe"):
		 print "Terminating scanstate.exe"
		 process.Terminate ()
	  except:
	         print "Error Cannot Find Process Scanstate.exe" 	 
	if pid1 == 'load':
	  try:
		for process in b.Win32_Process (caption="loadstate.exe"):
		 print "Terminating loadstate.exe"
		 process.Terminate ()
	  except:
		 
	     	print "Error Cannot Find Process Loadstate.exe"
        if pid1 == 'extract':
	  try:
		for process in b.Win32_Process (caption="usmtutils.exe"):
		 print "Terminating usmtutils.exe"
		 process.Terminate ()
	  except:
	 	print "Error Cannot Find Process usmtitils.exe"	  
	master.quit()
	
def callback3():
    if tkMessageBox.askokcancel("Quit", "Do you really wish to quit? This will stop any migration processes!"):
        term1()


################################################################################	


master = Tk()
master.title("User State Migration Helper")

#Label(master, text="Usage:LastName Comma Space First Initial or Email or LastName(ex: foo, b;foo@bar;foo)for Domain User(s) Lookup: Use Console to Answer Questions Once Create USMT Button is Clicked").grid(row=0,column=1,sticky=N)
l1 = Label(master, text="Users to Migrate:LookUp Domain Users(ex: foo, b;foo@bar;foo) | Blank To Gather All Users | Type: Local for Indivdual Users")
l1.grid(row=0,column=2,sticky=N+S+E+W)
l2 = Label(master, text="Users to Migrate:")
l2.grid(row=1,column=1,sticky=E+N+S+W)
l3 = Label(master, text="Drive Path(Migration Store")
l3.grid(row=2,column=1,sticky=E+N+S+W)
l4 = Label(master, text="USMT STATE(type load or scan")
l4.grid(row=3,column=1,sticky=E+N+S+W)

e1 = Entry(master,width=150)
e2 = Entry(master,width=150)
e3 = Entry(master,width=150)
e2.insert(0, r'\\server\share\DesktopDataMigration\USMT_Store')
#e3.insert(0, r'type load(load data back) or scan(gather data)')
#e1.insert(0,r'Leave Blank to gather all users or type username(s) separated by semicolons to select users')
e1.grid(row=1, column=2,sticky=N+S+E+W)
e2.grid(row=2, column=2,sticky=N+S+E+W)
e3.grid(row=3, column=2,sticky=N+S+E+W)

x = 0

btnq = Button(master, text='Quit', command = callback3)
btnq.grid(row=4, column=0, sticky=W+N+S+E, pady=4)
btn1 = Button(master, text='Run USMT', state="active", command=state)
btn1.grid(row=4, column=2, sticky=E+N+S+W, pady=4)
btn2 = Button(master, text='Aegis Local USB', state="active", command=usb)
btn2.grid(row=2, column=0, sticky=W+N+S+E, pady=0)
btn = Button(master, text='Log',state="disable", command = lambda:tail(x))
btn.grid(row=4, column=1, sticky=E+N+S+W, pady=4)

btn3 = Button(master, text='AutoFill',state="active", command = lambda:autofill(e1,e2,e3))
btn3.grid(row=0, column=0, sticky=E+N+S+W, pady=4)
btn3.rowconfigure(0,weight=1)
btn3.columnconfigure(0,weight=1)

master.rowconfigure(0,weight=1)
master.rowconfigure(1,weight=1)
master.rowconfigure(2,weight=1)
master.rowconfigure(3,weight=1)
master.rowconfigure(4,weight=1)

master.columnconfigure(0,weight=1)
master.columnconfigure(1,weight=1)
master.columnconfigure(2,weight=1)

l1.rowconfigure(0,weight=1)
l2.rowconfigure(1,weight=1)
l3.rowconfigure(2,weight=1)
l4.rowconfigure(3,weight=1)
l1.columnconfigure(2,weight=1)
l2.columnconfigure(1,weight=1)
l3.columnconfigure(1,weight=1)
l4.columnconfigure(1,weight=1)
e1.rowconfigure(1,weight=1)
e2.rowconfigure(2,weight=1)
e3.rowconfigure(3,weight=1)
e1.columnconfigure(2,weight=1)
e2.columnconfigure(2,weight=1)
e3.columnconfigure(2,weight=1)
btnq.rowconfigure(4,weight=1)
btnq.columnconfigure(0,weight=1)
btn1.rowconfigure(4,weight=1)
btn2.rowconfigure(2,weight=1)
btn.rowconfigure(4,weight=1)
btn1.columnconfigure(2,weight=1)
btn2.columnconfigure(0,weight=1)
btn.columnconfigure(1,weight=1)

master.protocol("WM_DELETE_WINDOW", callback3)


mainloop( )
