# Arg-Parser-Python
This package helps to parse args from the command line or the terminal to a dictionary and calls registered functions when the individual command is given. This makes dealing with args much easier, more efficient and better ordered.

***Why to use it?***

When you want to get the args with ```sys.argv``` they have to be in the correct position and if one is missing the script crashes. Executing a script working with ```sys.argv``` often looks like this:
```py .\script.py get name```.

If you integrate this script the args are registered like this and much easier to read out.
```py .\script.py --get -n name``` As you can see this is variable and could also be called like this ```... -n name --get```. Values can be accessed with ```args["-argname"]```

***Integration:***

Try to install this script with ```pip install arg_parser``` and then ```from arg_parser import *``` at the top of your script.
If this doesn't work you can download it from https://github.com/NightKylo/Python-Arg-Parser. After that put it into the same directory as your script. In your script add ```from arg_parser import *``` at the top.
Be aware that the better way is to install it via pip.

***Usage:***

To use the parser you have to initialize the ```Parser``` class via ```Parser(commands)``` where ```commands``` is a register-object created like that:
```reg = Register()```. You can register a command with ```reg + Command("--name", "description", ["-required_param"], ["-optional_param"])``` and a parameter with ```reg + Parameter("-name", "description")```. If you want you can use ```reg.add(Parameter("-name", "description"))``` instead of ```+```. If there are no required or optional params remove the lists or put ```None```.

Now you need to specify how to handle a command. It works like this: ```@parser("--command_name") def handle_command_name(args: dict): do_whatever_you_want()```. In the decorator above the function you have to pass the command eg ```--get``` and the parser will call the function when the command is supplied. 
```args``` is in this case a dictionary of the given args form the structure ```{ "-optname": "value", "-optname": "value" }```. Be aware that this dictionary does not contain the given command, only the options.

If you want to start the handle process manually you can add a ```True``` to the initialization of the parser and a ```parser.handle_commands()``` when you want to handle them. By default, the parser handles the commands when all handler-functions are given.

Look at the example files at https://github.com/NightKylo/Python-Arg-Parser for more detailed information.

***How does it work***

If you want to know, how this package works go to https://github.com/NightKylo/Python-Arg-Parser/tree/main/arg_parser and look at the parser.py file.
