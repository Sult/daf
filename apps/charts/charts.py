import humanize
from collections import defaultdict
from apps.characters.models import CharacterJournal


#creates a highcharts dict for balance at downtime for last month
def monthly_balance(characterapi):
    dataset = nested_dict()
    #set basics
    dataset = default_chart(dataset)
    dataset = timeline(dataset)
    dataset['chart']['renderTo'] = 'monthlyBalance'

    #add series
    serie = {
        'name': "Isk balance",
        'data': CharacterJournal.monthly_balance(characterapi),
    }
    dataset['series'] = [serie]
    dataset['yAxis']['min'] = min_value_yaxis(dataset, y_min=0)

    #add strings
    dataset['title']['text'] = "ISK balance last 30 days"
    dataset['subtitle']['text'] = 'current isk: <span class="text-success">\
        <strong>%s</strong></span>' % humanize.intcomma(
        characterapi.current_balance()
    )
    dataset['yAxis']['title']['text'] = "Isk"

    return dataset


def weekly_balance(characterapi):
    dataset = nested_dict()
    #set basics
    dataset = default_chart(dataset)
    dataset = timeline(dataset)
    dataset['chart']['renderTo'] = 'monthlyBalance'

    serie = {
        'name': "Isk balance",
        'data': CharacterJournal.weekly_balance(characterapi),
    }
    dataset['series'] = [serie]
    dataset['yAxis']['min'] = min_value_yaxis(dataset, y_min=0)

    #add strings
    dataset['title']['text'] = "ISK balance last 7 days"
    dataset['subtitle']['text'] = 'current isk: <span class="text-success">\
        <strong>%s</strong></span>' % humanize.intcomma(
        characterapi.current_balance()
    )
    dataset['yAxis']['title']['text'] = "Isk"
    return dataset


def nested_dict():
    return defaultdict(nested_dict)


def default_chart(dataset):
    dataset['title']['useHTML'] = True
    dataset['subtitle']['useHTML'] = True
    dataset['credits']['enabled'] = False
    dataset['legend']['enabled'] = False
    return dataset


# set to timeline chart
def timeline(dataset):
    dataset['chart']['type'] = 'line'
    dataset['xAxis']['type'] = 'datetime'
    return dataset


def min_value_yaxis(dataset, **kwargs):
    all_data = []
    for serie in dataset['series']:
        all_data += serie['data']

    min_value = min(all_data, key=lambda x: x[1])[1]
    max_value = max(all_data, key=lambda x: x[1])[1]
    delta = max_value - min_value
    minimal = min_value - delta / 5

    if "y_min" in kwargs:
        if minimal < kwargs['y_min']:
            return kwargs['y_min']

    return minimal
