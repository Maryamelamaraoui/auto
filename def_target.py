import os
import sys
import threading

file_object = ''
file_name = ''
folder_name = ''
target = ''
lock = threading.Lock()

# TARGET DEFINITION ===================================================================

def acquire_target():
    global target
    os.system('clear')
    target = input("Enter target URL (exclude www): ")
    print('\x1b[1;32m' + '\n[OK]\t' + '\x1b[0m' + 'Target Acquired')

# THE HARVESTER =======================================================================

def harvester():
    with lock:
        os.system('clear')
        print("\n[*]\tRunning TheHarvester\n[*]\tStep 1/6 in progress")
    global target
    global file_object
    cmd = 'theharvester -d ' + target + ' -b all'
    try:
        output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = output.communicate()
        if output.returncode != 0:
            print('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'Step 1 Failed! Check/Update prerequisitie packages. \nError: ' + err.rstrip())
            sys.exit(1)
        else:
            with lock:
                file_object.write('\nThe Harvester Output: \n')
                file_object.write('=========================================================================\n')
                file_object.write(str(out.rstrip()))
            print('\x1b[1;32m' + '\n[OK]\t' + '\x1b[0m' + 'Step 1 Executed\n')
    except:
        print("Something went wrong! Check prerequisites.\n")
    return 0

# WHOIS            =====================================================================================================================================
def whois():
    with lock:
        print("\n[*]\tRunning whois\n[*]\tStep 2/6 in progress")
    global target
    global fileObject
    cmd = 'whois' + ' ' + target
    try:
        output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = output.communicate()
        if output.returncode != 0:
            print('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'Step 2 Failed! Check/Update prerequisite packages. \nError: ' + err.rstrip())
            sys.exit(1)
        else:
            with lock:
                fileObject.write('\n\nWhois Output: \n')
                fileObject.write('=========================================================================\n')
                fileObject.write(str(out.rstrip()))
            print('\x1b[1;32m' + '\n[OK]\t' + '\x1b[0m' + 'Step 2 Executed\n')
    except Exception as e:
        print(f"Something went wrong! Check prerequisites. Error: {e}\n")
    return 0

# BUILTWITH         =====================================================================================================================================
def webtechnology():
    global target, folderName
    with lock:
        print("\n[*]\tConnecting to Robtex.com & Builtwith.com\n[*]\tStep 3/6 in progress")
    cmmd = 'curl -o Output/' + folderName + '/' + target + '_robtex_scan.html' + ' https://www.robtex.com/dns-lookup/' + target
    cmd = 'curl -o Output/' + folderName + '/' + target + '_builtwith_scan.html' + ' https://builtwith.com/' + target
    outPut = Popen(cmmd, shell=True, stdout=PIPE, stderr=PIPE)
    output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = output.communicate()
    out, err = outPut.communicate()
    try:
        if output.returncode != 0:
            print('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'Step 3 Failed! Check/Update prerequisite packages. \nError: ' + err.rstrip())
            sys.exit(1)
        else:
            print('\x1b[1;32m' + '\n[OK]\t' + '\x1b[0m' + 'Step 3 Executed\n')
    except Exception as e:
        print(f"Something went wrong! Check prerequisites. Error: {e}\n")
    return 0

# DNS RECON         =====================================================================================================================================
def dnslookup():
	with lock:
		print ("\n[*]\tRunning DNSrecon\n[*]\tStep 4/6 in progress")
	global target
	global fileObject
	cmd = 'dnsrecon -d' + ' ' + target
	output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out, err = output.communicate()
	try:
		if(output.returncode != 0):
			print ('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'Step 4 Failed Check/Update prerequisitie packages. \nError: ' + err.rstrip())
			sys.exit(1)
		else:
			#print "Return code: ", output.returncode
			#print out.rstrip(),err.rstrip()
			with lock:
				fileObject.write('\nDNS Recon Output: \n')
				fileObject.write('=========================================================================\n')
				fileObject.write(str(out.rstrip()))
			print ('\x1b[1;32m' + '\n[OK]\t' + '\x1b[0m' + 'Step 4 Executed\n')
	except:
		print ("Something went wrong! Check prerequisities.\n")
		# sys.exit(1)
	return 0

# METAGOOFIL         =====================================================================================================================================
def metagoofil():
	with lock:
		print ("\n[*]\tRunning metagoofil\n[*]\tStep 5/6 in progress")
	global target
	global fileObject
	cmd = 'metagoofil -d ' + target + ' -t pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx -l 10 -n 1 -o Output/' + folderName + '/' + 'metagoofil_file_downloads -f Output/' + folderName + '/metagoofil_scan_output.html' 
	output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out, err = output.communicate()
	try:
		if(output.returncode != 0):
			print ('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'Step 5 Failed! Check/Update prerequisitie packages. \nError: ' + err.rstrip())
			sys.exit(1)
		else:
			#print "Return code: ", output.returncode
			#print out.rstrip(),err.rstrip()
			with lock:
				fileObject.write('\nMetagoofil Output: \n')
				fileObject.write('=========================================================================\n')
				fileObject.write(str(out.rstrip()))
			print ('\x1b[1;32m' + '\n[OK]\t' + '\x1b[0m' + 'Step 5 Executed\n')
	except:
		print ("Something went wrong! Check prerequisities.\n")
		# sys.exit(1)
	return 0

# KNOCKPY           =====================================================================================================================================
def knockDomain():
	with lock:
		print ("\n[*]\tRunning knockpy. This step can take ~15 mins. to complete.\n[*]\tStep 6/6 in progress")
	global target
	global fileObject, GITHUB, fileName, folderName
	cmd = 'knockpy ' + target 
	output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out, err = output.communicate()
	try:
		if(output.returncode != 0):
			print ('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'Step 6 Failed! Check/Update prerequisitie packages. \nError: ' + err.rstrip())
			fileObject.close()
			sys.exit(1)
		else:
			#print "Return code: ", output.returncode
			#print out.rstrip(),err.rstrip()
			with lock:
				fileObject.write('\nKnockpy Subdomain Scan Output: \n')
				fileObject.write('=========================================================================\n')
				fileObject.write(str(out.rstrip()))
			print ('\x1b[1;32m' + '\n[OK]\t' + '\x1b[0m' + 'Results have been saved to /Output/%s/%s '%(folderName, fileName))
			print ('\x1b[1;32m' + '\n[OK]\t' + '\x1b[0m' + 'Step 6 Executed\n' + '\x1b[1;32m' + '[OK]\t' + '\x1b[0m' + 'Mission Over')
			print ("\nThank you for using %s" %NAME )
			print ("For suggestions %s" %TWITTER)
			print ("To contribute, visit %s\n" %GITHUB)
	except:
		print ("Something went wrong! Check prerequisities.\n")
		sys.exit(1)
	return 0

# INFORMATION           =====================================================================================================================================
def info():
	global target
	global fileObject, GITHUB
	os.system('clear')
	cmd = 'cat README.txt' 
	output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out, err = output.communicate()
	try:
		if(output.returncode != 0):
			print ('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'README.txt missing. You can download it by visiting %s \n'%GITHUB + err.rstrip())
			sys.exit(1)
		else:
			#print "Return code: ", output.returncode
			print (out.rstrip())
	except:
		sys.exit(1)
	return 0

# MAIN =================================================================================

if __name__ == '__main__':
    # global file_object
    # global file_name, folder_name, target
    print ("------------------------------------------------------------")
    print ('\x1b[1;31m' + '\n\t\t\   DARK ARMOURED RECON   /' + '\x1b[0m')
    print ('\x1b[1;31m' + '\t\t \    TIP OF THE SPEAR    /' + '\x1b[0m')
    print ('\x1b[1;34m' + '\nLight Armoured Recon v1.2' + '\x1b[0m')
    print ('\x1b[1;34m' + 'ENIRCK, B.' + '\x1b[0m')
    print ('\x1b[1;34m' + '@Praetorian_GRD' + '\x1b[0m')
    print ("------------------------------------------------------------")
    try:
        while True:
            print ("\n------------------------------------------------------------")
            print ("1.\tEnter Target Information")
            print ("2.\tCreate Output File")
            print ("3.\tInitiate Recon")
            print ("4.\tREADME")
            print ("------------------------------------------------------------")
            if not target:
                print ('\x1b[1;31m' + '\n[!]\t' + '\x1b[0m' + 'Target missing. Select 1 to enter target URL')
            else:
                print ('\x1b[1;32m' + '\n[OK]\t' + '\x1b[0m' + 'Scope: %s' % target)

            if not file_name:
                print ('\x1b[1;31m' + '[!]\t' + '\x1b[0m' + 'Select 2 to enter output file name')
            option = int(input("\nEnter your option or Press Ctrl+C to exit: "))
            if option == 1:
                acquire_target()
    except KeyboardInterrupt:
        sys.exit(0)
