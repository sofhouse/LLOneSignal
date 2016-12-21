class OSHeader:

    def __init__(self, auth_token):
        self.contentType = "application/json; charset=utf-8"
        self.authorization = "Basic " + auth_token

    def get_header(self):
        header = {"Content-Type": self.contentType, "Authorization": self.authorization}
        return header