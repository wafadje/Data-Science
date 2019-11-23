"""
You are given a database sport.db that contains data from 2018 Soccer World Cup.
I. Data introduction
    What tables does it contain?
    sqlite> .table
	cities         events         groups         places       
	continents     events_teams   groups_teams   rounds       
	countries      games          leagues        seasons      
	country_codes  goals          persons        teams        
	sqlite> 
    What is the structure of the table games? How many games were played in total?
    sqlite> .headers on
	sqlite> select * from games limit 1;
	id|key|round_id|pos|group_id|team1_id|team2_id|play_at|postponed|play_at_v2|play_at_v3|ground_id|city_id|knockout|home|score1|score2|score1et|score2et|score1p|score2p|score1i|score2i|score1ii|score2ii|next_game_id|prev_game_id|winner|winner90|created_at|updated_at
	64
    What is the structure of the table teams? How many teams participated in the competition?
    sqlite> select DISTINCT() from teams limit 1;
	id|key|title|title2|code|synonyms|country_id|city_id|club|since|address|web|assoc_id|national|created_at|updated_at
	1|alg|Algeria||ALG||27||f|||||f|2019-01-14 10:11:52.293459|2019-01-14 10:11:52.293459
	 
    222
II. Allez les bleus
    Write a SQL query that returns the team_id of France team fr.
    > sqlite> select id as team_id from teams where code = "FRA";
	team_id
	131
    Based on France team_id write a query that returns the number of matches played by France team.
    sqlite> select count() from games where (team1_id = 131 or team2_id = 131);
	count()
	5
    Write a SQL query that returns person_id and goals_scored (the number of scored goals) of all French players who scored a goal. Order the results by descending goals_scored.
    sqlite> select person_id, count(score1) as goals_scored
   ...> where team_id = 131
   ...> group by score1
   ...> order by score1 DESC;
	person_id|goals_scored
	28|2
	134|2
	23|3
	108|5
	99|2
	sqlite> 
    Write a SQL query that returns the same result as before but with the player name instead of the person_id. Which French player scored the most? Is the data clean?
    sqlite> select p.name, count(score1)
   ...> from persons p
   ...> join goals g
   ...> ;
	name|count(score1)
	Pogba|22378
    Write a SQL query that returns the minute at which Benjamin Pavard scored his "Demi-volée" goal.
III. Best strikers
    Write a SQL query that returns the name, the team name and the number of goals_scored of the 3 players who scored the most goals (excluding own goals)in the competition.
IV. Stats per country
    Write a SQL query that returns all teams that played with the fields nb_games_played, nb_games_win, nb_games_lost, nb_games_draw. Order the results by nb_games_played descending, nb_games_win descending, nb_games_draw descending, and team_name ascending.
        flashlight Hint: Go step-by-step when constructing your SQL query. At the look of the games table, construct first a table that answers the question for team playing "at home" - then for team playing "outside" - then combine both.
    Write a query that returns those results for Asian team(s) that played more than 3 games.
    Write a query that returns those results for African team(s) that lost all their game.
    [BONUS] Write a query that returns those those results for all countries plus the fields nb_goals_scored, nb_scores_collected.
"""
