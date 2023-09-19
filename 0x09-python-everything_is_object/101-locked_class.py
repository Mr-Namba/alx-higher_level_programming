class LockedClass:
    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        elif name != 'first_name' and hasattr(self, 'first_name') == False:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        else:
            raise AttributeError(f"Cannot set attribute '{name}'")

# Example Usage:
# Uncomment and run the following code to test the class

# obj = LockedClass()
# obj.first_name = 'John'
# print(obj.first_name)  # Output: John

# Uncommenting the line below would raise an AttributeError
# obj.last_name = 'Doe'

