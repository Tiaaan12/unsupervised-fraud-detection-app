from sklearn.ensemble import IsolationForest

def model_train(df):
    model = IsolationForest(random_state=42, n_estimators=283, contamination=0.008946057697978307, max_samples=0.44241943884813695, bootstrap=False)
    X = df.drop(columns=['is_fraud'], axis=1)
    
    model.fit(X)






