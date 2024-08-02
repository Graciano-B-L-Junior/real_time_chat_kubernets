window.addEventListener("DOMContentLoaded", () => {
  
  
    const ws = new WebSocket("ws://localhost:9000/");

    const user = document.querySelector("#user")
    user.getAttribute("value")

    // websocket.send("Graciano")


    ws.onopen = function(event) {
      console.log("Connected to WebSocket server,user:"+user.getAttribute("value"));
      ws.send(JSON.stringify({  user:user.getAttribute("value"),
                                action:"user_enter"}
                            ));
        document.querySelector(".send-message").addEventListener("click",function(){
            let input = document.querySelector("#message")
            let message = input.value
            input.value = ''
            ws.send(JSON.stringify({    user:user.getAttribute("value"),
                                        action:"send_message",
                                        message:message}
            ));
        })
    };

    ws.onmessage = function(event) {
        let chat_div = document.querySelector(".chat-scroll")
        
        
        let data = JSON.parse(event.data)
        const now = new Date();
        const hours = now.getHours().toString().padStart(2, '0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        const seconds = now.getSeconds().toString().padStart(2, '0');
        const time = `${hours}:${minutes}:${seconds}`
        switch (data.action) {
            case "user_enter":
                chat_div.insertAdjacentHTML('afterbegin', `<p>${time} [${data.user}] enter on chat</p>`);
                break;
            case "send_message":
                chat_div.insertAdjacentHTML('afterbegin', `<p>${time} [${data.user}]: ${data.message}</p>`);
                break;

            case "user_out":
                chat_div.insertAdjacentHTML('afterbegin', `<p>${time} [${data.user}]: leave the chat</p>`);
                break;
        }
    };

    ws.onclose = function(event) {
        if (event.wasClean) {
            console.log(`Connection closed cleanly, code=${event.code}, reason=${event.reason}`);
        } else {
            console.log('Connection closed unexpectedly');
        }
    };

    ws.onerror = function(error) {
        console.log(`WebSocket error: ${error.message}`);
    };;
  
  });