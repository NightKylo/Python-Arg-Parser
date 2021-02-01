# args.py

class Command:
    def __init__(self, name: str, description: str, required_params=None, optional_params=None):
        if required_params is None:
            required_params = []
        if optional_params is None:
            optional_params = []

        self.name = name
        self.description = description
        self.required_params = required_params
        self.optional_params = optional_params

    def __repr__(self):
        return self.name

    def __len__(self):
        return len(self.name)


class Parameter:
    def __init__(self, name: str, description: str, no_value_param: bool = False):
        self.name = name
        self.description = description
        self.no_value_param = no_value_param

    def __repr__(self):
        return self.name


class Register:
    def __init__(self):
        self.names = []
        self.all = []
        self.commands = []
        self.parameters = []

    def __contains__(self, item):
        for i in self.commands:
            if i == item:
                return True

        for i in self.parameters:
            if i == item:
                return True

        return False

    def __add__(self, other):
        if type(other) is Command:
            self.commands.append(other)
            self.all.append(other)
            self.names.append(other.name)
        elif type(other) is Parameter:
            self.parameters.append(other)
            self.all.append(other)
            self.names.append(other.name)
        else:
            raise Exception("Other has a not compatible type")

    def __sub__(self, other):
        if type(other) is Command:
            self.commands.remove(other)
            self.all.remove(other)
            self.names.remove(other.name)
        elif type(other) is Parameter:
            self.parameters.remove(other)
            self.all.remove(other)
            self.names.remove(other.name)
        else:
            raise Exception(f"Other has a not compatible type {type(other)}")

    def __repr__(self):
        return ", ".join(self.names)

    def __len__(self):
        return len(self.all)

    def __getitem__(self, name):
        for i in self.all:
            if i.name == name:
                return i
        raise IndexError(f"Self.all doesn't contain '{name}', Self.all: {self.all}")

    def merge(self, other):
        if type(other) is Register:
            for i in other.names:
                self.names.append(i)
            for i in other.commands:
                self.commands.append(i)
                self.all.append(i)
            for i in other.parameters:
                self.parameters.append(i)
                self.all.append(i)
        else:
            raise TypeError(f"Type of other is not Register its {type(other)}")

    def add(self, other):
        if type(other) is Command:
            self.commands.append(other)
            self.all.append(other)
            self.names.append(other.name)
        elif type(other) is Parameter:
            self.parameters.append(other)
            self.all.append(other)
            self.names.append(other.name)
        else:
            raise Exception(f"Other has a not compatible type {type(other)}")

    def remove(self, other):
        if type(other) is Command:
            self.commands.remove(other)
            self.all.remove(other)
            self.names.remove(other.name)
        elif type(other) is Parameter:
            self.parameters.remove(other)
            self.all.remove(other)
            self.names.remove(other.name)
        else:
            raise Exception(f"Other has a not compatible type {type(other)}")
