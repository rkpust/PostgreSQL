import pandas as pd
from sqlalchemy import create_engine


engine = 'postgresql+psycopg2://postgres:12345678@localhost:5432/ToDoDB'

with pd.ExcelFile('ToDoList.xlsx') as xls:
    df = pd.read_excel(xls)
    # print(df)
    df.to_sql(name='todos_todo', con=engine, if_exists='append', index=False)


