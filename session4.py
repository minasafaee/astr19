class duck:
	def __init__ (self):
		self.arms = 3.2
		self.legs = 3.4
		self.eye = 2
		self.tail = True
		self.furry = False

	def description(self):
		print("Ducks are waterfowls with a wing span of ", self.arms, " feet.")
		print("They have legs that are ", self.legs, " inches long.")
		print("They have ", self.eye, " eyes.")
		print("It is ", self.tail, " that ducks have a tail.")
		print("If you thought that ducks were furry you would be ", self.furry, ".")

d1 = duck()
d1.description()
