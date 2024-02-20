const express = require("express");
const socket = require("socket.io");

const app = express();

app.use(express.static("views"))

app.set("view engine", "ejs");


app.get("/", (req,res)=>{
    res.render("index")
})

const server = app.listen(4000)

const io = socket(server);

io.on('connection',(socket)=>{
    console.log("made socket connection", socket.id);

    socket.on('chat', function(data){
        io.sockets.emit('chat', data)
    });
})