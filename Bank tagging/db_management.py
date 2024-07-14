import json
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def secrets() -> json:
    """ 
    Getting secrets from json file for privacy purposes  
    """
    with open('secrets.json') as secrets_file:
        secrets = json.load(secrets_file)

    return secrets

def generate_engine(hidden):
    
    engine_url = f"postgresql://{hidden.get('NAME')}:{hidden.get('PASSWORD')}@localhost:5432/{hidden.get('NAME')}"
    engine_url = create_engine(engine_url)
    return engine_url

def sql_ingestion(desired_dataset:pd.DataFrame, named_table:str,engine_url):
    """
    using SQL alchemy to ingest pandas dataframe files into postgreSQL warehouse
    """
    try:
        # Create SQLAlchemy engine
        sql_server = engine_url

        # Upload the DataFrame to the SQL table
        desired_dataset.to_sql(named_table, sql_server, if_exists='append', index=False)
        
        return print('Successfully integrated')
        
    except SQLAlchemyError as e:
        return print('Error: Something went wrong')
    
def create_query(engine, query:str) -> pd.DataFrame:
    """
    create an SQL query using the query section. Example being: 
    SELECT * from expenditure_table limit 10;

    This will then be translated into a pandas dataframe
    """
    conn = engine.connect()
    # Query being made from function
    select_sql = query
    # Read query as SQL output 
    df = pd.read_sql_query(select_sql,conn)

    return df

       
        
    


