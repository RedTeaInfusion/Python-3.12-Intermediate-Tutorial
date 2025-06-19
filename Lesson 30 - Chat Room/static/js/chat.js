const socket = io();
const chatBox = document.getElementById('chat-box');
socket.on('message', function(msg){
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('chat-message');
    const username = document.getElementById('username').value;
    const sender = msg.split(':')[0];
    if (sender.trim() === username.trim()){
        msgDiv.classList.add('sender');
    } else {
        msgDiv.classList.add('receiver');
    }
    msgDiv.textContent = msg;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
});
function sendMessage() {
    const username = document.getElementById('username').value;
    const message = document.getElementById('message').value;
    if (message.trim() !== "") {
        socket.send(username + ': ' + message);
        document.getElementById('message').value = '';
    }
}