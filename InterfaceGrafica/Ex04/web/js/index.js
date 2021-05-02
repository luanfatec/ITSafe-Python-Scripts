function showClassDemo(msg, title, type_message){
    var notify = Metro.notify;
    notify.create(msg, title, {
        cls: type_message
    });
}

function scanner() {
    $("#load-scanner").append(`<div id="load-sc" data-role="activity" data-type="atom" data-style="color"></div>`)
    eel.scanner_main()(data => {
        if (data) {
            showClassDemo("Sanner finalizado com sucesso!", "Success!", "success")
            $("#load-sc").remove()
        } else {
            showClassDemo("Houve um erro ao realizar o scan!", "Error!", "alert")
            $("#load-sc").remove()
        }
    });
}