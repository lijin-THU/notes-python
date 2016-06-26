import requests as _requests
from goldsberry._apiFunc import *

my_headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'\
    ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 '\
    'Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'\
    ',image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}

class demographics:
    def __init__(self, playerid):
        self._url = 'http://stats.nba.com/stats/commonplayerinfo?'
        self._api_param = {'PlayerID':playerid}
        self._pull = _requests.get(self._url, params=self._api_param, headers=my_headers)
    def player_info(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def headline_stats(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class career_stats:
    def __init__(self, playerid, league='NBA',permode=1):
        self._url = "http://stats.nba.com/stats/playerprofilev2?"
        self._api_param = {'PlayerID':playerid,
                           'LeagueID':_nbaLeague(league),
                           'PerMode':_PerModeSmall36(permode)}
        self._pull = _requests.get(self._url, params=self._api_param, headers=my_headers)
    def season_totals_regular(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def career_totals_regular(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season_totals_post(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def career_totals_post(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season_totals_allstar(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def career_totals_allstar(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season_totals_college(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def career_totals_college(self):
        _headers = self._pull.json()['resultSets'][7]['headers']
        _values = self._pull.json()['resultSets'][7]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season_rankings_regular(self):
        _headers = self._pull.json()['resultSets'][8]['headers']
        _values = self._pull.json()['resultSets'][8]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season_rankings_post(self):
        _headers = self._pull.json()['resultSets'][9]['headers']
        _values = self._pull.json()['resultSets'][9]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season_high(self):
        _headers = self._pull.json()['resultSets'][10]['headers']
        _values = self._pull.json()['resultSets'][10]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def career_high(self):
        _headers = self._pull.json()['resultSets'][11]['headers']
        _values = self._pull.json()['resultSets'][11]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def next_game(self):
        _headers = self._pull.json()['resultSets'][12]['headers']
        _values = self._pull.json()['resultSets'][12]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class general_splits:
    def __init__(self, playerid, season='2015',seasontype=1, league='NBA',
        dateto='', datefrom='', gamesegment=1, lastngames=0, location=1, measuretype=1,
        month=0, opponentteamid=0, outcome=1, paceadjust=1, permode=1, period=0,
        plusminus=1, rank=1, seasonsegment=1, vsconf=1, vsdiv=1):
        self._url = "http://stats.nba.com/stats/playerdashboardbygeneralsplits?"
        self._api_param = {'PlayerID':playerid,
                           'SeasonType': _SeasonType(seasontype),
                           'Season': _nbaSeason(season),
                           'LeagueID': _nbaLeague(league),
                           'DateTo':_valiDate(dateto),
                           'DateFrom':_valiDate(datefrom),
                           'GameSegment':_GameSegment(gamesegment),
                           'LastNGames':lastngames,
                           'Location':_Location(location),
                           'MeasureType':_measureType(measuretype),
                           'Month':month,
                           'OpponentTeamID':opponentteamid,
                           'Outcome':_Outcome(outcome),
                           'PaceAdjust':_PaceAdjust(paceadjust),
                           'PerMode':_PerModeLarge(permode),
                           'Period':period,
                           'PlusMinus':_PlusMinus(plusminus),
                           'Rank':_Rank(rank),
                           'SeasonSegment':_SeasonSegment(seasonsegment),
                           'VsConference':_VsConference(vsconf),
                           'VsDivision':_VsDivision(vsdiv)}
        self._pull = _requests.get(self._url, params=self._api_param, headers=my_headers)
    def overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def location(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def wins_losses(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def month(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def pre_post_allstar(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def starting_position(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def days_rest(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class game_logs:
    def __init__(self, playerid, season='2015',seasontype=1, league='NBA'):
        self._url = "http://stats.nba.com/stats/playergamelog?"
        self._api_param = {'PlayerID':playerid,
                            'SeasonType': _SeasonType(seasontype),
                            'Season': _nbaSeason(season),
                            }
        self._pull = _requests.get(self._url, params=self._api_param, headers=my_headers)
    def logs(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class shot_dashboard:
    def __init__(self,playerid,league='NBA',season='2015', seasontype=1,teamid=0,
                             outcome=1,location=1,month=0,seasonsegment=1,datefrom='',
                             dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                             period=0,lastngames=0, permode=1):
        self._url = "http://stats.nba.com/stats/playerdashptshots?"
        self._api_param = {'PlayerID' : playerid,
                           'LeagueID': _nbaLeague(league),
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  _valiDate(datefrom),
                           'DateTo' : _valiDate(dateto),
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames,
                           'PerMode' : _PerModeMini(permode)
                           }
        self._pull = _requests.get(self._url, params=self._api_param, headers=my_headers)
    def overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def general(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def shot_clock(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def dribble(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def closest_defender(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def closest_defender_10ft(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def touch_time(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class rebound_dashboard:
    def __init__(self,playerid,league='NBA',season='2015', seasontype=1,teamid=0,
                outcome=1,location=1,month=0,seasonsegment=1,datefrom='',
                dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                period=0,lastngames=0,permode=1):
        self._url = "http://stats.nba.com/stats/playerdashptreb?"
        self._api_param = {'PlayerID' : playerid,
                           'LeagueID': _nbaLeague(league),
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  _valiDate(datefrom),
                           'DateTo' : _valiDate(dateto),
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames,
                           'PerMode' : _PerModeMini(permode)
                           }
        self._pull = _requests.get(self._url, params=self._api_param, headers=my_headers)
    def overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def shot_type(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def contesting_rebounders(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def shot_distance(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def rebound_distance(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class passing_dashboard:
    def __init__(self,playerid,league='NBA',season='2015', seasontype=1,teamid=0,
                 outcome=1,location=1,month=0,seasonsegment=1,datefrom='',
                 dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                 period=0,lastngames=0,permode=1):
        self._url = "http://stats.nba.com/stats/playerdashptpass?"
        self._api_param = {'PlayerID' : playerid,
                           'LeagueID': _nbaLeague(league),
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  _valiDate(datefrom),
                           'DateTo' : _valiDate(dateto),
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames,
                           'PerMode' : _PerModeMini(permode)
                           }
        self._pull = _requests.get(self._url, params=self._api_param, headers=my_headers)
    def passes_made(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def passes_received(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class defense_dashboard:
    def __init__(self,playerid,league='NBA',season='2015', seasontype=1,teamid=0,
                 outcome=1,location=1,month=0,seasonsegment=1,datefrom='',
                 dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                 period=0,lastngames=0,permode=1):
        self._url = "http://stats.nba.com/stats/playerdashptreb?"
        self._api_param = {'PlayerID' : playerid,
                           'LeagueID': _nbaLeague(league),
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  _valiDate(datefrom),
                           'DateTo' : _valiDate(dateto),
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames,
                           'PerMode' : _PerModeMini(permode)
                           }
        self._pull = _requests.get(self._url, params=self._api_param, headers=my_headers)
    def defending_shot(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class shot_log:
    def __init__(self,playerid,league='NBA',season='2015',seasontype=1,teamid=0,
                 outcome=1,location=1,month=0,seasonsegment=1,datefrom='',
                 dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                 period=0,lastngames=0):
        self._url = "http://stats.nba.com/stats/playerdashptshotlog?"
        self._api_param = {'PlayerID' : playerid,
                           'LeagueID': _nbaLeague(league),
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  _valiDate(datefrom),
                           'DateTo' : _valiDate(dateto),
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames
                           }
        self._pull = _requests.get(self._url, params=self._api_param, headers=my_headers)
    def log(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class rebound_log:
    def __init__(self,playerid,league='NBA',season='2015',seasontype=1,teamid=0,
                 outcome=1,location=1,month=0,seasonsegment=1,datefrom='',
                 dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                 period=0,lastngames=0):
        self._url = "http://stats.nba.com/stats/playerdashptreboundlogs?"
        self._api_param = {'PlayerID' : playerid,
                           'LeagueID': _nbaLeague(league),
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  _valiDate(datefrom),
                           'DateTo' : _valiDate(dateto),
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames
                           }
        self._pull = _requests.get(self._url, params=self._api_param, headers=my_headers)
    def log(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class shot_chart:
    def __init__(self,playerid,leagueid='',season='2015', seasontype=1,teamid=0,
                 gameid='',outcome=1,location=1,month=0,seasonsegment=1,
                 datefrom='',dateto='',opponentteamid=0,vsconf=1,vsdiv=1,
                 position=1,period=0,lastngames=0,aheadbehind=1,
                 contextmeasure=1,clutchtime=7,rookieyear='',
                 contextfilter='',startperiod='1',endperiod='10',startrange='0',
                 endrange='28800', gamesegment=1, rangetype='2'):
        if not rookieyear == '':
            rookieyear = _nbaSeason(rookieyear)
        self._url = "http://stats.nba.com/stats/shotchartdetail?"
        self._api_param = {'LeagueID': leagueid,
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'PlayerID' : playerid,
                           'GameID' : gameid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  _valiDate(datefrom),
                           'DateTo' : _valiDate(dateto),
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'Position' : _Position(position),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames,
                           'AheadBehind' : _AheadBehind(aheadbehind),
                           'ContextMeasure' : _ContextMeasure(contextmeasure),
                           'ClutchTime' : _ClutchTime(clutchtime),
                           'RookieYear' : rookieyear,
                           'ContextFilter':contextfilter,
                           'StartPeriod':startperiod,
                           'EndPeriod':endperiod,
                           'StartRange':startrange,
                           'EndRange':endrange,
                           'RangeType':rangetype,
                           }
        self._pull = _requests.get(self._url, params=self._api_param, headers=my_headers)
    def chart(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def leagueaverage(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

def PlayerList(season='2015', AllTime=False, league='NBA'):
    if AllTime:
        _url = "http://stats.nba.com/stats/commonallplayers?"
        _api_param = {'IsOnlyCurrentSeason':"0",
                      'LeagueID':_nbaLeague(league),
                      'Season': "2015-16"}
        _pull = _requests.get(_url, params=_api_param, headers=my_headers)
        _headers = _pull.json()['resultSets'][0]['headers']
        _values = _pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    else:
        _url = "http://stats.nba.com/stats/commonallplayers?"
        _api_param = {'IsOnlyCurrentSeason':"0",
                      'LeagueID': _nbaLeague(league),
                      'Season': _nbaSeason(season)}
        _pull = _requests.get(_url, params=_api_param, headers=my_headers)
        _headers = _pull.json()['resultSets'][0]['headers']
        _values = _pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

__all__ = ["demographics", "career_stats", "general_splits",
           "game_logs", "shot_dashboard", "rebound_dashboard",
           "passing_dashboard", "defense_dashboard", "shot_log",
           "rebound_log", "shot_chart"]
