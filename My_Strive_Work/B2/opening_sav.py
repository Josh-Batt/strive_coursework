import pickle
import pandas as pd

# filename = 'finalized_model.sav'

# loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, Y_test)
# print(result)
# #print(loaded_model.predict())

df = pd.read_csv('joshu_input.csv')

filename = 'joshu_model.sav'
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
y_pred = loaded_model.predict(df)
cleanup_target = {"target": {"Car":1,"Still":2,"Train":3,"Bus":4,"Walking":5}}
result = loaded_model.score()
print(result)