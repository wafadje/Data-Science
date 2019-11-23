"""
"""

import sqlalchemy as db


def keys(table):
	print(table.columns.keys())

def query(stmt, connection):
	result_proxy = connection.execute(stmt).fetchall()
	return result_proxy

def main():
	DATABASE_URL = "sqlite:///../input/sport.db"
	engine = db.create_engine(DATABASE_URL)
	table_name  = engine.table_names()

	connection = engine.connect()
	
	metadata = db.MetaData()

	games = db.Table('games', metadata, autoload=True, autoload_with=engine)
	goals = db.Table('goals', metadata, autoload=True, autoload_with=engine)
	teams = db.Table('teams', metadata, autoload=True, autoload_with=engine)
	persons = db.Table('persons', metadata, autoload=True, autoload_with=engine)

	#stmt = db.select([teams.c.id]).where(teams.c.code == "FRA")
	#stmt = db.select([games.c.team1_id, db.func.count(games.c.team1_id)]).group_by(games.c.team1_id).where(games.c.team1_id == 131 and games.c.team2_id == 131)
	keys(persons)
	keys(goals)
	keys(games)
	#stmt = db.select([goals.c.person_id, db.func.count(goals.c.score1)]).group_by(goals.c.score1).where(goals.c.team_id == 131).order_by(goals.c.score1)
	#stmt = db.select([persons.c.name, goals.c.person_id, db.func.count(goals.c.score1)]).select_from(goals.join(persons, goals.c.person_id == persons.c.id)).group_by(goals.c.score1).where(goals.c.team_id == 131)

	#    Write a SQL query that returns the minute at which Benjamin Pavard scored his "Demi-volée" goal.
	#stmt = db.select([goals.c.minute]).select_from(goals.join(persons, goals.c.person_id == persons.c.id)).where(persons.c.name == 'Benjamin Pavard')
	"""
    returns the name, the team name and the number of goals_scored of the 3 players who scored the most goals (excluding own goals)in the competition.
	"""
	#stmt = db.select([persons.c.name, db.func.max(goals.c.score1)]).select_from(goals.join(persons, goals.c.person_id == persons.c.id)).group_by(persons.c.name).where(goals.c.team_id == 131)

	"""
	all teams that played with the fields nb_games_played, nb_games_win, nb_games_lost, nb_games_draw.
	 Order the results by nb_games_played descending, nb_games_win descending, nb_games_draw descending,
	  and team_name ascending.
	flashlight Hint: Go step-by-step when constructing your SQL query. At the look of the games table, 
	construct first a table that answers the question for team playing "at home" - then for team playing "outside" 
	- then combine both.
	"""
	stmt = db.select([games.c.home])

	r = query(stmt, connection)
	print(r)
	
if __name__ == "__main__":
    main()
