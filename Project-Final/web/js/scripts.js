function myforeach(data, idx, err) {
    console.log(data)
}

$("#search").click(() => {
    eel.get_net("191.37.46.0/24")(d => {
        d.matches.forEach(myforeach)
    });
})
