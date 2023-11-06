import collections

cache_size = 16

#Class to implement the function of a CPU cache 
class Cache:
	#Similar to the memory class, we will be using a dequeue to emulate the cache. Inside the dequeue, our values will be stored as tuples (<address>,<value>)
	def __init__(self):
		self.cache = collections.deque(maxlen = cache_size)
		self.flush_cache()

	#Append cache to flush out the values
	def flush_cache(self):
		for i in range(cache_size):
			self.cache.append(("",""))

	#Search cache for values written
	def search_cache(self, address):
		for i in range(cache_size):
			if self.cache[i][0] == address:
				return self.cache[i][1]
		return None

	#Write values to cache
	def write_cache(self, address, value):
		self.cache.append(tuple((address, value)))