def submission(X_test_id, y_pred):
    with open ("../data/submission.csv", "w") as file:
        n = len(y_pred)

        file.write("Id, SalePrice")
        file.write("\n")

        for i in range(n):
            line = str(X_test_id[i]) + "," + str(y_pred[i])
            file.write(line)
            file.write("\n")
    print("Successfully created csv file")