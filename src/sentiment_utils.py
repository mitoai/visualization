from datetime import datetime


def sentiment_sequences(df, company_row_name, date_row_name, sentiment_row_name) -> dict:
  sequences = {}
  for index, row in df.iterrows():
    key = row[company_row_name]
    sentiment = row[sentiment_row_name]
    date_list = row[date_row_name].split("-")
    date = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2][:date_list[2].find(' ')]))
    value = sentiment[sentiment.find('(') + 1:sentiment.find(',')]
    if key in sequences:
      if date in sequences[key]:
        sequences[key][date].append(value)
      else:
        sequences[key][date] = [value]
    else:
      sequences[key] = {date: [value]}
  return sequences


def get_sentiment_scores(df, company_row_name, date_row_name, sentiment_row_name) -> dict:
  sequences = sentiment_sequences(df, company_row_name, date_row_name, sentiment_row_name)

  for sequence in sequences.keys():
    for date in sequences[sequence]:
      score = sequences[sequence][date].count('positive') - sequences[sequence][date].count('negative')
      sequences[sequence][date] = score

  return sequences


def sentiment_sequences_with_description(df, company_row_name, date_row_name, sentiment_row_name, description_row_name, url_row_name) -> dict:
  sequences = {}
  for index, row in df.iterrows():
    key = row[company_row_name]
    sentiment = row[sentiment_row_name]
    date_list = row[date_row_name].split("-")
    date = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2][:date_list[2].find(' ')]))
    description = row[description_row_name]
    url = row[url_row_name]
    value = (sentiment[sentiment.find('(') + 1:sentiment.find(',')], description, url)
    if key in sequences:
      if date in sequences[key]:
        sequences[key][date].append(value)
      else:
        sequences[key][date] = [value]
    else:
      sequences[key] = {date: [value]}
  return sequences


def get_sentiment_scores_with_description(df, company_row_name, date_row_name, sentiment_row_name, description_row_name, url_row_name) -> dict:
  sequences = sentiment_sequences_with_description(df, company_row_name, date_row_name, sentiment_row_name, description_row_name, url_row_name)

  for sequence in sequences.keys():
    for date in sequences[sequence]:
      sentiments = list(map(lambda x: x[0], sequences[sequence][date]))
      description_url_list = (list(map(lambda x: x[1],filter(lambda x: x[0] == 'positive' or x[0] == 'negative', sequences[sequence][date]))),
                              list(map(lambda x: x[2],filter(lambda x: x[0] == 'positive' or x[0] == 'negative', sequences[sequence][date]))))

      description_url = most_counted_description(description_url_list)
      score = sentiments.count('positive') - sentiments.count('negative')
      sequences[sequence][date] = [score, description_url[0], description_url[1]]

  return sequences


def most_counted_description(description_url_list) -> tuple:
  x = {}

  counter = 0
  for e in description_url_list[0]:
    if e in x:
      x[e][0] += 1
    else:
      x[e] = [0, description_url_list[1][counter]]
    counter += 1

  res = (0, "", "")
  for key in x:
    if x[key][0] > res[0]:
      res = (x[key][0], key, x[key][1])

  return res[1], res[2]
