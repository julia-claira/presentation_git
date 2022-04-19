
#QUERIES FLIX SQL BASED ON USER'S SELECTION AND RETURNS JSON to JS TO POPULATE TABLE

import pandas as pd
import sqlite3

def return_table(region,gender,generation,category):
    #Set up sqlite
    connection = sqlite3.connect('flix.db')
    
    
    #Assemble Query
    option_count=0
    if region=='all' or gender=='all' or generation=='all':
        sql_query="select *, sum(cast(replace(view,',','') as integer)) as views from flix_shows_kidz"
    else:
         sql_query="select *,cast(replace(view,',','') as integer) as views from flix_shows_kidz"
    
    if region!='all' or gender!='all' or generation!='all' or category!='all':
        sql_query=sql_query+" where"
    
    if region!='all': 
        sql_query=sql_query+f" viewing_country='{region}'"
        option_count=1
    if gender!='all':
        if option_count>0: sql_query=sql_query+" and"
        sql_query=sql_query+f" gender='{gender}'"
        option_count=1
    if generation!='all':
        if option_count>0: sql_query=sql_query+" and"
        sql_query=sql_query+f" generation='{generation}'"
    if category!='all':
        if option_count>0: sql_query=sql_query+" and"
        sql_query=sql_query+f" category='{category}'"
        
    if region=='all' or gender=='all' or generation=='all':
        sql_query=sql_query+" group by title order by Views desc"
        
    df=pd.read_sql_query(sql_query,connection)
    
    return df 