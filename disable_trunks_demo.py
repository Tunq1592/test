import os
for i in range (1,18):
	os.system ("fwconsole trunk --disable %d" %(i)) 
os.system ("fwconsole ma install contactmanager")
os.system ("fwconsole reload")
