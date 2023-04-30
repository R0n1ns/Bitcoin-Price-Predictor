import pandas as pd

def date_(data,date=False):
    """
        переработка даты
        :param data: данные
        :param date: если = True о дата будет преобразована в три столбца, если = False то дата уберается, по умолчанию = False        :return: возвращает датасет с разделенным категгориальным фактором
    """
    if not (date):
        data = data.drop(['Date'], axis=1)
    else:
        data["Day"] = [int(i.split("-")[2]) for i in data["Date"]]
        data["Month"] = [int(i.split("-")[1]) for i in data["Date"]]
        data["Year"] = [int(i.split("-")[0]) for i in data["Date"]]
        data = data.drop(['Date'], axis=1)
    return data

def data_proc(data_loc,date=False,cat=[]):
    """
        переработка данных
    :param data_loc: расположение данных
    :param date: если = True о дата будет преобразована в три столбца, если = False то дата уберается, по умолчанию = False
    :param cat: нужно передать название категориальных факторов в массиве, по умолчанию = []
    :return: возвращает датасет с разделенным категгориальным фактором
    """
    data = pd.read_csv(data_loc)
    if cat ==  []:
        return date_(data,date)
    else:
        data = date_(data,date)
        data = pd.get_dummies(data, columns=cat,dtype=float)
    return data