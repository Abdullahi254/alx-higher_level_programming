$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function (data) {
    const name = data.name
    $("DIV#character").text(name);
});