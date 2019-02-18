import plotly.graph_objs as go
from plotly.offline import plot
from src.utils import sort_dates


def layout(title):
  return go.Layout(
    title=title,
    plot_bgcolor="rgb(244, 244, 248)",
    paper_bgcolor="rgb(244, 244, 248)",
  )


def plot_line(sequence: dict, title):
  fig = go.Figure()
  fig.layout = layout(title)

  fig.add_scatter(
    x=list(sequence.keys()),
    y=list(sequence.values())
  )

  plot(fig)


def plot_lines(sequences, title):
  fig = go.Figure()
  fig.layout = layout(title)

  for key in sequences:
    sorted_sequence = sort_dates(sequences[key])
    fig.add_scatter(
      x=list(sorted_sequence.keys()),
      y=list(sorted_sequence.values()),
      name=key
    )

  plot(fig)


def plot_bar(sequence: dict, title):
  fig = go.Figure()
  fig.layout = layout(title)

  fig.add_bar(
    x=list(sequence.keys()),
    y=list(sequence.values())
  )

  plot(fig)


def plot_bars(sequences, title):
  fig = go.Figure()
  fig.layout = layout(title)

  for key in sequences:
    sorted_sequence = sort_dates(sequences[key])
    fig.add_bar(
      x=list(sorted_sequence.keys()),
      y=list(sorted_sequence.values()),
      name=key
    )

  plot(fig)


def plot_bars_with_descriptions(sequences, title):
  fig = go.Figure()
  fig.layout = layout(title)

  for key in sequences:
    sorted_sequence = sort_dates(sequences[key])
    x_values = list(sorted_sequence.keys())
    y_values = list(map(lambda value:  value[0], list(sorted_sequence.values())))
    descriptions = list(map(lambda value: value[1], list(sorted_sequence.values())))
    urls = list(map(lambda value: value[2], list(sorted_sequence.values())))

    descriptions_urls = []
    for i in range(0, len(descriptions)):
      descriptions_urls.append("<a href='" + urls[i] + "'>" + descriptions[i] + "</a>")

    fig.add_bar(
      x=x_values,
      y=y_values,
      hovertext=descriptions_urls,
      hoverlabel=dict(
        bgcolor="#cee1ff",
      ),
      name=key,
    )

    plot(fig)


def plot_pos_neutral_neg_stacked_bars(sequence, title):

  neutral = {}
  positive = {}
  negative = {}

  for date in sequence:
    neutral_count = sequence[date].count('neutral')
    positive_count = sequence[date].count('positive')
    negative_count = sequence[date].count('negative')

    neutral[date] = neutral_count
    positive[date] = positive_count
    negative[date] = negative_count

  neutral = sort_dates(neutral)
  positive = sort_dates(positive)
  negative = sort_dates(negative)

  fig = go.Figure()

  fig.add_bar(
    x=list(negative.keys()),
    y=list(negative.values()),
    name="negative",
    marker=dict(
      color='rgb(255, 0, 0)',
      line=dict(
        color='rgb(8,48,107)',
      ),
    ),
    opacity=0.8
  )

  fig.add_bar(
    x=list(neutral.keys()),
    y=list(neutral.values()),
    name='neutral',
    marker=dict(
      color='rgb(58,200,225)',
      line=dict(
        color='rgb(8,48,107)',
      ),
    ),
    opacity=0.8
  )

  fig.add_bar(
    x=list(positive.keys()),
    y=list(positive.values()),
    name="positive",
    marker=dict(
      color='rgb(0, 255, 33)',
      line=dict(
        color='rgb(8,48,107)',
      ),
    ),
    opacity=0.8
  )

  fig.layout = go.Layout(
    barmode='stack',
    title=title
  )

  plot(fig)
