from imdb import IMDb
import numpy as np

def rateme(show):
    ia = IMDb()
    shows = ia.search_movie(show)
    my_show = shows[0]
    my_show_id = my_show.movieID
    ia.update(my_show, 'episodes')
    how_many_seasons = sorted(my_show['episodes'].keys())

    season_ratings = np.array([])
    season_ratings = np.split(season_ratings,len(how_many_seasons))
    count = -1
    for i in list(range(1,len(how_many_seasons)+1)):
        count+=1
        season_i = my_show['episodes'][i]
        indi_season = []
        for epi in list(range(1,len(season_i)+1)):
            rating = season_i[epi]['rating']
            indi_season.append(rating)
        season_ratings[count] = indi_season

    season_avg = []
    for i in season_ratings:
        avg = np.average(i)
        season_avg.append(avg)

    all_priors = np.average(season_avg[0:len(season_avg)-1])
    last_season = season_avg[len(season_avg)-1]

    percent_drop_beg_to_last = 100-(100*(last_season/all_priors))
    return percent_drop_beg_to_last

def dropoff(show1,show2):
    percent_drop_beg_to_last_1 = rateme(show1)
    percent_drop_beg_to_last_2 = rateme(show2)

    
    print(show1,'last season was',percent_drop_beg_to_last_1,'worse than all other seasons')
    print(show2,'last season was',percent_drop_beg_to_last_2,'worse than all other seasons')

dropoff('Game of Thrones','Breaking Bad')
