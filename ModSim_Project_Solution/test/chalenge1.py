import random as rd

seeded_teams = [
        ["A", "Manchester City FC", "MNC", "ENG"],
        ["B", "Liverpool FC", "LIV", "ENG"],
        ["C", "AFC Ajax", "AFC", "NED"],
        ["D", "Real Madrid CF", "RMA", "ESP"],
        ["E", "FC Bayern München", "BAY", "GER"],
        ["F", "Manchester United", "MUN", "ENG"],
        ["G", "LOSC Lille",	"LIL", "FRA"],
        ["H", "Juventus", "JUV", "ITA"]
    ]

unseeded_teams = [
        ["A", "Paris Saint-Germain", "PSG",	"FRA"],
        ["B", "Club Atlético de Madrid", "AMD", "ESP"],
        ["C", "Sporting Clube de Portugal", "FCP", "POR"],
        ["D", "FC Internazionale Milano", "INT", "ITA"],
        ["E", "SL Benfica", "BNF", "POR"],
        ["F", "Villarreal CF", "VIL", "ESP"],
        ["G", "FC Salzburg", "SAL", "AUT"],
        ["H", "Chelsea FC", "CHE", "ENG"]
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

    print("------------------------------------------------------------------------------------------------------------")
    for i in range(8):
        print(f"({first_teams[i][1]}) VS ({second_teams[i][1]})")

except Exception:
    print("Conflict")