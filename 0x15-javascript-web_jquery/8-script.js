$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (title, movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
