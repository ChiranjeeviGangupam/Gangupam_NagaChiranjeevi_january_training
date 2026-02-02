<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Spam Mail Detection using SVM</title>
</head>

<body style="font-family: Arial, Helvetica, sans-serif; background-color: #f8fafc; color: #1f2937; padding: 20px; line-height: 1.6;">

  <h1 style="text-align:center; color:#0f172a;">
    📧 Spam Mail Detection using Support Vector Machine (SVM)
  </h1>

  <p style="text-align:center; color:#475569; font-size:16px;">
    A Machine Learning project that classifies emails as <b>Spam</b> or <b>Ham</b> using
    <b>Support Vector Machine (SVM)</b> and Natural Language Processing techniques.
  </p>

  <hr style="margin:30px 0;">

  <h2>📌 Project Description</h2>
  <p>
    Spam emails are unsolicited messages that may contain advertisements, phishing attempts,
    or malicious links. Manual filtering is inefficient and error-prone.
    This project uses a <b>Support Vector Machine (SVM)</b> classifier to automatically
    detect spam emails based on their textual content.
  </p>

  <h2>🎯 Objectives</h2>
  <ul>
    <li>To preprocess and clean raw email text data</li>
    <li>To convert text into numerical features using TF-IDF</li>
    <li>To build a spam detection model using Support Vector Machine</li>
    <li>To evaluate the model using standard classification metrics</li>
  </ul>

  <h2>📂 Dataset Information</h2>
  <ul>
    <li><b>Input:</b> Email message text</li>
    <li><b>Target:</b> Spam / Ham (Not Spam)</li>
  </ul>
  <p>
    The dataset contains labeled email messages, making it suitable for supervised learning.
  </p>

  <h2>⚙️ Technologies & Tools Used</h2>
  <ul>
    <li>Python</li>
    <li>Pandas, NumPy</li>
    <li>Scikit-learn</li>
    <li>Natural Language Processing (NLP)</li>
    <li>Jupyter Notebook</li>
  </ul>

  <h2>🧠 Algorithm Used – Support Vector Machine (SVM)</h2>
  <p>
    Support Vector Machine is a supervised learning algorithm that finds the optimal
    hyperplane separating different classes with maximum margin.
  </p>
  <ul>
    <li>Effective for high-dimensional text data</li>
    <li>Works well with sparse feature vectors (TF-IDF)</li>
    <li>Provides high accuracy in spam classification tasks</li>
  </ul>

  <h2>🔄 Machine Learning Workflow</h2>
  <ol>
    <li><b>Data Loading</b> – Load the spam email dataset</li>
    <li><b>Text Preprocessing</b> – Lowercasing, removing punctuation & stopwords</li>
    <li><b>Feature Extraction</b> – TF-IDF Vectorization</li>
    <li><b>Train-Test Split</b> – Separate data for training and testing</li>
    <li><b>Model Training</b> – Train SVM classifier</li>
    <li><b>Prediction</b> – Classify emails as spam or ham</li>
    <li><b>Evaluation</b> – Measure performance using metrics</li>
  </ol>

  <h2>📊 Model Evaluation Metrics</h2>
  <ul>
    <li><b>Accuracy</b> – Overall correctness of predictions</li>
    <li><b>Precision</b> – Correctly identified spam emails</li>
    <li><b>Recall</b> – Ability to detect all spam emails</li>
    <li><b>F1-Score</b> – Balance between precision and recall</li>
  </ul>
  <pre>
--- Support Vector Machine (SVM) Model Evaluation with TF-IDF Features ---
Training Accuracy (SVM with TF-IDF): 0.9966101694915255
Testing Accuracy (SVM with TF-IDF): 0.9748305905130688

Classification Report (SVM with TF-IDF, Test Set):
               precision    recall  f1-score   support

         ham       0.98      0.99      0.99       917
        spam       0.93      0.84      0.88       116

    accuracy                           0.97      1033
   macro avg       0.96      0.91      0.93      1033
weighted avg       0.97      0.97      0.97      1033


Confusion Matrix (SVM with TF-IDF, Test Set):
 [[910   7]
 [ 19  97]]</pre>

  <h2>✅ Results</h2>
  <p>
    The Support Vector Machine model achieved high classification accuracy.
    SVM combined with TF-IDF vectorization proved effective in detecting spam emails
    with minimal false positives.
  </p>

  <h2>🚀 Conclusion</h2>
  <p>
    This project demonstrates the effectiveness of SVM for text classification problems.
    Spam mail detection using SVM provides a reliable and scalable solution for filtering
    unwanted emails in real-world applications.
  </p>





</body>
</html>
