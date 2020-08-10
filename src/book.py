class Book:
    """A simple Book class"""
    title = "title"
    author = "last, first"
    genre = "fiction"

    def __init__(self, t, a, g):
        self.title = t
        self.author = a
        self.genre = g

    
    def __repr__(self):
        return str(self.genre) + ": " + str(self.title) + " by " + str(self.author)
