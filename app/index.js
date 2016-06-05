var http = require('http');
var fs = require('fs');

function get(url) {
return (new Promise(function (resolve, reject){
      var req = http.get({
        host: '192.168.0.12',
        path: url,
        port: 8080
      }, function (response) {
        var body = '';
        response.on('data', function (d) {
          body += d;
        });
        response.on('end', function () {
          resolve(body);
        });
      });
    }))
}

var express = require('express');
var https = require('https');
var http = require('http');
var app = express();

var pkey = fs.readFileSync('priv.pem');
var pcert = fs.readFileSync('cert.cer')

var options = {
	    key: pkey,
		    cert: pcert
};


http.createServer(app).listen(8000);
https.createServer(options, app).listen(443);

var canal = [];

// task model {'isFinish': 0, 'name': 'open', 'data': {'url': 'google.fr'}}
var users_tasks = [];

app.use(require('cors')());

app.get('/tasks/:user', function (req, res) {
  var user = req.params.user;
  var tasks = users_tasks[user];
  users_tasks[user] = [];
  res.status(200).json(tasks);
});

app.get('/tasks/:user/new', function (req, res) {
  var user = req.params.user;
  var url = req.query.url;
  var action = req.query.action;
  delete req.query.action;

  if (!users_tasks[user]) {
  	users_tasks[user] = [];
  }
  var task = {
  	isFinish: false,
	action: action,
	data: req.query
  }
  users_tasks[user].push(task);
  res.write('ok, i will do it for you');
  res.end();
});
app.get('/tasks/:user/open', function (req, res) {
  var user = req.params.user;
  var url = req.query.url;
  if (!users_tasks[user]) {
  	users_tasks[user] = [];
  }
  var task = {
  	isFinish: false,
	action: 'open',
	data: {
		url: url,
	}
  }
  users_tasks[user].push(task);
  res.write('ok, i will open page');
  res.end();
});

// task model {'isFinish': 0, 'name': 'open', 'data': {'url': 'google.fr'}}
app.get('/chat/opencanal/:user', function (req, res) {
  var user = req.params.user;
  /*canal[user] = 'Okay, i\'m contacting ' + user;
  var str = canal[user];
  res.write(str);
  res.end();
  */
  var task = {};
  task = {
  	isFinish: false,
	action: 'stopYoutube',
	data: {
	}
  }
  if (!users_tasks[user]) {
  	users_tasks[user] = [];
  }
  users_tasks[user].push(task);
  task = {
  	isFinish: false,
	action: 'open',
	data: {
		url: 'https://appear.in/seedup'
	}
  }
  users_tasks[user].push(task);
  res.write('Okey, i\'m contacting ' + user);
  res.end();
});
