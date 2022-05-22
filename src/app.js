const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/ArticleDump', {
    "auth":{
        "username" : "GauravKr",
        "password" : "gaurav123"
    },
    "authSource" : "admin",
    "useNewUrlParser" : true,
    "useUnifiedTopology" : true
}).then(result => {
    console.log("mongoose connected!");
}).catch(err => console.log(err));