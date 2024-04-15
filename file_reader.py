def get_dna_data(file_name):
    with open(file_name, 'r') as f:
        classes = []
        features = []

        lines = f.readlines()

        for line in lines:
            classes.append(line[0])

            line = line[2:]
            feature = [0] * 180

            for l in line.split(" "):
                key, value = l.split(":")
                feature[int(key) - 1] = int(value)

            features.append(feature)

    return features, classes
