class Album:
    def __init__(self, id, title, release_year, artist_id, artist_name = None):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
        self.artist_name = artist_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id}, {self.artist_name})"
    
    def is_valid(self):
        if self.title == "" or self.title == None:
            return False
        if self.release_year == "" or self.release_year == None:
            return False
        if self.artist_id == "" or self.artist_id == None:
            return False
        return True
    

    def contains_errors(self):
        errors = []
        if self.title == "" or self.title == None:
            errors.append("Album has no title")
        if self.release_year == "" or self.release_year == None:
            errors.append("Album has no release year")
        if self.artist_id == "" or self.artist_id == None:
            errors.append("Album has no artist ID")
        return f"{', '.join(errors)}."