import os
import sys
import re
import traceback
from CmdLoop import CmdLoop

if __name__ == '__main__':
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
        with open(f"{path}{filename}.log", "a+") as logfile:
            if len(prompt) > 0:
                CmdLoop(logfile).onecmd(prompt)
            CmdLoop(logfile).cmdloop()
            print(f"\n -- bye -- \n")
    except Exception as err:
        print (f" oopsy! \n{err} \n{traceback.print_exc()}")
