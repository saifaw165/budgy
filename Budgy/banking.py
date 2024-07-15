import pandas as pd
import numpy as np
import datetime as dt


def sourcing_bill(bill:pd.DataFrame) -> pd.DataFrame:
    """
    Return relevant fields for billing bill and mapping things for differnet categories being:
    - Lifestyle
    - Life bills
    - Flat bills 
    - Income influx 
    """
    # mapping out to granularity level 2 (detail of categories above)
    bill['Category'] = np.where(bill['Description'].str.contains('TESCO STORES|ASDA|TIAN TIAN|MARKS&SPENCER|SAINSBURY|GARDENS FOOD AND , WINE '), 'Groceries',
                           np.where(bill['Description'].str.contains('TFL|TRAINLINE'), 'Transport', 
                           np.where(bill['Description'].str.contains('SKY SUBSCRIPTION|DISNEY PLUS|H3G|NHS|APPLECARE|GYM'),'Personal_bills',
                           np.where(bill['Type'] == 'S/O', 'Flat',
                           np.where((bill['Type']=='DPC') & (bill['Description'].str.contains('BETY NAVITASARI')),'Mum',
                           np.where(bill['Description'].str.contains('ZAKRIYA'),'Tutoring',   
                           np.where((bill['Description'].str.contains('E.ON|SECRET ESCAPES')) & (bill['Type']=='BAC'), 'Salary',
                           np.where(bill['Description'].fillna('').str.contains('FIVE GUYS|DUCK & WAFFLE|HANWOO VILLAGE|FRANCO MANCA|LIVERPOOLMU|MY OLD DUTCH|DEUN DEUN|RASA SAYANG|3KOBROS|THE BREAKFAST CLUB|THE PASTY SHOP|PRIME BURGER|LIFE4CUTS|PUTTSHACK|CINEWORLD|CAKE & BINGSOO|DELIVEROO|SEOUL BIRD|SECRET_E'),'Girlfriend_tax',
                                                                                                             
                                     'Other'))))))))
    
    # mapping out to granularity level 1 using new category field 
    bill['Buckets'] = np.where(bill['Category'].str.contains('Transport|Groceries'),'Lifestyle',
                      np.where(bill['Category'].str.contains('Mum|Personal_bills'),'Personal',
                      np.where(bill['Category'].str.contains('Tutoring|Salary'),'Income',
                      np.where(bill['Category']=='Flat','Flat','Other'))))
    
    # change date format to datetime 
    bill['Date'] = pd.to_datetime(bill['Date'],format='%d %b %Y')

    # return description columns seperating out certain columns
    bill['description1'] = bill['Description'].str.split(',', n=1).str[0]
    bill['description2'] = bill['Description'].str.split(',', n=2).str[1]

    # limit columns to only relevant fields 
    final_bill = bill[['Date','Type','Category','Description','description1','description2','Value']]
    
    return final_bill



def payday_month_start(date:pd.Timestamp,payday:int) -> pd.Timestamp:
    """
    Define the custom month by when your payday is 
    """
    # If the date is on or after the 25th, set the start to the 25th of the current month
    if date.day >= payday:
        return pd.Timestamp(year=date.year, month=date.month, day=payday)
    # If the date is before the 25th, set the start to the 25th of the previous month
    else:
        if date.month == 1:
            return pd.Timestamp(year=date.year - 1, month=12, day=payday)
        else:
            return pd.Timestamp(year=date.year, month=date.month - 1, day=payday)
        


            