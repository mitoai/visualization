from datetime import datetime


def get_trend_scores(df, company_row_name, date_row_name, trend_row_name) -> dict:
    sequences = {}
    for index, row in df.iterrows():
        key = row[company_row_name]
        score = row[trend_row_name]
        date_list = row[date_row_name].split(".")
        date = datetime(int(date_list[2]), int(date_list[1]), int(date_list[0]))
        if key in sequences:
            sequences[key][date] = score

        else:
            sequences[key] = {date: score}

    return sequences
