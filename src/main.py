import os
import sys
import re
import traceback
from CmdLoop import CmdLoop

prompt = " ".join(sys.argv[1:])
pattern = re.compile('[^A-Za-z0-9_.-]')
filename = prompt.replace(' ', '')[6:36]
if len(filename) > 0:
    filename = re.sub(pattern=pattern,repl='',string=filename)
else: 
    filename = "default"
path = "chat-sessions/"
isExist = os.path.exists(path)

try:    
    if not isExist:
        os.makedirs(path)

    if __name__ == '__main__':
        with open(f"{path}{filename}.log", "a+") as logfile:
            loop = CmdLoop(logfile)
            if len(prompt) > 0:
                loop.onecmd(prompt)
            loop.cmdloop()
except Exception as err:
    print (f" oopsy! \n{err} \n{traceback.print_exc()}")
