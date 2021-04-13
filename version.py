import sklearn
import pickle
from sklearn.tree import DecisionTreeClassifier
print(sklearn.__version__)
print(pickle.compatible_formats)
pickle_in = open("model_tree.pkl", "rb")
clf = DecisionTreeClassifier(random_state=0)
model = pickle.load(pickle_in)
print(model.__doc__)
