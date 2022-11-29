import pandas as pd 


if __name__ == '__main__':
    
    ficheros = ['order_details_2016.csv','orders_2016.csv','pizza_types.csv','pizzas.csv']
    for i in range(0,len(ficheros)):
            print('limpieza de ficheros')
            print(' ')
            print(ficheros[i])
            if i == 0 or 2:
                df= pd.read_csv(ficheros[i],sep=";", encoding='LATIN-1')
            else:
                df= pd.read_csv(ficheros[i],sep=",", encoding='LATIN-1')
            print('\nNúmero de Nan por columna:')
            print(df.isna().sum())
            print('\nNúmero de nulls por columna:')
            print(df.isnull().sum())
            print("Los tipos de datos en las columnas son: ")
            print(df.dtypes)