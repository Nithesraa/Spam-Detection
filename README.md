# 📩 Spam Detection System using Machine Learning

An end-to-end **Spam Detection System** that classifies SMS messages as **Spam** or **Not Spam** using **Natural Language Processing (NLP)** and **Machine Learning**.  
The model is trained using **TF-IDF vectorization** and **Multinomial Naive Bayes**, and deployed as an interactive **Streamlit web application**.

---

## 🚀 Features
- Classifies messages as **Spam 🚨** or **Not Spam ✅**
- High accuracy (**98.29%**)
- Clean and user-friendly UI
- Real-time prediction
- Color-coded results (Red for Spam, Green for Not Spam)
- Lightweight and fast inference

---

## 🧠 Machine Learning Approach

### 🔹 Data Preprocessing
- Lowercasing text
- Removing special characters
- Stopword removal
- Text normalization

### 🔹 Feature Extraction
- **TF-IDF Vectorization** (max_features = 3000)

### 🔹 Models Used
- Multinomial Naive Bayes ✅ *(Final Model)*
- Logistic Regression *(for comparison)*

---

## 📊 Model Performance

| Model | Accuracy |
|-----|---------|
| Naive Bayes | **98.29%** |
| Logistic Regression | 97.31% |

### Classification Highlights
- High precision for spam detection
- Minimal false positives
- Balanced and production-safe model


---

## 📁 Dataset
- **SMS Spam Collection Dataset**
- Source: UCI Machine Learning Repository
- Total messages: 5,574
- Labels: `spam`, `ham`

---

## 🖥️ Web Application (Streamlit)

The Streamlit app allows users to:
1. Enter an SMS message
2. Click **Check Message**
3. Instantly view the classification result with color-coded alerts

---




"# Spam-Detection" 
