-- the team with most win
-- the team with most win at home
-- the team with most win at away
-- the team 
-- the team with most loss

-- 1. List the team and opponent in the table.
select team, opponent from nba_games_stats;

-- 2. List the team, date, home, WinofLoss for all team playing with NYK
select team, Date, home, WINorLOSS from nba_games_stats
where opponent in ("NYK");

-- 3. List the Team, team points, Opponent, opponent point, Date for all date in year 2015
-- with x3pointshotspercent between 60% and 75%.
select team, TeamPoints, Opponent, OpponentPoints, Date from nba_games_stats
where year(date) = 2015 and X3PointShotsPercent between 0.60 and 0.75;

-- 4. (Use a SUBQUERY) List the team, winorloss, home, freethrows, opponent and highest opptotalfouls for the
select team, WINorLOSS, Home, FreeThrows, Opponent, OppTotalFouls from nba_games_stats
where OppTotalFouls in (select max(OppTotalFouls) from nba_games_stats);

-- 5. What is the teamname and highest x3pointshotsattempted that has the highest avg(x3pointshotspercent) 
select team, X3PointShotsAttempted, avg(X3PointShotsPercent) as a from nba_games_stats
where X3PointShotsAttempted in (select max(X3PointShotsAttempted) from nba_games_stats)
group by team, X3PointShotsAttempted
order by a desc limit 1;

-- select * from nba_games_stats;
