import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    mask = views.loc[views['author_id']==views['viewer_id']]
    return mask[['viewer_id']].drop_duplicates().sort_values(by='viewer_id').rename(columns={'viewer_id':'id'})