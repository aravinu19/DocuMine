var express = require("express");
var bodyParser = require("body-parser");
var mineApi = require("./mineApi.js");

var app = express();
app.set('port', (process.env.PORT || 8080));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

var server = app.listen(app.get('port'), () => {
    console.log("DocuMine API Server is Up and Running on ", server.address().port);
});