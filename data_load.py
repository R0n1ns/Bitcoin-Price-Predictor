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

def data_drop(data,drop_col = []):
    """
        функия удаления нужных столбцов
    :param drop_col: нужно передать названима нужных столбцов в массивв�
    :return: возвращает датасет с удаленными столбцами
    """
    if drop_col != []:
        data = data.drop(drop_col, axis=1)
    return data

def cat_(data,cat):
    """
        переработка категориальных факторов
    :param data: данные в виде датафрейма pandas
    :param cat: столбцы с категориями для переработки в числовые факторы
    :return: датафрейм с без категариальных факторов
    """
    if  cat != []:
        data = pd.get_dummies(data, columns=cat,dtype=float)
    return data

def data_save(data,par = 'r',path = None):
    """
        сохранение датасета в фаил
    :param data: датасет
    :param par: параметр для запаковки датасета,r = только возвращает датасет, s = сохранение в файл, rs = сохранение в файл и возвращает датасет, по умолчанилю = 'r'
    :return:
    """
    if par == 'r':
        return data
    elif par == 's':
        data.to_csv(path, index=False)
    elif par == 'rs':
        data.to_csv(path, index=False)
        return data



def data_proc(data_loc,date=False,cat=[],drop = [],save = "r"):
    """
        переработка данных
    :param data_loc: расположение данных
    :param date: если = True о дата будет преобразована в три столбца, если = False то дата уберается, по умолчанию = False
    :param cat: нужно передать название категориальных факторов в массиве, по умолчанию = []
    :param save: параметр для запаковки датасета,r = только возвращает датасет, s = сохранение в файл, rs = сохранение в файл и возвращает датасет, по умолчанилю = 'r'
    :param drop: нужно передать названия нужных столбцов в массиве для удаления, по умолчанию = []
    :return: возвращает переработанный датасет
    """
    data = pd.read_csv(data_loc)
    data = date_(data,date)
    data = data_drop(data,drop)
    data = cat_(data,cat)
    path = data_loc[:-4]+"_proc.csv"
    data = data_save(data = data,par = save,path=path)
    return data