import zipfile

zFile = zipfile.ZipFile('test.zip')
passFile = open('passwords.txt','r')

for line in passFile:
    try:

        password = line.strip('\n')
        zFile.extractall(pwd = password)
        print "[+] Password " + password
        break
    except Exception as e:
        print "[-] NOT MATCHED " + password
