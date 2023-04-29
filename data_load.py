import pandas as pd
def data_proc(data_loc,date=False,cat=[]):
    """
    переработка данных
    :param data_loc: расположение данных
    :param date: если = True о дата будет оставлено, если = False то дата уберается, по умолчанию = False
    :param cat: нужно передать название категориальных факторов в массиве, по умолчанию = []
    :return: возвращает датасет с разделенным категгориальным фактором
    """
    data = pd.read_csv(data_loc)
    if cat ==  []:
        if not(date):
            data = data.drop(['Date'], axis=1)
        data = pd.get_dummies(data, columns=["Value_Classification"])
        return data
    else:
        if not(date):
            data = data.drop(['Date'], axis=1)
        data = pd.get_dummies(data, columns=cat,dtype=float)

        return data