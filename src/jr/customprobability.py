from sklearn.ensemble import VotingClassifier

class CustomVotingClassifier(VotingClassifier):
    def __init__(self, estimators, voting='hard', weights=None, n_jobs=None, flatten_transform=True):
        super().__init__(estimators=estimators, voting=voting, weights=weights, n_jobs=n_jobs, flatten_transform=flatten_transform)
        self.estimators = estimators

    def predict_proba(self, X):
        avg = None
        for name, clf in self.estimators:
            proba = clf.predict_proba(X)
            if avg is None:
                avg = proba
            else:
                avg += proba
        avg /= len(self.estimators)
        return avg
