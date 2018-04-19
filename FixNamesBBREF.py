import numpy as np
import pandas as pd
import os

os.chdir('/Users/michaerl/Documents/Stats2FinalProject')


def fix_names(filenameraw,outputfilename):
    ## get the df
    df = pd.read_csv(filenameraw)

    ## splits each row in column 'Player' at \  (need 2nd \ to read \)
    df['name'], df['id'] = zip(*df['Player'].map(lambda x: x.split('\\')))

    ## remove useless column Rk and then old Player, id
    df = df.drop(['Rk','Player','id'], axis=1)

    ## rename name -> Player like it initially was
    df.rename(columns={'name':'Player'}, inplace=True)

    ## moves player to first spot in data frame like it initially was
    df = df.reindex(['Player'] + list(df.columns[:-1]), axis=1)

    df.to_csv(outputfilename)

    return df



active = "ActivePlayersRaw.csv"
onballot = "OnHofBallotRaw.csv"

fix_names(active,"ActivePlayers.csv")
fix_names(onballot,"OnHoFBallot.csv")
