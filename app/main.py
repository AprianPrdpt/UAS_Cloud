from fastapi import FastAPI
import pandas as pd
import dask.dataframe as dd
from app.database import engine

app = FastAPI()

@app.get("/list")
def list_data():
    pdf = pd.read_sql("SELECT * FROM sensor_log", engine)

    ddf = dd.from_pandas(pdf, npartitions=2)

    df = ddf.compute()
    return df.to_dict(orient="records")
