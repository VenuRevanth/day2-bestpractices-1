class Birds:
    def __init__(self):
        self.members = ['Duck', 'Raven','Sparrow']
    def PrintMembers(self):
        print('Printing members of birds class' )
        for members in self.members:
            print('\t%s'  % members)
        
