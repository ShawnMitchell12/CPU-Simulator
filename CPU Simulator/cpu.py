from email.errors import NoBoundaryInMultipartDefect
from cache import Cache
from memory import Memory

cpu_counter_init_value = 0
number_of_registers = 9

add_instruction_operator = 'ADD'
add_i_instruction_operator = 'ADDI'
jump_instruction_operator = 'J'
cache_instruction_operator = 'cache'

cache_off_value = 0
cache_on_value = 1
cache_flush_value = 2

#Helper function to convert register string to an index value
def convert_register_to_index(value):
	return int(value[1:])

#CPU class to implement the bulk of our cpu simulator
#CPU Properties included in class:
#CPU counter - shows how many instructions are being parsed
#Registers - list to represent the memory registers
#Cache flag - boolean showing if cache is currently is use
#Cache - cache object
#Memory Bus - memory object
class CPU:
	def__init__(self):
		self.cpu_counter = cpu_counter_init_value
		self.registers = [0] * number_of_registers
		self.cache_flag = False
		self.cache = Cache()
		self.memory_bus = Memory()

	def increment_cpu_counter(self):
		self.cpu_counter += 1

	def reset_cpu_counter(self):
		self.cpu_counter = cpu_counter_init_value

	def get_cpu_counter(self):
		return self.cpu_counter

	def set_cpu_counter(self, value):
		self.cpu_counter = value

	def reset_registers(self):
		for i in range(len(self.registers)):
			self.registers[i] = 0

	def set_cache_flag(self, value):
		self.cache_flag = value

	def flush_cache(self):
		self.cache.flush_cache()

	def search_cache(self, address):
		return self.cache.search_cache(address)

	def write_cache(self, address, value):
		self.cache.write_cache(address, value)
