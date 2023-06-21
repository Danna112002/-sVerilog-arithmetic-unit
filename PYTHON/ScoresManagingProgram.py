#program typu bazodanowego polegajacy na rozbudowaniu odrobinę poprzedniego, utrzymany w tej samej konwencji rankingu wyników gier.
import os
import pandas
import os.path
#funkcja sprawdza istnienie pliku i liczy jego linie
def LineCounting(Scores):
    if os.path.isfile(Scores)==True:
        count = 0
#została tu użyta pętla do liczenia, bo metoda wbudowana zajmuje dość sporo zasobów
        with open(Scores) as f:
            for line in f:
                if line.strip():
                    count += 1
        f.close()
    else:
        print("Nie ma takiego pliku!! Koniec programu")
        exit()
    return count
#Funkcja zczytuje dane z pliku oraz wrzuca je w listę słowników
def ScoresReading(count, Scores):
    f=open(Scores, "r")
    LeaderboardClimbing=[]
    for i in range(0,count):
            s_temp=f.readline()
            l_temp=s_temp.split()
            LeaderboardClimbing.append({"nick":l_temp[0], "gra":l_temp[1], "wynik":l_temp[2]})
    #print(LeaderboardClimbing) - zakomnetowane, bo wiem, że działa, to wypluwanie całej listy niepotrzebne
    f.close()
    return LeaderboardClimbing
#funkcja sortuje wszystkie dane w tablicy poszerzonej o wyniki wpisane przez użyszkodnika
def ScoresSorting(NewestPlayerScores, InitialScore):
    result=[]
    NewResult=[]
    for i in range(len(NewestPlayerScores)):
            InitialScore.append(NewestPlayerScores[i])
    keys = InitialScore[0].keys()
    result=[[i[k] for k in keys] for i in InitialScore]
    result=sorted(result, key=lambda wynik: int(wynik[2]), reverse=True)
    #zamieniamy to z powrotem w listę słowników
    for i in range(0,len(result)): 
        NewResult.append({"nick": result[i][0], "gra": result[i][1], "wynik": result[i][2]})
    return  NewResult
#funkcja wyszukuje osobę po wpisanym nicku 
def ScoreSeraching(Scores, nick):
    record=[]
    for i in range(len(Scores)):
        if Scores[i]["nick"]==nick:
            record.append(Scores[i])
    if record==[]:
         print("W rankingu nie ma gracza o takim nicku")
    else:
        print("Dane gracza, którego szukasz to: ", record)
    return record
#funkcja umożliwia wpisanie customowych daych przez użyszkodnika
def KeyInYourScore():
    NewestPlayerScores=[]
    ConVar=input("Czy pragniesz wpisać nowe wyniki do tabeli? Jeżeli tak, wciśnij y.")
    if ConVar not in ('y','Y'):
        print("Żadne nowe wyniki nie zostały wprowadzone, więc elementy listy graczy się nie zmieniają.")
    while ConVar in ('y', 'Y'):
        while True:
            nick=input("Proszę wpisz swój nick ")
            if nick!='':
                break
        while True:
            gra=input("Proszę napisz, wynik jakiej gry chcesz zapisać: ")
            if gra!='':
                break
        while True:
            try:
                wynik=input("Proszę wpisz swój wynik wyrażony dodatnią liczbą naturalną: ")
                wart = int(wynik)
                if wart < 0:  # if not a positive int print message and ask for input again
                    print("Wpisana wartość nie jest dodatnia!")
                else:
                    break
            except ValueError:
                print("Bład! Wpisana wartość nie jest liczbą!!")  
        NewestPlayerScores.append({"nick":nick, "gra":gra, "wynik":wynik})
        ConVar=input("Jeżeli chcesz zakończyć wpisywanie nowych wyników wciśnij n, jeżeli chcesz kontynuować wciśnij y")
        if ConVar in ('n', 'N'):
            print("Wprowadzanie nowych wyników zakończone")
    return NewestPlayerScores
#funkcja konwertująca ostateczną tablicę do pliku csv
def csvConvertion(Scores):
    df=pandas.DataFrame(Scores)
    df.to_csv('FinalScores.csv', index=False, header=True)
    return df    
#main
if __name__ == '__main__':
    FilePath = os.path.join(os.getcwd(),"Scores.txt")
    MyCount=LineCounting(FilePath) #otwarcie pliku, z którego będziemy brać dane do listy słowników 
    MyScore=ScoresReading(MyCount, FilePath)
    NewestPlayerScores=KeyInYourScore()
    # Na razie zakładamy, że użyszkodnik sam wpisze swoje wyniki, de facto mogłyby być pobierane z jakiegoś innego pliku, ale po co, 
    #nie bedzie wtedy żadnej komunikacji między programem, a użyszkodniekiem.
    SortedScores=ScoresSorting(NewestPlayerScores, MyScore)
    if input("Czy pragniesz wyszukać jakąś osobę i jej wynik? Jeżeli tak wsiśnij y") in ('y','Y'):
        MySearch=input("Podaj nick grcza, którego wyników szukasz: ")
        ScoreSeraching(SortedScores,MySearch)
    else: 
        print("Niczyje wyniki nie były poszukiwane, koniec programu.")
    print("Teraz nastąpi konwersja danych do pliku csv obecnego w tym samym repozytorium co program oraz koniec programu.")
    csvConvertion(SortedScores)
    
