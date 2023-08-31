import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result_df = activity.sort_values(by=['player_id','event_date'])
    result_df = result_df.groupby('player_id')['event_date'].min().reset_index()
    result_df.rename(columns={'event_date':'first_login'},inplace=True)
    return result_df