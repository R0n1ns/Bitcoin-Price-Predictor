from data_load import data_proc
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd
import matplotlib.pyplot as plt


#загрузка и подготовка данных
dt_train = pd.read_csv('BTC-USD_train_proc.csv')
X_train = dt_train[:-1]
Y_train = dt_train['Close'][1:]

dt_test = pd.read_csv('BTC-USD_test_proc.csv')
X_test = dt_test[:-1]
Y_test = dt_test['Close'][1:]


#Создание модели
acc_ = {}
def train():
    model = GradientBoostingRegressor(
        random_state=1,
        loss='quantile',
        n_estimators = 250,
        max_depth = 15,
        criterion = 'squared_error',
        learning_rate= 0.025,
        min_samples_leaf= 2,
        min_samples_split= 2

    )
    model.fit(X_train, Y_train)
    #предикат и метрика
    pred = model.predict(X_test)
    acc = mean_absolute_error(Y_test, pred)
    #acc_[acc] = [model.train_score_,model.init_]
    return model
tr = train()
pred = tr.predict(X_test)
print(acc_)

# def train():
#     model = GradientBoostingRegressor(
#         random_state=1,
#         loss='absolute_error',
#         n_estimators = 100,
#         max_depth = 50,
#         criterion = 'friedman_mse',
#         learning_rate= 0.025,
#         min_samples_leaf= 2,
#         min_samples_split= 2
#
#     )

#предикат и метрика

#отрисовка
plt.plot(pred)
plt.plot(Y_test)
plt.ylabel('some numbers')
# plt.show()
plt.savefig('saved_figure.png')