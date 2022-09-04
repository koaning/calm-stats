import pandas as pd

def stack():
    """
    Stack new csv data on to some old one. 
    """
    new = "locust_stats_history.csv"
    old = "datasets/locust_stats_history.csv"
    pd.concat([pd.read_csv(new), pd.read_csv(old)]).to_csv(old)

stack()
