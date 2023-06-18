Team 1 - Traffic Flow Prediction using Deep Learning Models

Directory Structure:
-Models
  -Dataset
  -Evaluation Metrics
  -Flow
    -LSTM
    -GRU
    -SAE
  -Occupancy
    -LSTM
    -GRU
    -SAE
  -Speed
    -LSTM
    -GRU
    -SAE
-Report
  -Team1_Report.docx
  -Team1_Report.pdf
-Source Code
  -Team1_Experiment
  -Team1_ARIMA
  -Team1_DNN
  -crawler
  -README

Folders:
-Models
  Main Dataset => Dataset folder contains the Input_flow.csv, Input_occ.csv, Input_speed.csv and data.csv (Combined CSV File) files which is used for the traffic flow prediction.
  Toy Dataset => PeMSBay.csv file can be used as toy dataset consisting of only 4 months data for the traffic flow. (Download from the link provided below)
  Evaluation Metrics => Screenshots of all the graphs presented in the presentation of model comparison
  Flow, Occupancy, Speed => LSTM, GRU, SAE models .h5 files are stored which can be directly imported, pretrained and used for prediction along with screenshots

-Report
  Team1_Report.docx and Team1_Report.pdf files are the team project final report in IEEE format.

-Source Code
  Team1_Experiment, Team1_ARIMA, Team1_DNN Google Colab Notebooks for reference which conatins the whole project code along with comments.
  crawler.py is the source code for the web crawler written in Python using the BeautifulSoup library

Links for Google Colab Source Codes:
  PeMSBay:
    https://drive.google.com/drive/folders/1Kjmv7-lzI-bDWoQSl08lvp0P3ihZb3mS?usp=sharing
  Team1_Experiment:
    https://colab.research.google.com/drive/1K2aQbXKxCjAJXW-bvrrm2NJy33iAfUzX?usp=sharing
  Team1_ARIMA:
    https://colab.research.google.com/drive/1FrPjEH1oJkT-2YWpJWNWq2OzlxDqVv3t?usp=sharing
  Team1_DNN:
    https://colab.research.google.com/drive/1DLd4z67k3-5bmBrnJ1PxDaezme4Xh9lW?usp=sharing

Steps to run the code:
  Running the code is easy as it is hosted on Google Colab. 
  Run the Notebook and imported the dataset present in the /Models folder.
  For pretrained models, access /Models/Flow, /Models/Occupancy, /Models/Speed and import it in the code
  Run the cells present according to the Headers sequentially to get the model predictions and results.

