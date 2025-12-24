# Listing exceptions

class NotALigand(Exception):
    # For incorrect dimensions
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"