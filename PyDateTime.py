
class DateTime:
	def __init__(self):
		self.month = 1
		self.day = 1
		self.year = 2012
		self.hour = 0
		self.minute = 0
		self.second = 0

	def getDate(self):
		return [self.month, self.day, self.year]

	def getTime(self):
		return [self.hour, self.minute, self.second]

	def toCsv(self):
		return "%s,%s,%s,%s,%s,%s" % (self.month, self.day, self.year, \
			self.hour, self.minute, self.second)

	def toString(self):
		return "%02d/%02d/%02d %02d:%02d:%02d" % (int(self.month),int(self.day), int(self.year), \
			int(self.hour), int(self.minute), int(self.second))
