import csv, os

csv_path = "/home/ucla/Downloads/tianchi-2D/csv"
# csv_path = "/home/jenifferwu/IMAGE_MASKS_DATA/z-nerve/csv"
annotations_true_file = os.path.join(csv_path, "annotations.csv")
annotations_pred_file = os.path.join(csv_path, "imgs_mask_test_coordinate.csv")
statistics_file = os.path.join(csv_path, "statistics.csv")

########################################################################################################################
csvRows = []


def csv_row(seriesuid, coordX_error, coordY_error, coordZ_error, diameter_mm_error):
    new_row = []
    new_row.append(seriesuid)
    new_row.append(coordX_error)
    new_row.append(coordY_error)
    new_row.append(coordZ_error)
    new_row.append(diameter_mm_error)
    csvRows.append(new_row)


########################################################################################################################

# Read the annotations.csv in (skipping first row).
true_csvRows = []
csvFileObj = open(annotations_true_file)
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue  # skip first row
    true_csvRows.append(row)
csvFileObj.close()

# Read the imgs_mask_test_coordinate.csv in.
pred_csvRows = []
csvFileObj = open(annotations_pred_file)
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    pred_csvRows.append(row)
csvFileObj.close()

csv_row("seriesuid", "coordX-error", "coordY-error", "coordZ-error", "diameter_mm-error")
for true_row in true_csvRows:
    # print("true_row: ")
    # print(true_row)
    true_seriesuid = true_row[0]
    true_coordX = true_row[1]
    true_coordY = true_row[2]
    true_coordZ = true_row[3]
    true_diameter_mm = true_row[4]
    # print("True value: ")
    # print(true_seriesuid, true_coordX, true_coordY, true_coordZ, true_diameter_mm)
    for pred_row in pred_csvRows:
        # print("pred_row: ")
        # print(pred_row)
        pred_seriesuid = pred_row[0]
        pred_coordX = pred_row[1]
        pred_coordY = pred_row[2]
        pred_coordZ = pred_row[3]
        pred_diameter_mm = pred_row[4]
        # print("Prediction value: ")
        # print(pred_seriesuid, pred_coordX, pred_coordY, pred_coordZ, pred_diameter_mm)
        if true_seriesuid == pred_seriesuid:
            coordX_error = abs(float(true_coordX) - float(pred_coordX))
            coordY_error = abs(float(true_coordY) - float(pred_coordY))
            coordZ_error = abs(float(true_coordZ) - float(pred_coordZ))
            diameter_mm_error = abs(float(true_diameter_mm) - float(pred_diameter_mm))
            csv_row(true_seriesuid, coordX_error, coordY_error, coordZ_error, diameter_mm_error)

# Write out the statistics file.
print(statistics_file)
csvFileObj = open(statistics_file, 'w')
csvWriter = csv.writer(csvFileObj)
for row in csvRows:
    # print row
    csvWriter.writerow(row)
csvFileObj.close()