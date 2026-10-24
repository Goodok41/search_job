class SearchJobError(Exception):
    pass


class ParseError(SearchJobError):
    def __init__(self, filename, reason):
        super().__init__(f"{filename}: {reason}")
        self.filename = filename
        self.reason = reason