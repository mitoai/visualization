import pandas


def read_csv(path, columns=None):
  df = pandas.read_csv(path, sep=";", usecols=columns)
  return df


def sort_dates(sequence) -> dict:
  res = {}
  for (key, value) in sorted(sequence.items()):
    res[key] = value
  return res


def filter_on_threshold(sequences, threshold) -> dict:
  res = {}
  for sequence in sequences.keys():
    for date in sequences[sequence]:
      if abs(sequences[sequence][date]) > threshold:
        if sequence in res:
          res[sequence][date] = sequences[sequence][date]
        else:
          res[sequence] = {date: sequences[sequence][date]}
  return res


def filter_description_on_threshold(sequences, threshold) -> dict:
  for sequence in sequences.keys():
    for date in sequences[sequence]:
      if abs(sequences[sequence][date][0]) < threshold:
        sequences[sequence][date][1] = ""
        sequences[sequence][date][2] = ""

  return sequences


def get_sequences(df, sequence_row_name, x_row_name, y_row_name) -> dict:
  sequences = {}
  for index, row in df.iterrows():
    key = row[sequence_row_name]
    y_value = row[x_row_name]
    x_value= row[y_row_name]
    if key in sequences:
      sequences[key][x_value] = y_value

    else:
      sequences[key] = {x_value: y_value}

  return sequences
