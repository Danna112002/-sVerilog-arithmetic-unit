#Na chwilę obecną program jest 'toporny', zakłada maksimum akcji z wewnątrz, to znaczy z dostarczonych danych w funkcji, po zakończeniu rozrywki, ma coś zrobić
#dane zostały wymyślone w wywołaniach funkcji w dwóch ostatnich linijkach, jednakowoż program został napisany tak, by docelowo znajdowały się tam generowane losowo dane
#funkcja dodająca wynik najnowszej gry do tablicy InitialScore i sortująca tablicę InitialScore
def LeaderboardClimbing(InitialScore, NewestPlayerScores):
    result=([])
    for i in range(len(NewestPlayerScores)):
            InitialScore.append(NewestPlayerScores[i])
            InitialScore.sort(reverse=True)
            result+=([InitialScore.index(NewestPlayerScores[i])+1])
    print("Twoje pozycje w rankingu po wszystkich zagranych rundach to kolejno: ", result)
    return result
#funkcja wypluwajaca twój najlepszy wynik oraz najlepszy ranking ze sztywnej tupli danych
def YourBestScore(NewestPlayerScores, LeaderboadClimbingResults):
            result=max(NewestPlayerScores)
            print("Twój najlepszy wynik to: ", result)
            HighestScore=min(LeaderboadClimbingResults)
            print ("Twoja najwyższa pozycja w rankingu po wszystkich zagranych rundach wynosi: ", HighestScore)
#zainicjalizujmy sobie na początek potrzebny nam input w postaci tablic
MyResult=LeaderboardClimbing([100,105], (150,70,45))
YourBestScore((150, 70, 45), MyResult)


