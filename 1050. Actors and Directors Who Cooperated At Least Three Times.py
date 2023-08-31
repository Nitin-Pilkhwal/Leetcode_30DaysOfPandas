import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped = actor_director.groupby(['actor_id','director_id']).count().reset_index()
    timestamp = grouped[grouped['timestamp']>=3]
    return timestamp[['actor_id','director_id']]