import numpy as np
import csv


with open("testing.txt", "r") as f:
    reader = csv.reader(f)
    testing_set  = [line for line in reader]

###################
# random baseline #
###################

random_predictions = np.random.choice([0, 1], size=len(testing_set))
random_predictions = zip(range(len(testing_set)), random_predictions)

with open("random_predictions.csv","w") as pred:
    csv_out = csv.writer(pred)
    csv_out.writerow(['id','predicted'])
    for row in random_predictions:
        csv_out.writerow(row)        

# note: Kaggle requires that you add "id" and "category" column headers

