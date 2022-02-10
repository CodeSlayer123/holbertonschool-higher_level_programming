-- lists all shows in hbtn_0d_tvshows without a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM hbtn_0d_tvshows WHILE tv_show_genres NOT linked
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
