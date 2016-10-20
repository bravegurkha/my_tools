'''

    Unix Password Cracker Python Script
    @creator Swornim Shrestha
    @email srestaswrnm@gmail.com
    Oct 20 2016 Wed 2:44 PM

    Usage:
    python3 unixcracker.py -f <password filename> -d <dictionary  filename>
'''


import crypt #Importing Crypt Function
import optparse #For parsing arguments

def testPassword(cryptPass,dictionary): #Function to test password
    salt = cryptPass[0:2] #Catching the salt from the encrypted password. First two characters are called salt.
    dictFile = open(dictionary, "r") # Opening dictionary file

    for word in dictFile.readlines(): # Read all the lines
        try:
            word = word.split("\n")[0] # Split new line tags \n
            cryptWord = crypt.crypt(word,salt) # Crypting the words from wordlist with salt
            if (cryptWord == cryptPass): # Comparing the password
                print("[*] Found password %s" % word) # If password
                break; # Breaking the loop after password is matched

        except Exception: # IF the password doesn't match
            print("[!] No Password Found") # pASSWORD Not Found


def main():
    parser = optparse.OptionParser("Usage unixcracker.py -f password_file -d dictionary file") # Setting up argument parser
    parser.add_option("-f",dest="passwordFilename",type="string",help = "Sepecify Password File")
    parser.add_option("-d",dest="dictFilename",type="string",help= "Specify dictionary filename")

    (options, args) = parser.parse_args() # Getting arguments

    if(options.passwordFilename == None ) | (options.dictFilename == None): # If the password filename and dictionary filename is blank
        print (parser.usage) # Print the usages
        exit(0)

    else:
        ## Assiging filenames
        passwordFilename = options.passwordFilename
        dictFilename = options.dictFilename

    passFile = open(passwordFilename , "r") # Opening the file

    for line in passFile.readlines(): # Reading lines
        if ":" in line:
            user = line.split(":")[0] # Splitting and getting the username
            cryptPass = line.split(":")[1].strip(" ") # Splitting and getting the hash password
            print("[*] Cracking Password For %s" %user)
            testPassword(cryptPass,dictFilename) # Using function testPassword


if __name__ == "__main__":
    main()
