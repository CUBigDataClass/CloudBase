
# coding: utf-8

# In[13]:


import numpy as np 
import csv
import math
from scipy import stats
import pandas as pd
import matplotlib.pylab as plt



# In[15]:


def GameAnalysis(d, team, opponent):
    point_diff = []
    mean_diff = []
    sum_diff = 0
    total_game = 0
    Nwin = 0
    Pwin = 0.0
    
    # team
    for each in d: 
        if each==team:
            for game in d[each]:
                # opponent
                if game[1]==opponent:
                    diff = game[3]-game[4]
                    point_diff.append(diff)
                    total_game+=1
                    sum_diff+=diff
                    dmean = sum_diff/total_game
                    mean_diff.append(dmean)
                    if diff>0:
                        Nwin+=1

    if len(mean_diff) == 0:
       print("\nEnter the right team name.\n\n")
       return 0
                    
    mean_diff.append(mean_diff[-1])    
    Pwin = Nwin/total_game
    
    if(int(mean_diff[-1]))>0:
        predict = "Win by " + str(int(mean_diff[-1]))
    else:
        predict = "Loss by " + str(abs(int(mean_diff[-1])))
    
    print("\n\n\nTeam: ", team)
    print("opponent: ", opponent)
    print("\ntotal games:", total_game)
    print("number of winnings games:", Nwin)
    print("Probability of winning:", Pwin, )
    print("prediction for next game:", predict)
    print("\n\n")
    
    x = []
    line_zero = []
    for i in range(total_game+1):
        x.append(i+1)
        line_zero.append(0)
    
    fig, ax = plt.subplots(figsize=(15,6))
    ax.set_xlim(0, total_game+2)
    ax.set_ylim(-50, 50)
    ax.plot(x[:-1], point_diff, color="steelblue", label = "games")
    ax.plot(x, mean_diff, color = "red",label = "mean")
    ax.set_xlabel("games",fontsize=12)
    ax.set_ylabel("points difference", fontsize=12)
    ax.grid(alpha=0.25)
    ax.legend()
    
    #return total_game, Nwin, Pwin, int(mean_diff[-1])
    
#GameAnalysisForTeams(d, "IND", "BOS")


# In[16]:


def TeamPerformance(d, header, data, team ="ATL"):
    #home/w,l/tp/fg/fga/fg%/3p/3pa/3p%/ft/fta/ft%/assist/turnover/opfg/opfga/opfg%      
    # 3    5. 6. 8.  9. 10. 11 12  13  14 15. 16   19.     22     24.   25.   26
    
    HomeAway = []
    WinLoss = []
    
    feature = {}
    for i in range (len(header)):
        if i in [0,3,5,6,8,9,10,11,12,13,14,15,16,19,22,24,25,26]:
                    feature[header[i]] = [] 

    for row in data:
        for i in range(len(row)):
            if i == 3:
                if row[i]=="Away":
                    HomeAway.append(0)
                else:
                    HomeAway.append(1)
            if i == 5:
                if row[i]=="L":
                    WinLoss.append(0)
                else:
                    WinLoss.append(1)
            if i in [0,6,8,9,10,11,12,13,14,15,16,19,22,24,25,26]:
                feature[header[i]].append(row[i]) 
    feature[header[3]] = HomeAway
    feature[header[5]] = WinLoss
    
    game_of_team = 0
    game_at_home = 0
    N_win_home = 0
    N_win_away = 0
    N_home = 0
    N_win = 0
    N_Loss = 0
    Point_Win = 0
    Point_Loss = 0
    AVG_point = 0.0
    AVG_FG = 0
    AVG_FGA = 0
    AVG_FGP = 0.0
    AVG_FG_W = 0
    AVG_FG_L = 0
    AVG_FGA_W = 0
    AVG_FGA_L = 0
    AVG_FGP_W = 0
    AVG_FGP_L = 0
    ThreeP = 0
    ThreePA = 0
    ThreePP = 0.0
    ThreeP_W = 0
    ThreePA_W = 0
    ThreePP_W = 0.0
    ThreeP_L = 0
    ThreePA_L = 0
    ThreePP_L = 0.0
    Assist = 0
    Assist_W = 0
    Assist_L = 0
    Turnover = 0
    Turnover_L = 0
    Turnover_W = 0
    
    
    for i in range (len(data)): 
        if feature[header[0]][i] == team:
            #percentage of win at home:
            game_of_team+=1
            if HomeAway[i]==1:
                game_at_home+=1
                if WinLoss[i] == 1:
                    # home and win:
                    N_win_home+=1
            if HomeAway[i]==0:
                if WinLoss[i] == 1:
                    # Away and Win:
                    N_win_away+=1
            # AVG points
            AVG_point+=int(feature[header[6]][i])
            # Field Goal:
            AVG_FG+=int(feature[header[8]][i])
            AVG_FGA+=int(feature[header[9]][i])
            AVG_FGP+=float(feature[header[10]][i])
            # Three Points shots
            ThreeP+=int(feature[header[11]][i])
            ThreePA+=int(feature[header[12]][i])
            ThreePP+=float(feature[header[13]][i])
            # Assist 
            Assist += int(feature[header[19]][i])
            # turnover 
            Turnover+= int(feature[header[22]][i])
            
            if WinLoss[i] == 1:
                N_win+=1
                Point_Win+=int(feature[header[6]][i])
                AVG_FG_W+=int(feature[header[8]][i])
                AVG_FGA_W+=int(feature[header[9]][i])
                AVG_FGP_W+=float(feature[header[10]][i])
                ThreeP_W+=int(feature[header[11]][i])
                ThreePA_W+=int(feature[header[12]][i])
                ThreePP_W+=float(feature[header[13]][i])
                Assist_W += int(feature[header[19]][i])
                Turnover_W+=int(feature[header[22]][i])
                
            if WinLoss[i] == 0:
                N_Loss+=1
                Point_Loss+=int(feature[header[6]][i])
                AVG_FG_L+=int(feature[header[8]][i])
                AVG_FGA_L+=int(feature[header[9]][i])
                AVG_FGP_L+=float(feature[header[10]][i])
                ThreeP_L+=int(feature[header[11]][i])
                ThreePA_L+=int(feature[header[12]][i])
                ThreePP_L+=float(feature[header[13]][i])
                Assist_L += int(feature[header[19]][i])
                Turnover_L+=int(feature[header[22]][i])
                
    P_win = (N_win_away+N_win_home)/game_of_team
                
    WinAtHome = N_win_home/game_at_home
    WinAway = N_win_away/(game_of_team - game_at_home)
    
    AVG_point = AVG_point/game_of_team
    AVG_Point_Win = Point_Win/N_win
    AVG_Point_Loss = Point_Loss/N_Loss
            
    AVG_FG = AVG_FG/game_of_team
    AVG_FG_W = AVG_FG_W/N_win
    AVG_FG_L = AVG_FG_L/N_Loss
    
    AVG_FGA = AVG_FGA/game_of_team
    AVG_FGA_W = AVG_FGA_W/N_win
    AVG_FGA_L = AVG_FGA_L/N_Loss
    
    AVG_FGP = AVG_FGP/game_of_team
    AVG_FGP_W = AVG_FGP_W/N_win
    AVG_FGP_L = AVG_FGP_L/N_Loss
    
    ThreeP = ThreeP/game_of_team
    ThreeP_W = ThreeP_W/N_win
    ThreeP_L = ThreeP_L/N_Loss
    
    ThreePA = ThreePA/game_of_team
    ThreePA_W = ThreePA_W/N_win
    ThreePA_L = ThreePA_L/N_Loss
    
    ThreePP = ThreePP/game_of_team
    ThreePP_W = ThreePP_W/N_win
    ThreePP_L = ThreePP_L/N_Loss
    
    Assist = Assist/game_of_team
    Assist_W = Assist_W/N_win
    Assist_L = Assist_L/N_Loss
    
    Turnover = Turnover/game_of_team
    Turnover_W = Turnover_W/N_win
    Turnover_L = Turnover_L/N_Loss
    
    # pecentage of winnint at home v.s. Away 
    print("\n\nTeam: ", team)
    print("\nWinning: ", N_win, "   Lossing: ", game_of_team - N_win)
    print("\nPercentage of winning:", round(P_win*100,2),"%")

    print("    Home:", round(WinAtHome*100, 2), "%")
    print("    Away:", round(WinAway*100,2), "%")

    print("\nAverage team point: ", round(AVG_point,1))
    print("    In Winning game: ", round(AVG_Point_Win,1))
    print("    In Lossing game: ", round(AVG_Point_Loss,1))

    print("\nAverage Field Goal: ", round(AVG_FG,1))
    print("    In Winning game: ", round(AVG_FG_W,1))
    print("    In Lossing game: ", round(AVG_FG_L,1))

    print("\nAverage Field Goal Attemptd: ", round(AVG_FGA,1))
    print("    In Winning game: ", round(AVG_FGA_W,1))
    print("    In Lossing game: ", round(AVG_FGA_L,1))
        
    print("\nAverage Field Goal Percentage: ", round(AVG_FGP*100,2),"%")
    print("    In Winning game: ", round(AVG_FGP_W*100,2),"%")
    print("    In Lossing game: ", round(AVG_FGP_L*100,2),"%")
    
    print("\nAverage Three Point Shots made: ", round(ThreeP, 1))
    print("    In Winning game: ", round(ThreeP_W,1))
    print("    In Lossing game: ", round(ThreeP_L,1))
    
    print("\nAverage Three Point Shots Attempted: ", round(ThreePA,1))
    print("    In Winning game: ", round(ThreePA_W,1))
    print("    In Lossing game: ", round(ThreePA_L,1))
    
    print("\nAverage Three Point Shots percentage: ", round(ThreePP*100, 2),"%")
    print("    In Winning game: ", round(ThreePP_W*100,2),"%")
    print("    In Lossing game: ", round(ThreePP_L*100,2),"%")
    
    print("\nAverage Assist: ", round(Assist,1))
    print("   Winning game: ", round(Assist_W,1))
    print("   Lossing game: ", round(Assist_L,1))
    
    print("\nAverage Turnover: ", round(Turnover,1))
    print("   Winning game: ", round(Turnover_W,1))
    print("   Lossing game: ", round(Turnover_L,1))
    print("\n\n\n")
    
    
#TeamPerformance(d, header, data, "GSW")


# In[22]:


def main():
    dfPMC = pd.read_csv("nba_games_stats.csv")
    dfPMC.head()

    d = {}

    with open("nba_games_stats.csv") as csv_file:
        raw = list(csv.reader(csv_file))
    header, data = raw[0], raw[1:]
    #print(len(data))

    for row in data:
        #for i in range(len(header)):
        if row[0] not in d:
            d[row[0]]=[[row[3], row[4], row[5], int(row[6]), int(row[7]), int(row[8]), int(row[9]), float(row[10]), int(row[11]), int(row[12]), float(row[13]), int(row[14]), int(row[15]), float(row[16]), int(row[19]), int(row[22]), int(row[24]), int(row[25]), float(row[26])]]
        else:
            d[row[0]].append([row[3], row[4], row[5], int(row[6]), int(row[7]), int(row[8]), int(row[9]), float(row[10]), int(row[11]), int(row[12]), float(row[13]), int(row[14]), int(row[15]), float(row[16]), int(row[19]), int(row[22]), int(row[24]),int(row[25]), float(row[26])])

    #home/op/w,l/tp/op/fg/fga/fg%/3p/3pa/3p%/ft/fta/ft%/assist/turnover/opfg/opfga/opfg%
    # 3   4.  5. 6. 7. 8.  9. 10. 11 12  13  14 15. 16   19.     22     24.   25.   26

    while True:
        choice = input("1. Game Analysis   2. Team Performance   3. quit\n")
        if choice == "1":
            t = input("Choose a team: ")
            op = input("Choose a opponent: ")
            GameAnalysis(d, t, op)
        elif choice == "2":
            team = input("Choose a team: ")
            TeamPerformance(d, header, data, team)
        elif choice == "3":
            return 0




if __name__ == "__main__":
    main()

