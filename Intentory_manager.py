import pandas as pd
import os

if not os.path.exists('Data_Store.csv'):
    df = pd.DataFrame([['0','TEST', 'TEST', '5']],columns= ['index','ITEM_NAME', 'TYPE', 'QTY'])
    df.to_csv('Data_Store.csv', index=False)


def New_item(ITEM_NAME, TYPE_UNIT, QTY):
    df = pd.read_csv('Data_Store.csv', index_col=0)
    new_data = pd.DataFrame([[ITEM_NAME, TYPE_UNIT, QTY]], columns= ['ITEM_NAME', 'TYPE', 'QTY'])
    df = pd.concat([df, new_data], ignore_index=True)
    try:
        df = df.drop(['index'], axis=1)
    except:
        pass
    df['index'] = df.reset_index().index
    df = df.reset_index()
    df.to_csv('Data_Store.csv', index=False)

def Remove_item(ITEM_NUMBER):
    df = pd.read_csv('Data_Store.csv')
    df = df.drop(df.index[int(ITEM_NUMBER)])
    try:
        df = df.drop(['index'], axis=1)
    except:
        pass
    df['index'] = df.reset_index().index
    df.to_csv('Data_Store.csv', index=False)

def display_items():
    df = pd.read_csv('Data_Store.csv')
    df = df[['index', 'ITEM_NAME', 'TYPE', 'QTY']]
    df = df.reset_index(drop=True)
    return df.columns.values.tolist(), df.values.tolist()

def edit_item(ITEM_NUMBER, ITEM_NAME, TYPE_UNIT, QTY):
    df = pd.read_csv('Data_Store.csv')
    df.at[int(ITEM_NUMBER),'ITEM_NAME']=ITEM_NAME
    df.at[int(ITEM_NUMBER),'TYPE']=TYPE_UNIT
    df.at[int(ITEM_NUMBER),'QTY']=QTY
    df.reset_index(drop=True)
    df.to_csv('Data_Store.csv', index=False)

def return_value(ITEM_NUMBER):
    df = pd.read_csv('Data_Store.csv')
    df = df.reset_index(drop=True)
    df = df.loc[ITEM_NUMBER]
    return df.values.tolist()

