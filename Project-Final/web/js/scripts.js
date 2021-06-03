function myforeach(data, idx, err) {
    console.log(data)
}

$("#search").click(() => {
    eel.load_config_user()(d => {
        const data = JSON.parse(d)
        console.log(data)
    });
})

// Update profile
document.getElementById("form-settings").addEventListener("click", (event) => {
    event.preventDefault();

    // Get form settings
    let form_settings = document.getElementById("form-settings").children
    const data_form = {}

    // Config values form settings
    data_form["NAME_PROJECT"] = form_settings[0].children[1].value;
    data_form["NAME"] = form_settings[1].children[1].value;
    data_form["EMAIL"] = form_settings[2].children[1].children[1].value;
    data_form["USERNAME"] = form_settings[3].children[1].value;
    data_form["SHODAN"] = form_settings[4].children[1].value;
    data_form["SHODAN_API_LINK"] = form_settings[5].children[1].value;
    data_form["LINK_PROFILE"] = form_settings[6].children[1].value;
    data_form["API_KEY"] = form_settings[7].children[1].value;

    eel.update_settings_user(data_form)() // Save settings
})
