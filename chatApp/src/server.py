from socketengine import host
import time

h = host()
h.start()
validate = True
while validate:
	data = h.get_ALL("test")
	if data is not None:
		for item in data:
			print(item)
			validate = False
			time.sleep(10)
			h.write_ALL("test", ["completed"])
			break

h.close()