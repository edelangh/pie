

var http = require ('http')

http.get({
	host: 'api.stackexchange.com',
	path: '/2.2/search',
	headers: {'content-type': 'application/json'}
}, function (res) {
	var body = '';
	res.on('data', function (chk) {
		body += chk;
	});
	res.on('end', function () {
		console.log(body);
	});
});

