$(window).ready(function () {

    $("#home-lk").click(() => {
        for (let idx = 0; idx < document.getElementsByTagName("main")[0].children.length; idx++) {
            document.getElementsByTagName("main")[0].children[idx].style.display = "none";
        }
        document.getElementById("home").style.display = "block";
    });

    $("#panel-lk").click(() => {
        for (let idx = 0; idx < document.getElementsByTagName("main")[0].children.length; idx++) {
            document.getElementsByTagName("main")[0].children[idx].style.display = "none";
        }
        document.getElementById("panel").style.display = "block";

        eel.get_api_information()(function (dt) {
            const data_json = JSON.parse(dt)
            console.log(data_json)
            let main = document.getElementById("area-credits-shodan").children

            // Configuração da barra de progresso "monitored_ips"...
            let usage_monitored_ips_total = (data_json.monitored_ips/data_json.usage_limits.monitored_ips)*100;
            console.log(usage_monitored_ips_total)
            main[0].children[0].innerText = "IPs Monitorados"
            main[0].children[1].children[0].innerText = `${parseInt(usage_monitored_ips_total)}%`;
            main[0].children[1].children[0].style = `width: ${parseInt(usage_monitored_ips_total)}%`;

            // Configuração da barra de progresso "query_credits"...
            let usage_query_credit_total = (data_json.query_credits/data_json.usage_limits.query_credits)*100;
            main[1].children[0].innerHTML = "créditos de consulta";
            main[1].children[1].children[0].attributes[5].value = data_json.usage_limits.monitored_ips;
            main[1].children[1].children[0].innerText = `${parseInt(usage_query_credit_total)}%`;
            main[1].children[1].children[0].style = `width: ${parseInt(usage_query_credit_total)}%`;
        })


    });

    $("#settings-lk").click(() => {
        for (let idx = 0; idx < document.getElementsByTagName("main")[0].children.length; idx++) {
            document.getElementsByTagName("main")[0].children[idx].style.display = "none";
        }
        document.getElementById("settings").style.display = "block";
    });

    $("#search-cdir-lk").click(() => {
        for (let idx = 0; idx < document.getElementsByTagName("main")[0].children.length; idx++) {
            document.getElementsByTagName("main")[0].children[idx].style.display = "none";
        }
        document.getElementById("search-cdir").style.display = "block";
    });
});