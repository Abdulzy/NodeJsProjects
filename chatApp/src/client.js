var client = require('socket.engine').client;
var c = new client();
c.start();
c.on("test", (data) => {
	console.log(data)
});

c.write("test", "jyhhkj");



