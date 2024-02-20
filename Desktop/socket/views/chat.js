const socket = io.connect("http://localhost:4000");

const message= document.getElementById('message');
const name= document.getElementById('name');
const btn= document.getElementById('send');
const output= document.getElementById('output');
const feedback = document.getElementById('feedback');

console.log("java works");

btn.addEventListener('click', function(){
    console.log("button clicked")

    socket.emit('chat',{
        message: message.value,
        name: name.value
    });
    message.value="";
});

message.addEventListener("keypress", ()=>{
    socket.emit("typing", name.value);
})


socket.on('chat', function(data){
    feedback.innerHTML=""
    output.innerHTML += "<p><strong>"+data.name + ": </strong>" + data.message + "</p>"
})
