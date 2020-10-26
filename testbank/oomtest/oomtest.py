#!/usr/bin/env python3
import subprocess, sys

def test_name():
    print("Out of Memory")

def run_command(cmd):
    print("Command executed : " + cmd)
    # Had to parse this command explictly since, Pythong doesn't like to add quotes in list properly
    process = subprocess.Popen(['/usr/bin/grep','-i','"Out of Memory"','/var/log/messages'], stdout=subprocess.PIPE, universal_newlines=True)

    # Little ugly, make a man fly and bird walk method to bypass grep error return code properly
    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code == 1:
            return_code = 0
            print('Return code : ', return_code)
            sys.exit(return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
        elif return_code == 0:
            return_code = 1
            print('Return code : ', return_code)
            sys.exit(return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())

if __name__=="__main__":
    cmd = ('/usr/bin/grep -i \'Out of Memory\' /var/log/messages*')
    test_name()
    run_command(cmd)





