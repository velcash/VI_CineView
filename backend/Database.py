from sqlalchemy import create_engine
from backend import DataFilter as df

engine = create_engine('sqlite:///cine_view.db')

data = df.DataFilter('../Data')

#data.load_BOdata('boxoffice.csv').to_sql('boxoffice', con=engine)
#data.load_oscarData('Oscars.csv').to_sql('oscars', con=engine)
#data.load_palmeData('palmeDor.csv').to_sql('palme', con=engine)

p = engine.execute("SELECT * from boxoffice")

d, a = {}, []
for u in p:
    for column, value in u.items():
        # build up the dictionary
        d = {**d, **{column: value}}
    a.append(d)
print(a)
