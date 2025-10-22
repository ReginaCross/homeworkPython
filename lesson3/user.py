class User:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def print_first_name(self):
        print(self.fname)
    
    def print_last_name(self):
        print(self.lname)
    
    def print_full_name(self):
        print(f"{self.fname} {self.lname}")