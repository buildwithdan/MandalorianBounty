# from config import engine
# import pandas as pd

# def selectTable2():
#     # Define query
#     query = "SELECT * FROM public.bounties3 ORDER BY bounty_amount DESC"

#     # Read the SQL query into a pandas DataFrame using the SQLAlchemy engine
#     df = pd.read_sql_query(query, engine)

#     # html_table = df.to_html(index=False, classes="my-table")
    
#     # Return the DataFrame
    
#     # Print the DataFrame
#     # print(df)
#     return df


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return f'<User {self.username}>'