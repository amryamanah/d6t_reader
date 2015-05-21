import csv
import os


HEADER = ["tPTAT", "tP0", "tP1",
          "tP2", "tP3", "tP4", "tP5", "tP6", 
          "tP7", "tP8", "tP9", "tP10", "tP11", 
          "tP12", "tP13", "tP14", "tP15", "TPEC"]

CSV_PATH = os.path.join(os.getcwd(), "temperature.csv")

def form_dct_result(data):
  return dict(zip(HEADER, data))

def create_csv_result():
  if not os.path.exists(CSV_PATH):
    with open(CSV_PATH, "w") as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=HEADER)
      writer.writeheader()

def write_csv_result(lst_result):
  with open(CSV_PATH, "a") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=HEADER)
    for data in lst_result:
      writer.writerow(data)
