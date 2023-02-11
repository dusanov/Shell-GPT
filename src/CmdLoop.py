import os
import cmd
from typing import Any
from Shell import reset_session, \
                    do_a_prompt, \
                    list_models, \
                    current_model, \
                    set_model, \
                    num_tokens_from_string

class CmdLoop(cmd.Cmd):
    """ Shell interface for OpenAI Chat GPT Prompt """

    prompt = f' [0]: '
    last_output = ''

    def do_set_model(self,line):
        if len(line) > 0:
            set_model(line)
            print(f"\n -- model set to:\n {current_model()} \n")
        else:
            print(f" -- please provide model name")

    def do_current_model(self,line):
        if len(line) == 0:
            print(f"\n -- current model:\n {current_model()} \n")
        else:
            self.default(f"current models {line}")

    def do_list_models(self,line):
        if len(line) == 0:
            print(f"\n -- available models:\n {list_models()} \n")
        else:
            self.default(f"list models {line}")

    def do_reset_session(self,line):
        if len(line) == 0:
            print(f"\n -- session reset \n")
            reset_session()
        else:
            self.default(f"reset {line}")

    def do_shell(self, line):
        "Run a shell command by typing '!' "
        output = os.popen(line).read()
        print (output)
        self.last_output = output

    def __init__(self, logfile):
        self.logfile = logfile
        super().__init__()
    
    def do_logfilename (self, line):
        if len(line) == 0:
            print(f"\n -- logging to: {self.logfile.name}\n")
        else:
            self.default(f"logfilename {line}")        

    def send_to_prompt(self, line):
        if len(line) > 9:
            tokens_used = do_a_prompt(line, self.logfile)
            self.prompt = f' [{tokens_used}]: '
        else:
            print(f"\n -- prompt not long enough \n")        

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

    def do_exit(self,_):
        if len(_) == 0:
            print(f"\n -- bye \n")
            return True      
        else:
            self.default(f"exit {_}")

    def do_EOF(self, line):
        print(f"\n -- EOF {line} \n ")
        return True
    
    def completedefault(self, *ignored: Any):
        print(f"\r [{num_tokens_from_string(ignored[1])}]: {ignored[1]}", end='')