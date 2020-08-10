import progress
import os
import sys
import pwd

print('> Login: ' + pwd.getpwuid(os.getuid()).pw_name)
