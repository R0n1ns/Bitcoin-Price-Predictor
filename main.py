from data_load import data_proc

#загрузка и подготовка данных
data_loc = 'BTC-USD_test.csv'
dt = data_proc(data_loc=data_loc,date=True,drop = ['Adj Close'],save="rs")
print(dt)



