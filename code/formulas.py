#Funcion 1
def leer_datos(ruta):
    df = pd.read_csv(ruta)
    df['TS'] = pd.to_datetime(df['TS'])
    
    return df

#Funcion 2
def filtrar_calcular_media(df, nombre):
    filtro = df[df['Tag'] == nombre]
    media = filtro['Value'].mean()
    return media

