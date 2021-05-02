var progresso = null;
function iniciar_scan(){
    progresso = Metro.activity.open({
        type: 'square',
        overlayColor: "#fff",
        overlayAlpha: 1,
        text: '<div class="mt-2 text-small">Por favor aguarde...</div>',
        overlayClickClose: true
    });
}

function encerrar_scan(){
    Metro.activity.close(progresso)
}

$("#btn1").click(() => {
    iniciar_scan();
    let ip_address = $("#inp1").val();
    eel.comecar_scan(ip_address)(clients => {
        for (item of clients) {
            $("#result-final").append(`<li>${item}</li>`)
        }
        encerrar_scan();
    })
})

$("#resultado").click(() => {
    $("#section-home").hide(250)
    $("#section-result").show(250)
});

$("#principal").click(() => {
    $("#section-result").hide(250)
    $("#section-home").show(250)
});