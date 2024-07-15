import requests
import json
import pandas as pd
import ast


def secrets() -> json:
    """ 
    Getting secrets for Splitwise API 
    """
    with open('secrets.json') as secrets_file:
        secrets = json.load(secrets_file)

    return secrets

def splitwise_get_expenses_api_call(api_key) -> json:
    API_KEY = api_key

    # Base URL for Splitwise API
    base_url = 'https://secure.splitwise.com/api/v3.0/'

    # Headers for authentication
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }

    # Params
    params = {
        'limit': 200
    }

    # Fetch expenses
    response = requests.get(f'{base_url}/get_expenses', headers=headers,params=params)
    expenses = response.json()

    return expenses

def initial_groupings(expense:json) -> pd.DataFrame:
    """
    return initial grouping from json to main grocery flat group on splitwise 
    """
    expense_df = pd.DataFrame(expense['expenses'])
    # this is group id for stebondale flat
    stebondale_group = expense_df[expense_df['group_id']==50024800]
    # return user info column that is a json 
    longer_user_info = pd.json_normalize(stebondale_group['users'])
    # join this expanded table into the initial table
    stebondale_group = stebondale_group.drop(columns=['users'])
    stebondale_expanded_group = stebondale_group.reset_index().join(longer_user_info)

    return stebondale_expanded_group

def parse_json(json_obj):
    """ 
    allow json files to be parsed and manipulated further
    """
    if isinstance(json_obj, str):
        return json.loads(json_obj)
    return json_obj

def source_groceries(table_info:pd.DataFrame, desired_columns: str) -> pd.DataFrame:
    """
    return parsed dataset to get columns 
    """
    table_info[desired_columns] = table_info[desired_columns].apply(parse_json)
    # return output of only name from the json category 
    table_info[desired_columns] = table_info[desired_columns].apply(lambda x: x['name'])

    groceries = table_info[table_info[desired_columns]=='Groceries']

    return groceries

def normalize_dataset(datafile:pd.DataFrame, desired_columns:str) -> pd.DataFrame: 
    """ 
    returns joined normalized data as this will be done for a number of columns
    """
    normalized_df = pd.json_normalize(datafile[desired_columns])
    
    # remove unwanted additional columns from json 
    normalized_df = normalized_df.drop(columns=['user_id','user.id','user.last_name','user.picture.medium'])

    # for ease of identification of columns as json columns would have duplicates with regards to who is in shopping event
    normalized_df = normalized_df.rename(columns={'paid_share':'paid_share_' + desired_columns, 'owed_share': 'owed_share_' + desired_columns
                                                    ,'net_balance': 'net_balance_' + desired_columns, 'user.first_name': 'user.first_name_' + desired_columns })
    
    
    return normalized_df

def saif_stebondale_expenses(grocery_df:pd.DataFrame) -> pd.DataFrame:
    """
    filter columns to only relation to my personal expenses
    """

    # look at user columns that json file parsed against
    user_columns = ['zero','one','two','three']

    for user in user_columns: 
        grocery_df['user.first_name_'+user] = grocery_df['user.first_name_'+user].astype(str)

    # create concatanated column of this to source out who was in the expense 
    grocery_df['concat_user'] = grocery_df[['user.first_name_zero',
                                            'user.first_name_one',
                                            'user.first_name_two',
                                            'user.first_name_three']].agg(''.join,axis=1)
    
    # return data specifically to my shopping events
    grocery_df_saif = grocery_df[grocery_df['concat_user'].str.contains('Saif')]

    return grocery_df_saif

    
def sourcing_saif_columns(pre_data:pd.DataFrame, column_index:int) -> pd.DataFrame:
    """from concat user use this as additional movements in data to return relevant fields"""
    
    # create dictionary for mapping 
    int_dict = {0:'zero',1:'one',2:'two',3:'three'}

    # Check if any of the 'concat_user' strings start with 'Saif' after splitting by '_'
    mask = pre_data['concat_user'].str.split('_').str[column_index] == 'Saif'

    filtered_df = pre_data[mask]
    
    # return relevant fields
    wanted_columns = filtered_df[['index','created_at',
                                  'description','category',
                                  'owed_share_'+int_dict[column_index],
                                  'net_balance_'+int_dict[column_index]]]
    
    wanted_columns = wanted_columns.rename(columns={'owed_share_'+int_dict[column_index]:'owed_share',
                                                    'net_balance_'+int_dict[column_index]:'net_balance'})
    
    wanted_columns = wanted_columns.drop(columns=['index'])
    
    wanted_columns = wanted_columns.reset_index()

    return wanted_columns