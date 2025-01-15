import pandas as pd
import uvicorn
from fastapi import FastAPI

app = FastAPI()


def get_employees():
    df = pd.read_csv("../resources/employee_data.csv")
    head = df.head(10)
    data = head.to_dict(orient="records")
    return data


@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}


@app.get("/employee")
async def read_root():
    return get_employees()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
