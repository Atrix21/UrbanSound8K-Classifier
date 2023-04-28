# Urban Sound Classification

This repository contains the code for a project that classifies audio files into different types of urban sounds using machine learning techniques. The project consists of three main components: a convolutional neural network (CNN) model trained on a dataset of urban sounds, a Flask API to deploy the trained model, and a Flutter mobile application that allows users to upload audio files and receive the predicted class probabilities.

# Requirements

The following libraries are required to run the project:
- TensorFlow 2.x 
- librosa 
- Flask 
- numpy 
- pandas 
- scikit-learn 
- Flutter SDK 
  
# CNN Model

The CNN model is built using TensorFlow 2.x and trained on a dataset of 8732 audio files that belong to 10 different classes of urban sounds. The model architecture consists of 4 convolutional layers, 2 pooling layers, and 2 fully connected layers. The input layer of the model takes a tensor of shape (batch_size, 40, 174, 1) where batch_size is the number of training examples in each batch. The output layer is a softmax layer that returns the predicted class probabilities. The model is trained for 30 epochs using a batch size of 64 and achieves an accuracy of 93.9% on the test set.

# Flask API

The Flask API is used to deploy the trained CNN model and provide a way for the Flutter app to make predictions on new audio files. The API exposes a single route /predict that accepts audio files in WAV format and returns the predicted class probabilities. The API is built using Flask and is hosted on an AWS EC2 instance.

# Hosting the Flask App on AWS EC2

To host the Flask app on an AWS EC2 instance, follow these steps:
- Launch an EC2 instance on AWS and configure it with a public IP address.
- Connect to the instance using SSH.
- Install the required libraries using pip install -r requirements.txt.
- Copy the code for the Flask app (app.py) to the instance.
- Import the model into your SSH instance.
- follow the steps from the the youtube playlist https://www.youtube.com/playlist?list=PL5KTLzN85O4KTCYzsWZPTP0BfRj6I_yUP videos 3-5.

# Flutter Mobile Application

The Flutter mobile application allows users to upload audio files and receive the predicted class probabilities from the deployed CNN model. The app is built using Flutter SDK and has a simple user interface that consists of two screens: a login screen and a home screen. The login screen allows users to log in using their phone number and a one-time password sent via SMS. The home screen allows users to upload audio files and receive the predicted class probabilities. The app communicates with the Flask API to make predictions on new audio files.

# Usage

To use the project, follow these steps:

- Clone the repository using git clone https://github.com/Atrix21/login_phoneno.git
- Install the required libraries using pip install -r requirements.txt for the Flask API.
- Install the flutter packages from the pubspec.yaml file availbale in the Flutter App folder of the repo.
- Train the CNN model using the code available in CNN1_US8K.ipynb file.
- Deploy the Flask API using python app.py 
- Run the Flutter app using flutter run on an emulator or physical device. 


# Conclusion

The Urban Sound Classification project demonstrates the use of machine learning techniques to classify audio files into different types of urban sounds. The project consists of a CNN model trained on a dataset of urban sounds, a Flask API to deploy the trained model, and a Flutter mobile application that allows users to upload audio files and receive the predicted class probabilities.

# Acknowledgements
- The UrbanSound8K dataset was obtained from the following source: https://urbansounddataset.weebly.com/urbansound8k.html
- The code for building the CNN model was adapted from the following kaggle notebook: https://www.kaggle.com/code/emrekayah/notebook-cnn 
- The process of creating an EC2 instance and configuring for flask : https://www.youtube.com/playlist?list=PL5KTLzN85O4KTCYzsWZPTP0BfRj6I_yUP
