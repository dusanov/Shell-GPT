import cmd
from Shell import *

class CmdLoop(cmd.Cmd):
    """ Shell interface for OpenAI GPT Prompt """

    tokens_used = 0
    prompt = f' [{tokens_used}]: '
    last_output = ''

    def do_shell(self, line):
        "Run a shell command"
        output = os.popen(line).read()
        print (output)
        self.last_output = output

    def __init__(self, logfile):
        super().__init__()
        self.logfile = logfile
        print(f" -- logging to: {self.logfile.name}")

    def send_to_prompt(self, line):
        global tokens_used
        if len(line) > 9:
            tokens_used = do_a_prompt(line, self.logfile)
        else:
            print(f" -- prompt not long enough ")        

    def default(self, line):
        self.send_to_prompt(line)  

    def emptyline(self):
        pass

    def do_file(self, filepath):
        prompt = ''
        try:
            with open(f"{filepath}", "r") as promptfile:
                prompt = " ".join(promptfile.readlines()) 
            self.send_to_prompt(prompt)
        except Exception as e:
            print(f" -- {e}")

    
    def do_greet(self, person):
        if person:
            print (' -- hello,', person) 
        else:
            print(" -- hello stranger")

    def do_thx(self,_):
        if len(_) == 0:
            print(f"\n -- bye \n")
            return True  
        else:
            self.default(f"thx {_}")     

    def do_bye(self,_):
        if len(_) == 0:
            print(f"\n -- bye \n")
            return True      
        else:
            self.default(f"bye {_}")

    def do_quit(self,_):
        if len(_) == 0:
            print(f"\n -- bye \n")
            return True      
        else:
            self.default(f"quit {_}")

    def do_EOF(self, line):
        print(f"\n -- EOF {line} \n ")
        return True
    
    def postcmd(self, stop, line):
        return cmd.Cmd.postcmd(self, stop, line)