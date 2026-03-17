class Mammals:
    def __init__(self):
        self.members = ['Tiger', 'Elephant', 'dog']

    def PrintMembers(self):
        print (' Printing Members of Mammals Class' )
        for members in self.members:
            print('\t%s'  % members)

