$(function() {
    const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

    $.ajax({
        url: apiUrl,
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            $('#character').html(data.name);
        },
        error: function(xhr, status, error) {
            console.log('Error:', status, error)
        }
    });
});
