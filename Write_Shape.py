import fiona
#reading in function, takes file as an argument
def write_file(df):

    #setting up fiona schema
    schema = {'geometry':'Point','properties':[('Name','str')]}
    #creating a fiona object
    shape = fiona.open('Shape Files/output.shp',mode = 'w',driver = 'ESRI Shapefile',schema=schema, crs = 'WGS84')

    #creating points list
    xy = []
    rowname = ''
    for i,j in df[['Longitude','Latitude']].iterrows():
        rowDict = {'geometry': {'type': 'Point', 'coordinates': (j.Longitude,j.Latitude)}, "properties": {'Name': None}}
        shape.write(rowDict)
    #writing and closing the file
    shape.close()








