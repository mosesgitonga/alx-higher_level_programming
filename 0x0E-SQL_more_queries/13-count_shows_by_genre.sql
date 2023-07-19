-- list and count

SELECT tv_show_genres.title AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY tv_show_genres.title
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
