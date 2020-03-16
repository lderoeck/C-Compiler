from Source.Types import *


class TypeTable:
    def __init__(self):
        self.tables = list()

    def enter_scope(self):
        self.tables.append(dict())

    def leave_scope(self):
        if len(self.tables) != 0:
            self.tables.pop()

    def insert_variable(self, name, value_type, **kwargs):
        if name in self.tables[-1]:
            return False
        if value_type == "char":
            self.tables[-1][name] = Entry(Char, **kwargs)
        elif value_type == "int":
            self.tables[-1][name] = Entry(Int, **kwargs)
        elif value_type == "float":
            self.tables[-1][name] = Entry(Float, **kwargs)
        else:
            self.tables[-1][name] = Entry(value_type, **kwargs)
        return True

    def lookup_variable(self, name):
        for i in range(1, len(self.tables) + 1):
            if name in self.tables[-i]:
                return self.tables[-i][name]
        return None

    def insert_function(self, name, parameters, value_type):
        key = tuple(name) + tuple(parameters)
        if len(self.tables) != 1:
            return False
        if key in self.tables[-1]:
            return False
        self.tables[-1][key] = Entry(value_type)
        return True

    def lookup_function(self, name, parameters):
        key = tuple(name) + tuple(parameters)
        return self.lookup_variable(key)

    def __str__(self):
        str = ''
        for i in self.tables:
            str += i.__str__()
        return str


class Entry:
    def __init__(self, value_type, **kwargs):
        self.type = value_type

        self.pointer = kwargs.get("pointer") or False
        self.const = kwargs.get("const") or False

        self.value = kwargs.get("value")
        # Location of variable in the register
        self.register = kwargs.get("register")
        # Location of variable on the stack (if applicable)
        self.location = kwargs.get("location")

    def update_value(self, new_value):
        if not isinstance(new_value, self.type):
            print("Mismatched types")
        self.value = new_value

    def __str__(self):
        return "Type: %s %s%s, Value: %s" % (
            "const" if self.const else "", str(self.type), "*" if self.pointer else "", str(self.value))

    def __repr__(self):
        return "Type: %s %s%s, Value: %s" % (
            "const" if self.const else "", str(self.type), "*" if self.pointer else "", str(self.value))


def get_type(val1, val2):
    if isinstance(val1, Float) or isinstance(val2, Float):
        return float
    if isinstance(val1, Int) or isinstance(val2, Int):
        return int
    if isinstance(val1, Char) or isinstance(val2, Char):
        return str


if __name__ == "__main__":
    table = TypeTable()
    table.enter_scope()
    table.insert_variable("i", "int", value=5)
    print(table.lookup_variable("i"))
    print(table.lookup_variable("b"))
    table.enter_scope()
    table.insert_variable("b", "float", value=3.0)
    print(table.lookup_variable("i"))
    b = table.lookup_variable("b")
    print(b)
    b.update_value(5)
    print(table.lookup_variable("b"))

    table.leave_scope()
    table.leave_scope()
