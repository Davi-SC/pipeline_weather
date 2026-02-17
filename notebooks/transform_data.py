import pandas as pd
from  pathlib import Path
import json

import logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


path_name = Path(__file__).parent.parent / 'data' / 'weather_data.json'

def create_dataframe(path_name:str) -> pd.DataFrame:
    path = path_name

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    
    with open(path) as f:
        data = json.load(f)
    
    df = pd.json_normalize(data)
    logging.info(f"\n Dataframe criado com {df.shape[0]} linhas e {df.shape[1]} colunas")

    return df