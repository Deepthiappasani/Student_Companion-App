from libraries import *

class setupUtils:
        def setup(self):
                #User List
                file_exists = os.path.isfile("users.txt")
                if file_exists:
                        pass
                else:
                        file = open("users.txt", "w+")
                        file.close()

                #User-Event List
                file_exists = os.path.isfile("Events.txt")
                if file_exists:
                        pass
                else:
                        file = open("Events.txt", "w+")
                        file.close()

                #User-Books-Papers List	
                file_exists = os.path.isfile("Books.txt")
                if file_exists:
                        pass
                else:
                        file = open("Books.txt", "w+")
                        file.close()

                #Activities List
                file_exists = os.path.isfile("Activities.txt")
                if file_exists:
                        pass
                else:
                        file = open("Activities.txt", "w+")
                        file.close()
