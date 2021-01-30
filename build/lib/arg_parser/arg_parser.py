# arg_parser.py

import sys
from .args import *


class Parser:
    def __init__(self, cmds: Register, call_handle_manual: bool = False):
        self.reg = Register()
        self.reg + Command("--help", "Prints the command usage")
        self.reg.merge(cmds)
        self.handlers = {}
        self.call_handle_manual = call_handle_manual
        self.args = self.parse_args()

    def __call__(self, cmd_to_handle):
        def decorator(func):
            if self.reg.names.__contains__(cmd_to_handle):
                self.handlers[cmd_to_handle] = func
                if len(self.handlers) == len(self.reg.commands) - 1:
                    if not self.call_handle_manual:
                        self.handle_commands()
            else:
                raise Exception(f"Command {cmd_to_handle} was not specified in commands: {self.reg.names}")

        return decorator

    def __repr__(self):
        return f"Parser instance from module {__name__}\ncommands: {self.reg}\nargs: {self.args}\nhandlers: " \
               f"{self.handlers}"

    def print_usage(self):
        usage = f"Usage:\n    {__file__} <command> [options]\n\nCommands\n"
        maxlen1 = 0
        maxlen2 = 0

        for name in self.reg.names:
            length1 = 4 + len(name) + 4
            length2 = 4 + len(name) if type(self.reg[name]) == Parameter else 4 + len(name) + \
                      len(" ".join(self.reg[name].required_params)) + len(" ".join(self.reg[name].optional_params))
            maxlen1 = length1 if length1 > maxlen1 else maxlen1
            maxlen2 = length2 if length2 > maxlen2 else maxlen2

        maxlen2 += 50

        for command in self.reg.commands:
            string = " " * 4 + command.name
            if len(command.required_params) > 0:
                string += " " * (maxlen1 - len(command)) + "[ " + ", ".join(command.required_params)
            elif len(command.optional_params) > 0:
                string += " " * (maxlen1 - len(command)) + "[ (" + ", ".join(command.optional_params) + ") ]"

            if len(command.required_params) > 0 and len(command.optional_params) > 0:
                string += ", (" + ", ".join(command.optional_params) + ") ]"
            elif len(command.required_params) > 0 and len(command.optional_params) == 0:
                string += " ]"

            string += " " * (maxlen2 - len(string)) + command.description + "\n"
            usage += string

        usage += "\nOptions\n"

        for param in self.reg.parameters:
            string = " " * 4 + param.name
            string += " " * (maxlen2 - len(string)) + param.description + "\n"
            usage += string

        print(usage)

    def parse_args(self):
        args = {}
        got_cmd = False
        for arg_index in range(len(sys.argv)):
            if sys.argv[arg_index][0] == "-":
                if sys.argv[arg_index][1] != "-":
                    try:
                        args[sys.argv[arg_index]] = sys.argv[arg_index + 1]
                        for arg in range(len(sys.argv)):
                            if arg > arg_index + 1:
                                if sys.argv[arg][0] != "-":
                                    args[sys.argv[arg_index]] += " " + sys.argv[arg]
                                else:
                                    break
                    except IndexError:
                        self.print_usage()
                elif not got_cmd:
                    args[sys.argv[arg_index]] = ""
                    got_cmd = True
        return args

    def handle_commands(self):
        for c in [arg for arg in self.args if self.args[arg] == ""]:
            try:
                for j in self.reg[c].required_params:
                    if not self.args.keys().__contains__(j):
                        print(f"Error executing command '{c}'. Required parameter '{j}' is missing")
                        self.print_usage()
                        return
                self.args.pop(c)
                self.handlers[c](self.args)
                return
            except KeyError:
                if c == "--help":
                    self.print_usage()
                    return
                print(f"No handler specified for command '{c}'")
                return
        self.print_usage()
