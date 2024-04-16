def read_file(file_name, features_numbers):
    with open(file_name, 'r') as f:
        classes = []
        features = []

        lines = f.readlines()

        for line in lines:
            classes.append(line[0])

            line = line[2:]
            feature = [0] * features_numbers

            for l in line.split(" "):
                key, value = l.split(":")
                feature[int(key) - 1] = float(value)

            features.append(feature)

    return features, classes
