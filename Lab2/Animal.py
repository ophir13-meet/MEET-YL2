class Animal:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sleep(self): 
		print self.name+" who is "+self.age+" years old is sleeping!"

	def eat(self):
		print self.name+" who is "+self.age+" years old is eating!"


class Dog(Animal):
	def __init__(self, furColor, size, name, age):
		Animal.__init__(self, name, age)
		self.furColor = furColor
		self.size = size

	def bark():
		print self.name+" is being very noisy. Kill him!"


class Bird(Animal):
	def __init__(self, wingColor, name, age):
		Animal.__init__(self, name, age)
		self.wingColor = wingColor

	def fly():
		print self.name+" is getting away! Kill him!"




doggy = Dog("Purple", "big", "Bart", 5)
Birdy = Bird("Black","Sam", 4)

print doggy.name
print Birdy.age
print Birdy.wingColor