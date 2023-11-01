$(function() {
    const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    $.ajax({
        url: apiUrl,
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            for (let i = 0; i < data.results.length; i++) {
                $('#list_movies').append('<li>' + data.results[i].title + '</li>');
            };
        }
    });
});