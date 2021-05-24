from detectors.WindowedGaussianDetector import WindowedGaussianDetector
from detectors.bayes_changept_detector import BayesChangePtDetector
from detectors.numenta_detector import NumentaDetector
import os


Gaussian_obj = WindowedGaussianDetector()
Bayes_obj = BayesChangePtDetector()
numenta_obj = NumentaDetector()

# open file to write headers
result_path =  os.getcwd() + '\\results\\'
Gaussian_fileName =  result_path + 'Gaussian_results.csv'
f1 = open(Gaussian_fileName,"w")
f1.write("Timestamp,Value,Anomaly_score\n")
f1.close()
Bayes_fileName = result_path + 'Bayes_results.csv'
f2 = open(Bayes_fileName,"w")
f2.write("Timestamp,Value,Anomaly_score\n")
f2.close()
numenta_fileName = result_path + 'Numenta_results.csv'
f3 = open(numenta_fileName,"w")
f3.write("Timestamp,Value,Anomaly_score\n")
f3.close()


# function to create a resultant row
def create_result_row(inputData,score):
    timestamp = inputData["timestamp"]
    value = inputData["value"]
    Anomaly_score = score[0]
    print(f"Timestamp :{timestamp} ,Value :{value} , Anomaly_score :{Anomaly_score}")
    return str(timestamp)+","+str(value)+","+str(Anomaly_score)+"\n"

def runner(inputData):
    print("----")
    print(inputData)
    print("Windowed Gaussian Detector ")
    anomalyScore = Gaussian_obj.handleRecord(inputData)
    print (f"Anomaly Score : {anomalyScore}")
    result_file = create_result_row(inputData, anomalyScore)
    f1 = open(Gaussian_fileName,"a")
    f1.write(result_file)
    f1.close()
    print("Bayes Change Pt Detector")
    anomalyScore = Bayes_obj.handleRecord(inputData)
    print (f"Anomaly Score : {anomalyScore}")
    result_file = create_result_row(inputData, anomalyScore)
    f2 = open(Bayes_fileName,"a")
    f2.write(result_file)
    f2.close()
    print("-------")

    print("numenta Detector")
    anomalyScore = numenta_obj.handleRecord(inputData)
    print (f"Anomaly Score : {anomalyScore}")
    result_file = create_result_row(inputData, anomalyScore)
    f3 = open(numenta_fileName,"a")
    f3.write(result_file)
    f3.close()
    print("-------")
    
