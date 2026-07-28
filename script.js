function sendMessage() {

    let message = document.getElementById("message").value;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    })

    .then(response => response.json())

    .then(data => {
        document.getElementById("chat").innerHTML +=
            "<p><b>You:</b> " + message + "</p>" +
            "<p><b>Bot:</b> " + data.reply + "</p>";

        document.getElementById("message").value = "";
    });

}