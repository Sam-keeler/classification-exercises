# Create a function named prep_iris that accepts the untransformed iris data, and returns the data 
# with the transformations above applied.

def prep_iris(x):
    x.drop(columns = ['species_id', 'measurement_id'], inplace = True)
    x.rename(columns = {'species_name': 'species'}, inplace = True)
    dummies = pd.get_dummies(x[['species']])
    x = pd.concat([x, dummies], axis=1)
    return x

def clean_iris(iris):
    train_validate, test = train_test_split(iris, test_size=0.2, random_state=1920)
    train, validate = train_test_split(train_validate, train_size=0.7, random_state=1920)
    return train, test, validate