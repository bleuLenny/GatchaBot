class Character:
    def __init__(self, name, value, owned=False, owner=None):
        self.name = name
        self.value = value
        self.owned = owned
        self._owner = owner

    def owned(self):
        return self.owned

    def __str__(self):
        return self.value

    @property
    def owner(self):
        """Returns the value of the owner"""
        return self.owner
    @owner.setter
    def owner(self, owner):
        """Sets the owner value"""
        if self.owned == False and self.owner == None:
            self.owner = owner
            self.owned = True