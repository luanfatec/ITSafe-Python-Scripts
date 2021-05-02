var progresso = null;
eel.expose(js_carregar);

function js_carregar() {
        progresso = Metro.activity.open({
        type: 'square',
        overlayColor: '#fff',
        overlayAlpha: 1,
        text: '<div class="nt-2 text-small">Aguarde por favor...</div>'
    });
}


eel.expose(js_fechar);
function js_fechar() {
    Metro.activity.close(progresso)
}

eel.expose(esperar);
function esperar() {
    $(document).ready(() => {
        return true;
    });
}