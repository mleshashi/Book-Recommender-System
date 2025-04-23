# 📚 Book Recommender System

Welcome to the **Book Recommender System** – A machine learning-based application that helps users discover books tailored to their preferences using collaborative filtering. Built using Python, Streamlit, and deployed via Docker on Google Cloud Platform (GCP), this app serves as an intelligent recommendation engine for book lovers.

---

## 🔗 Live Demo

🚀 [Try the Book Recommender System on GCP](https://book-recommender-latest-m3llqmtv6a-oe.a.run.app/)

---

## 📌 Features
- **Personalized Recommendations**: Get book suggestions based on your input using collaborative filtering.
- **Book Covers**: Visual representation of book recommendations using cover images.
- **Containerized**: Fully Dockerized application for ease of deployment and scalability.
- **GCP Deployment**: Deployed using Google Cloud Run for serverless scalability.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python (Collaborative Filtering)
- **Data**: Book-Crossing Dataset (cleaned & preprocessed)
- **Deployment**: Docker, Google Cloud Platform (Cloud Run)
- **Orchestration**: `docker-compose`

---

## 📁 Project Structure

```plaintext
Book-Recommender-System/
│
├── .vscode/                # VS Code config
├── data/                   # Raw and processed data files
├── resources/              # Saved models and assets (e.g., images)
├── src/                    # Source code and modules
│   ├── recommend.py        # Recommendation logic
│   └── fetch_poster.py     # Fetch book cover images
│
├── app.py                  # Main Streamlit app
├── brs_notebook.ipynb      # EDA and model training notebook
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Compose for local Docker deployment
├── requirements.txt        # Python dependencies
├── setup.py                # Project setup script
├── .dockerignore
├── .gitignore
└── README.md               # You're here!
```

---

## 🚀 How to Run Locally

### Prerequisites

- Python 3.12+
- Docker
- Git

---

### 1. Clone the Repo

```bash
git clone https://github.com/mleshashi/Book-Recommender-System.git
cd Book-Recommender-System
```

---

### 2. Build and Run with Docker

```bash
docker build -t book-recommender .
docker run -p 8501:8501 book-recommender
```

Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

### 3. Or Use Docker Compose

```bash
docker-compose up --build
```

---

## 🧠 How It Works

- The recommender is trained using **collaborative filtering** techniques on a matrix of users vs. books.
- Similarity is calculated using **cosine similarity** between book vectors based on user ratings.
- Once a user selects a book, the model retrieves similar books from the precomputed similarity matrix.
- **Book covers** are fetched dynamically using the Google Books API.

---

## 🧪 Model Training

To retrain the model:

1. Open `brs_notebook.ipynb`
2. Run all cells to:
   - Load and clean data
   - Create pivot tables
   - Train similarity model
   - Save the model to `/resources`

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

**Shashi MLE**  
📧 Connect: [LinkedIn](https://www.linkedin.com/in/mleshashi)  
📦 GitHub: [@mleshashi](https://github.com/mleshashi)

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on the [GitHub repository](https://github.com/mleshashi/Book-Recommender-System). Your support is greatly appreciated!

---
