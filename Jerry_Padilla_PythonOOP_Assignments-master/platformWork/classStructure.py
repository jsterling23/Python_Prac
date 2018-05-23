# class User(object):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = False
#
#     def login(self):
#         self.login = True
#         print self.name + " is logged in"
#         return self
#
# new_user = User("Jerry", "Jerry@gmail.com")
# print new_user


# class User(object):
#     name = "Jerry"
#
# jerry = User()
# print "jerry's name: ", jerry.name
# User.name = 'Bob'
# print "jerrys name after change: ", jerry.name
# bob = User()
# print "bobs name: ", bob.name
#
# print jerry.name


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
    def login(self):
        self.logged = True
        return self
    def logout(self):
        self.logged = False
        return self
    def changeName(self):
        self.name = "you changed the name to bill"
        return self
    def show(self):
        print "name: {}, email: {}, logged: {}".format(self.name, self.email, self.logged)
        return self

user1 = User('Jerry Padilla', 'jerrypadilla23@gmail.com')
user1.login(), user1.changeName()
print user1.logged
print user1.name
user1.logout()
print user1.show()
