class Fish:
	def __init__(self):
		self.members = ['Dolphin', 'Shark', 'Catfish']
	def PrintMembers(self):
		print(' Printing members of fish class' )
		for member in self.members:
			print('t%s' %member)
