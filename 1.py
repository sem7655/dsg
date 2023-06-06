class StringVar:
    def __init__(self, string=""):
        self.string = string

    def set(self, new_string):
        self.string = new_string

    def get(self):
        return self.string

        string_var = StringVar ('World!')
        print (string_var.get ())
        string_var.set ('Goodbye')
        print (string_var.get ())
