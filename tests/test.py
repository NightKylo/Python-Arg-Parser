

from Tools.arg_parser.objects.arg_parser import *

reg = Register()
reg + Command("--get", "gets IP from github", ["-u", "-r", "-fp"], ["-p"])
reg + Parameter("-u", "Username")
reg + Parameter("-r", "Repo")
reg + Parameter("-fp", "FilePath")
reg + Parameter("-p", "Path")
parser = Parser(reg)


@parser("--get")
def get(opts):
    print(opts)
