

$(document).on('click', document, function(e){
    console.log('events file: ', e.target)
})

let url = `ws://${window.location.host}/ws/socket-server` // instead of http, we use websocket channel (ws)

// create websocket object
const notifSocket = new WebSocket(url)

// this event will fire when data is received through a websocket or data coming from our backend
notifSocket.onmessage = function(e){
    let data = JSON.parse(e.data)
    console.log('data: ', data)
}

