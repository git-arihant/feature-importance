import sys
import pandas as pd
import math
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest,mutual_info_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score

model_for_feature_selection = mutual_info_classif
upper_limit_of_model = 500

file = sys.argv[1]
nf = int(sys.argv[2])

def data(file,nf):
    top_features_to_find = nf
    df = pd.read_csv(file)

    # Extracting feature names and splitting the data
    global features,x,y,scaler,x_train,x_test,y_train,y_test
    features = df.columns
    x = df.drop(['class'],axis=1)
    y = df['class']

    #Normalising the the data data
    scaler = StandardScaler()
    x = pd.DataFrame(scaler.fit_transform(x))
    x.columns = features[0:-1]

    #splitting the data into train and test
    x_train,x_test,y_train,y_test = train_test_split(x,y,random_state = 1,test_size=0.25)
    main_fun(x_train.columns,upper_limit_of_model,model_for_feature_selection,top_features_to_find)
    

# Function that distributes the features into subsets
def feature_divider(features,upper_limit):
    total_features = len(features)
    n_rows = math.floor(total_features/upper_limit)
    split = n_rows*upper_limit
    
    left_features = features[split:]
    features = features[:split]
    
    itr = 0
    feature_sets = []   # List of list of features in each set
    for i in range(n_rows):
        feature_sets.append(features[itr:itr+upper_limit])
        itr = itr + upper_limit
    return left_features,feature_sets
    
# Function that selects top k features from each subset and sorts it
def feature_selector(feature_sets,k,mod):
    top_k = []
    sorted_top_k = []
    top_feature = []
    selector = SelectKBest(mod,k=k)
    for i in range(len(feature_sets)):
        curr_df = x_train[feature_sets[i]]   #creating df for subset of feature
        selector_fit = selector.fit(curr_df,y_train)
        
        top_k.append(dict(zip(selector_fit.get_feature_names_out(),selector_fit.scores_)))
        top_k[i] = sorted(top_k[i].items(), key=lambda item: item[1],reverse=True)    
        top_feature.append(top_k[i][0])
    top_feature.sort(key = lambda x:x[1],reverse=True)
    
    for i in range(len(top_k)):
        for j in range(len(top_k)):
            if(top_k[j][0]==top_feature[i]):
                sorted_top_k.append(top_k[j])
    return sorted_top_k
    
# Selecting features from upper matrix and adding left features in it
def upper_matrix(sorted_top_k,left_features):
    final_features = []
    itr = len(sorted_top_k[0])
    for i in range(len(sorted_top_k)):
        for j in range(itr):
            final_features.append(sorted_top_k[i][j][0])
        itr -= 1
        if(itr == 0):
            break
    final_features += list(left_features)
    return final_features


def main_fun(features,upper_limit,mod,k):    
    # cutting out unimportant features with each iteration
    # features = x_train.columns
    # upper_limit = upper_limit_of_model
    # mod = model_for_feature_selection
    # k = top_features_to_find

    print("cutting out unimportant features with each iteration")
    while(len(features)>upper_limit):
        left_features, feature_sets = feature_divider(features,upper_limit)
        sorted_top_k = feature_selector(feature_sets,k,mod)
        final_features = upper_matrix(sorted_top_k,left_features)
        features = final_features
        print(len(features)) 
        
    # final iteration which selects top n features
    selector = SelectKBest(mod,k=k)
    selector_fit = selector.fit(x_train[features],y_train)
    top_n_features = selector_fit.get_feature_names_out()

    # writing selected features in file
    fp = open('top_features.txt','w')
    fp.write(str(top_n_features))
    fp.close()

    print("Writing done\nOpen top_features.txt to view top selected features")
    
data(file,nf)
