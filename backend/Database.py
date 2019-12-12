from sqlalchemy import create_engine
from backend import DataFilter as df

engine = create_engine('sqlite:///cine_view.db')

data = df.DataFilter('../Data')

data.load_BOdata('data.csv').to_sql('boxofficeRanked', con=engine)
data.load_oscarData('Oscars.csv').to_sql('oscars', con=engine)
data.load_palmeData('palmeDor.csv').to_sql('palme', con=engine)
