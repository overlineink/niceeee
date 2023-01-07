file_path = input('Insert your file into here\n')

file = open(file_path, 'r')
file_data = file.readlines()

res_array = []

for idx, line in enumerate(file_data, 1):
    helper = line.find('AGCT')

    res_array.append(helper)

    if (helper > 0):
      sequence = file_data[0].replace("\n", "")
      print(sequence + "\t" + str(len(line)) + "\t" + str(helper) + "\t" + str(idx))
