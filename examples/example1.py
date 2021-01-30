# example1.py Basic usage example

from arg_parser import *

reg = Register()
# You can use reg.add(item) or just a + sign to add commands or parameters to the register.
# You can remove them with reg.remove(item) or a - sign
reg.add(Command("--command", "This is just a basic command", ["-param"]))
reg + Command("--find", "Finds a substring inside a string", ["-str", "-substr"])
reg.add(Parameter("-str", "Any string"))
reg + Parameter("-substr", "Any substring")

parser = Parser(reg)


@parser("--find")
def find_handler(opts: dict):
    if opts["-str"].find(opts["-substr"]) > 0:
        print(f"Found substring at index {opts['-str'].find(opts['-substr'])}")
    else:
        print("It seems like the string doesn't contain the substring")


# This is called here because we didn't specify a handler for --command so it wouldn't start automatically.
# If we would have a handler for --command it would start immediately after the declaration.
parser.handle_commands()
