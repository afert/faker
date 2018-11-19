import re

page="In a dark dirty house, there lived a small, dirty salesman. " \
"He always makes unhealthy candies and sells them to the students. " \
"He has a lot of money now. But how does he make the candie. Oh, xuHe i"

words=re.findall("\w+",page)

for word in words:
	print (word)