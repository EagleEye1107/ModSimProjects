import random as rd
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

N = 100

prob = np.zeros((8,8))
df = pd.DataFrame(prob, columns = ['PSG', 'AMD', 'FCP', 'INT', 'BNF', 'VIL', 'SAL', 'CHE'], index = ['MNC', 'LIV', 'AFC', 'RMA', 'BAY', 'MUN', 'LIL', 'JUV'])

for j in range(N):
    seeded_teams = [
            [0, "Manchester City FC", "MNC", "ENG"],
            [1, "Liverpool FC", "LIV", "ENG"],
            [2, "AFC Ajax", "AFC", "NED"],
            [3, "Real Madrid CF", "RMA", "ESP"],
            [4, "FC Bayern München", "BAY", "GER"],
            [5, "Manchester United", "MUN", "ENG"],
            [6, "LOSC Lille",	"LIL", "FRA"],
            [7, "Juventus", "JUV", "ITA"]
        ]

    unseeded_teams = [
            [0, "Paris Saint-Germain", "PSG",	"FRA"],
            [1, "Club Atlético de Madrid", "AMD", "ESP"],
            [2, "Sporting Clube de Portugal", "FCP", "POR"],
            [3, "FC Internazionale Milano", "INT", "ITA"],
            [4, "SL Benfica", "BNF", "POR"],
            [5, "Villarreal CF", "VIL", "ESP"],
            [6, "FC Salzburg", "SAL", "AUT"],
            [7, "Chelsea FC", "CHE", "ENG"]
        ]

    first_teams = []
    second_teams = []


    try:
        while len(seeded_teams) != 0:
            possible_opponents = []
            team1 = rd.randint(0, len(seeded_teams)-1)

            for x in unseeded_teams:
                if (x[0] != seeded_teams[team1][0] and x[3] != seeded_teams[team1][3]):
                    possible_opponents.append(x)
            

            team2 = rd.randint(0, len(possible_opponents)-1)
            first_teams.append(seeded_teams[team1])
            second_teams.append(possible_opponents[team2])
            seeded_teams.pop(team1)
            unseeded_teams.remove(possible_opponents[team2])

        for i in range(8):
            prob[first_teams[i][0]][second_teams[i][0]] += 1

    except Exception:
        for k in range(8):
            j = rd.randint(0, 7)
            prob[k][j] += 1
        pass


df = df / N

for i in range(8):
    prob[i][:] = [x / N for x in prob[i]]

print(prob)
print(df)
sns.heatmap(df, annot=True, fmt = '.2f')
plt.show()