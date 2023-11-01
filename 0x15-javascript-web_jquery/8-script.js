$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (data) {
    const movies = data.results;
    $("UL#list_movies").append(movies.map(movie => `<li>${movie.title}</li>`));
});