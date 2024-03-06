from sklearn.ensemble import VotingClassifier


class CustomVotingClassifier(VotingClassifier):
    def __init__(self, estimators, voting='hard', weights=None, n_jobs=None, flatten_transform=True):
        """
        Custom implementation of VotingClassifier that calculates the average probability
        of each class label across multiple estimators.

        Parameters:
        - estimators (list): List of (name, estimator) tuples.
        - voting (str, default='hard'): Voting strategy. Can be 'hard' or 'soft'.
        - weights (list, default=None): Optional list of weights for each estimator.
        - n_jobs (int, default=None): Number of jobs to run in parallel for `predict_proba`.
        - flatten_transform (bool, default=True): Whether to flatten the transform output.

        """
        super().__init__(estimators=estimators, voting=voting, weights=weights, n_jobs=n_jobs, flatten_transform=flatten_transform)
        self.estimators = estimators

    def predict_proba(self, X):
        """
        Predict class probabilities for input samples.

        Parameters:
        - X (array-like): Input samples.

        Returns:
        - avg (array-like): Average class probabilities across all estimators.

        """
        avg = None
        for name, clf in self.estimators:
            proba = clf.predict_proba(X)
            if avg is None:
                avg = proba
            else:
                avg += proba
        avg /= len(self.estimators)
        return avg
