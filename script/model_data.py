from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def model_stat(models, X_train, y_train, X_test, y_test):
    local_models = models

    for name, model in local_models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        probs = model.predict_proba(X_test)[:, 1]

        print(f"Model: {name}")
        print("Accuracy:", accuracy_score(y_test, preds))
        print("Precision:", precision_score(y_test, preds))
        print("Recall:", recall_score(y_test, preds))
        print("F1 Score:", f1_score(y_test, preds))
        print("ROC-AUC:", roc_auc_score(y_test, probs))
