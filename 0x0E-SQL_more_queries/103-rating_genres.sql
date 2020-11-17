-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT tv_genres.name, SUM(rate) rating
	FROM tv_shows
	INNER JOIN tv_show_genres  ON tv_show_genres.show_id = tv_shows.id
		INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
		INNER JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
	GROUP BY tv_genres.name
	ORDER BY rating desc;
