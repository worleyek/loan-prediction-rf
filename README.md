## Loan Approval Prediction: Random Forest Model & Deployed [Web App](https://loan-prediction-worleyek.streamlit.app/)

### Project Purpose:
To create a full machine learning project from scratch to deployment.

### Business Case:
To create a model that accurately predicts loan approval and automates the approval process.

### Goal:
To accurately predict loan approvals without falsely approving too many loans that should be denied (minimize false positives).

---

### Deliverable:
A web app that end users can utilize to predict loan approvals using a Random Forest model on the backend. Includes configurable credit score guideline in `loan-app.py`. 

    https://loan-prediction-worleyek.streamlit.app/

---

### In Repository:
1. Dataset (`loan_train.csv`)
2. Data dictionary (`data_dictionary.jpg`)
3. Random forest model creation (`loan_approval_model.ipynb`)
4. Sample decision tree from random forest model (`decision_tree.png`)
5. Web app Python code (`loan_app.py`)

---

### Business Context and Model Evaluation
From a business perspective, the goal of this model is to support loan approval decisions while minimizing financial risk and maintaining strong predictive coverage of eligible borrowers. In this setting, the most important concern is reducing false positives (incorrectly approving risky applicants), which makes precision a key evaluation metric.

Overall, the model performs well on the test dataset, achieving an accuracy of 81.25%, indicating that it correctly classifies approximately 4 out of every 5 loan applications.

**Precision:**

The model achieves a precision of `0.80`, meaning that when it predicts a loan approval, it is correct 80% of the time. This indicates a strong level of reliability in approved predictions, with some risk of false approvals.

**Recall:**

The model achieves a recall of `0.985`, meaning it correctly identifies nearly all actual approved applicants. This is a very strong result and indicates that the model rarely misses qualified borrowers. 

**F1 Score:**

The F1 score of `0.88` reflects a strong overall balance between precision and recall. It indicates that while the model prioritizes capturing all eligible applicants (high recall), it still maintains reasonable accuracy in its approval predictions (moderate precision).

**Accuracy:**

The overall accuracy of `81.25%` indicates solid general performance. However, accuracy alone does not fully capture model quality due to differing costs of misclassification.

---

### Conclusions
The model demonstrates a strong tendency to prioritize identifying approved applicants, as reflected by the extremely high recall. This ensures that very few eligible borrowers are missed, which is beneficial from a revenue perspective.

However, the trade-off is a moderate reduction in precision, meaning some applicants may be incorrectly predicted as approved. In a real-world lending environment, this would need to be carefully managed, as false approvals carry higher financial risk than false rejections.

Overall, the model is well-suited for scenarios where maximizing loan approvals and minimizing missed opportunities is prioritized, but it may require further tuning (such as threshold adjustment or class weighting) for risk reduction.

---

### Business Impact
End users will be able to use the web app built off of this model to predict loan approvals. There will be no missed revenue opportunities since the model captures all true approvals, and only a small portion of borrowers predicted to be approved will actually be denied. This will speed up the manual approval process and allow the company to process more loans in less time, resulting in more clients and revenue.

---

From here, we should monitor performance, tune the model further, and retrain with more data as it becomes available.
