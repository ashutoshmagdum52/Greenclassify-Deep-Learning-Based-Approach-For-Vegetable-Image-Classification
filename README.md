GreenClassify: Deep Learning-Based Vegetable Image Classification

GreenClassify is a web-based application that leverages deep learning techniques to classify images of vegetables. Built with Flask and Keras, it provides an intuitive interface for users to upload images and receive accurate predictions.

🚀 Features

Deep Learning Model: Utilizes a Convolutional Neural Network (CNN) trained on a diverse dataset of vegetable images.

Web Interface: User-friendly web application built with Flask.

Git LFS Integration: Model file managed using Git Large File Storage (LFS) for efficient version control.

🖼️ Sample Output

Include screenshots or examples of the application's interface and predictions here.

🛠️ Installation
Prerequisites

Python 3.6 or higher

Git

Git LFS

Steps

Clone the Repository

git clone https://github.com/ashutoshmagdum52/Greenclassify-Deep-Learning-Based-Approach-For-Vegetable-Image-Classification.git
cd Greenclassify-Deep-Learning-Based-Approach-For-Vegetable-Image-Classification


Install Git LFS and Pull Model Files

git lfs install
git lfs pull


Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies

pip install -r requirements.txt


Run the Application

python app.py


Access the application at http://localhost:5000.

🧠 Model Details

Architecture: Convolutional Neural Network (CNN)

Framework: Keras with TensorFlow backend

Model File: vegetable_classification.h5 (managed via Git LFS)

Include additional details about the model's architecture, training process, and performance metrics here.

📁 Project Structure
Greenclassify-Deep-Learning-Based-Approach-For-Vegetable-Image-Classification/
├── app.py
├── vegetable_classification.h5
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── logout.html
│   └── prediction.html
├── uploads/
├── .gitignore
├── .gitattributes
└── README.md

📄 License

Specify the license under which the project is distributed.

🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

📞 Contact

For any inquiries or feedback, please contact ashutoshmagdum52
.