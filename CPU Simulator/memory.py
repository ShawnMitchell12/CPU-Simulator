memory_bus_size = 128

#Class to implement the mode of transportation for the memory of our simulated CPU

class Memory:
	def __init__(self):
	#Using dictionary key:values to simulate the memory bus
		self.memory_bus = {}
		self.init_memory_bus()

	#Method used to initialize the memory bus. Converts iterator to a binary string value by looping from 0 to the bus size
	def init_memory_bus(self):
		for i in range(memory_bus_size):
			self.memory_bus['{0:08b}'.format(i)] = 0

	#Method to search if memory address has anything wrtiten to it
	def search_memory_bus(self, address):
		if self.memory_bus.get(address) is not None:
			return self.memory_bus.get(address)
		return None

	#Method to write values to memory address
	def write_memory_bus(self, address, value):
		if self.memory_bus.get(address) is not None:
			self.memory_bus[address] = value