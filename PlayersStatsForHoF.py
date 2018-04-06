import numpy as np
import pandas as pd
import os


## URL for the players we want to get stats from
##
## currently doing this manually, possible a way if we can
## find player ID (the final part of the html)
##
## can add players of interest here for future use
craigBiggio = "https://www.baseball-reference.com/players/b/biggicr01.shtml"
lanceBerkman = "https://www.baseball-reference.com/players/b/berkmla01.shtml"
toddHelton = "https://www.baseball-reference.com/players/h/heltoto01.shtml"
juanPierre = "https://www.baseball-reference.com/players/p/pierrju01.shtml"
kevinYoukilis = "https://www.baseball-reference.com/players/y/youklke01.shtml"
michaelYoung = "https://www.baseball-reference.com/players/y/youngmi02.shtml"

## list of URLS to iterate through
URLS = [craigBiggio,lanceBerkman,toddHelton,
        juanPierre,kevinYoukilis,michaelYoung]

## names in same order to add on later
names = ['Craig Biggio','Lance Berkman','Todd Helton',
         'Juan Pierre','Kevin Youkilis',"Michael Young"]

## gets the stats of the players
def getStats(URL):
    ## reads the correct table
    tables = pd.read_html(URL)[0]

    ## takes the tail to only get the last row, which is the players career stats
    ## we only want certain categories so we restrict the columns
    df = pd.concat([tables.tail(1)]).iloc[:,3:18]

    ## change column names because they aren't aligned correctly
    df.columns = ['AB','R','H','2B','3B','HR','RBI','SB',
                   'CS','BB','SO','BA','OBP','SLG','OPS']
    return df

## new list of data frames
futureHoF = []

for i in range( 0,len(URLS) ):
    ## iterate through each URLS, add to futureHoF
    futureHoF.append( getStats( URLS[i] ) )

## combine the list of dfs into one larger df
df = pd.concat( futureHoF )

## change the index of the rows to the players' name
df.index = names

## create csv
## os.chdir('/Users/michaerl/Documents')
## df.to_csv('futureHoF.csv')
