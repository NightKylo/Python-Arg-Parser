# Arg-Parser-Python
This simple script helps to parse the args a script is called with and makes printing command-usages much easier.

***Why to use it?***

When you want to get the args with ```sys.argv``` they have to be in the correct position and if one is missing the script crashes. A script working with ```sys.argv``` often looks like this:
```py .\script.py get name```.

If you integrate this script the args are registered like this and much easier to read out.
```py .\script.py --get -n name``` As you can see this is variable and could also be called like this ```... -n name --get```. Values can be accessed with ```args["-argname"]```

***Integration:***

Try to install this script with ```pip install arg_parser``` and then ```import arg_parser``` at the top of your script.
If this doesn't work you can download it from https://github.com/NightKylo/Python-Arg-Parser. After that put it into the same directory as your script. In your script add ```from arg_parser import *``` or if that doesn't work ```from . import arg_parser``` at the top.
Be aware that the better way is to install it via pip.

***Usage:***

To use the parser you have to initialize the ```Parser``` class via ```arg_parser.Parser(commands)``` (without the module name if you imported with *) where ```commands``` is a register-object created like that:
```reg = arg_parser.Register()```. You can register a command with ```reg + Command("--name", "description", ["-required_param"], ["-optional_param"])``` and a parameter with ```reg + Parameter("-name", "description")```. If there are no required or optional params just leave the list empty.

Now you have to specify the way a command shall be handled. It works like this: ```@parser("--command_name") def handle_command_name(args: dict): do_whatever_you_want()```. In the decorator above the function you have to pass the command eg ```--get``` and the parser will call it when the command is supplied. 
```args``` is in this case a dictionary of the given args form the structure ```{ "-optname": "value", "-optname": "value" }```. Be aware that this dictionary does not contain the given command, only the options.

If you want to start the handle process manually you can add a ```True``` to the initialization of the parser and a ```parser.handle_commands()``` when you want to handle them. By default, the parser handles the commands when all handler-functions are given.

Look at the example files at https://github.com/NightKylo/Python-Arg-Parser for more detailed information.
