filename_input = input('Insert your file into here\n')

filename = open(filename_input, 'r')
my_file = filename.readlines()

res_array = []

for idx, line in enumerate(my_file, 1):
  is_present = line.find('AGCT') > 0

  res_array.append(line.find('AGCT'))
  
  if (is_present):
    print('Motif found at line \t', idx)
    print(f'Sequence lenght %d \t' % len(line))

print(res_array.sort())