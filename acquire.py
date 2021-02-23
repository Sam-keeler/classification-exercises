
# Make a function named get_iris_data that returns the data from the iris_db on the codeup data science 
# database as a pandas data frame. The returned data frame should include the actual name of 
# the species in addition to the species_ids. Obtain you


def get_iris_data(host = host, user = user, password = password):
    filename = 'iris.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        db = 'iris_db'
        df = pd.read_sql('SELECT * FROM measurements JOIN species USING(species_id)', f'mysql+pymysql://{user}:{password}@{host}/{db}')
        df.to_csv(filename)
        return df

# Make a function named get_titanic_data that returns the titanic data from the codeup data science database 
# as a pandas data frame. Obtain your data from the Codeup Data Science Database.

def get_titanic_data(host = host, user = user, password = password):
    filename = 'titanic.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        db = 'titanic_db'
        df = pd.read_sql('SELECT * FROM passengers', f'mysql+pymysql://{user}:{password}@{host}/{db}')
        df.to_csv(filename)
        return df