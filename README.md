
📧 SMS & Text Spam Detection System

A Machine Learning and Deep Learning-based Binary Text Classification system designed to classify SMS text messages as *Spam* or *Ham* (Legitimate).

📊 Dataset Overview

* Source Dataset: SMS Spam Collection Dataset
* Total Records: 5,572 messages
* Target Classes:
  * Ham (Legitimate):** ~86.6% (4,825 samples)
  * Spam: ~13.4% (747 samples)

🧹 Data Cleaning & Preprocessing

1. Data Cleaning:
   * Checked and handled missing/null values.
   * Removed duplicate rows and unnecessary features.
2. Text Normalization:
   * Lowercased text, removed special characters, punctuation, and extra whitespace.
3. Dataset Splitting:
   * 80% Training set (4,457 samples)
   * 20% Testing set (1,115 samples)
4. Feature Engineering & Tokenization:
   * For Machine Learning:`TF-IDF Vectorizer` with `max_features=5000`.
   * For Deep Learning: Keras `Tokenizer` (`num_words=10000`) and Sequence Padding (`maxlen=100`, `padding='post'`).


## ⚙️ Model Architectures

1. **Logistic Regression (Machine Learning Baseline):**
   * Feature Input: TF-IDF Vectors
   * Max Iterations: 1000
2. **LSTM - Long Short-Term Memory (Deep Learning Model):**
   * `Embedding Layer` (input_dim=10000, output_dim=64, input_length=100)
   * `LSTM Layer` (64 units)
   * `Dropout Layer` (rate=0.5)
   * `Dense Layer` (32 units, ReLU activation)
   * `Output Layer` (1 unit, Sigmoid activation)

 📈 Performance & Metric Comparison
| Model               |  Accuracy  | Precision  | Recall     | F1-Score   |
| :---                | :---:      |   :---:    | :---:      | :---:      |
| Logistic Regression | 95.77%     | **98.42%** | 87.36%     | 92.56%     |
| LSTM (Deep Learning)| **95.81%** | 96.23%     | **89.61%** | **92.80%** |


📷 Model Evaluation Screenshots

![Class Distribution](screenshot/sms_class_distribution.png)
![Logistic Regression Results](screenshot/logistic_regression_results.png)
![LSTM Results](screenshot/lstm_results.png)
# cross-platform-spam-detector
NLP-based Cross-Platform Spam Detector for SMS, Email, and YouTube comments using Machine Learning and Deep Learning models.


## 📊 Model Evaluation & Best Model Selection

We evaluated 6 different Machine Learning and Deep Learning models for Spam Classification. Below is the comprehensive benchmark summary:

| Model Type | Model Name | Accuracy | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Machine Learning** | Logistic Regression | 0.9577 | 0.9842 | 0.8736 | 0.9256 |
| **Machine Learning** | **SVM (Linear)** 🏆 | **0.9776** | **0.9800** | **0.9400** | **0.9600** |
| **Machine Learning** | Random Forest | 0.9677 | 0.9746 | 0.9103 | 0.9414 |
| **Deep Learning** | LSTM | 0.9581 | 0.9623 | 0.8961 | 0.9280 |
| **Deep Learning** | GRU | 0.8752 | 0.7165 | 0.9691 | 0.8239 |
| **Deep Learning / Transformer** | **BERT** 🏆 | **0.9826** | **0.9776** | **0.9611** | **0.9693** |


### 🏆 Model Selection Summary
* **Best ML Model:** **SVM (Linear)** achieved the best performance among classical ML models with an Accuracy of **97.76%** and F1-Score of **0.9600**.
* **Best DL Model:** **BERT** achieved the highest performance overall with an Accuracy of **98.26%** and F1-Score of **0.9693**.
* **Final Deployment Model:** **BERT Model** was selected for the Web Application integration due to its superior contextual understanding, highest accuracy, and balanced Precision-Recall trade-off.






## 🚀 How to Run and Test the Web Application

Follow these steps to launch and test the Gradio Web Application using Google Colab:

### Prerequisites:
* Ensure that the trained BERT model folder (`bert_model`) is placed in your Google Drive at the path:
  `/content/drive/MyDrive/spam_detection/models/bert_model`



### Step-by-Step Instructions:

1. **Open the Notebook:**
   * Open the `notebooks/Spam_Detection_Web_Appipynb.ipynb` file from this repository in **Google Colab**.

2. **Run the Notebook:**
   * Click **Runtime** > **Run all** (or press `Ctrl + F9`).
   * When prompted, click **"Connect to Google Drive"** to allow the notebook to access the saved BERT model.

3. **Launch the Web Interface:**
   * Once all cells execute, navigate to the last cell output.
   * You can access the Web Interface in **two ways**:
     * **Inline Interface:** Test directly within the Colab notebook.
     * **Public URL:** Click the generated `https://xxxx.gradio.live` share link to open the full Web Application in a new tab.

4. **Testing the Application:**
   * Select a platform (**Email**, **SMS**, or **YouTube**).
   * Enter or paste any sample message into the input box.
   * Click **🔍 Analyze Message** to view classification results (Spam / Ham), confidence scores, highlighted spam indicators, and safety guidelines.

