import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import pickle
from sqlalchemy import create_engine
import pymysql
import pandas as pd
from sklearn.model_selection import train_test_split


db_connection = 'mysql+pymysql://drax:mysql@localhost/mrp_database'
conn = create_engine(db_connection)

dataset = pd.read_sql("select * from history_sales_data", conn)
x = dataset.drop('id',axis=1)
x = x.drop('unit_produced',axis=1)
# print(x.describe())

compn = x.company_username.unique()
print(compn)

productn = x.product_username.unique()
print(productn)



for c in compn:
    for p in productn:
        new =  x[(x['company_username'] == c) & (x['product_username'] == p)]
        new = new.drop('company_username',axis=1)
        new = new.drop('product_username',axis=1)
        new = new.drop('year',axis=1)

        x1 = new.drop('price',axis=1)
        y1 = new['price']
        if len(x1.index)<12:
            breakb
        #print(x1)
        reg =  DecisionTreeRegressor(criterion= "mse",max_depth=None)
        reg.fit(x1,y1)

        e = DecisionTreeRegressor(criterion="mse",max_depth=None)
        new = new.drop('price',axis=1)
        new = new.drop('cost',axis=1)
        print(new.head())
        x2 = new.drop('unit_sold',axis=1)
        y2 = new['unit_sold']
        print("X2=============")

        print(x2)

        print("Y2=============")
        print(y2.describe())
        e.fit(x2,y2)
        f = c+'_'+p+'_price.pkl'
        pickle.dump(reg,open('D:/Codes/DJANGO Projects/MRP/ML_models/'+f,"wb"))
        pickle.dump(e,open('D:/Codes/DJANGO Projects/MRP/ML_models/'+c+"_"+p+"_demand.pkl","wb"))
        
