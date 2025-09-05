class Artist:
    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    

    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"
    

    def is_valid(self):
        if self.name == "" or self.name == None:
            return False
        if self.genre == "" or self.genre == None:
            return False
        return True
    

    def contains_errors(self):
        errors = []
        if self.name == "" or self.name == None:
            errors.append("Artist has no name")
        if self.genre == "" or self.genre == None:
            errors.append("Artist has no genre")
        return f"{', '.join(errors)}."