# coding: utf8
'''
# -------------------------------------------------------------------------------------------------------
# IMPORTAR SHAPEFILES DO PROJETO TRACKSOURCE PARA UM GEODATABASE
# -------------------------------------------------------------------------------------------------------
# Michel Metran
# Setembro de 2017

# Script elaborado para criar uma base de dados do sistema viário, a partir dos dados do Proeto TrackSource.
# http://tracksource.org.br/
# 

'''

# -------------------------------------------------------------------------------------------------------
# Módulos e Codificação
import os
import sys
import arcpy

reload(sys)
sys.setdefaultencoding('utf8')

# -------------------------------------------------------------------------------------------------------
# Variável de Input
project = r'E:\SIG_MP_BasesCartograficas\BR_TrackSource'
shapefiles = os.path.join(project, 'Converter', 'Etapa_2_shp')

# -------------------------------------------------------------------------------------------------------
# Variáveis de Ambiente do ArcGIS
arcpy.ResetEnvironments()
arcpy.env.overwriteOutput = True

# -------------------------------------------------------------------------------------------------------
# Cria a pasta 'Dados Brutos', caso não exista.
print '## Etapa 1: Create folders'

directorys = ['Etapa_2_shp', 'Etapa_3_select', 'Etapa_4_copy']
for directory in directorys:
    try:
        os.makedirs(os.path.join(project, 'Converter', directory))        
    except OSError:
        if not os.path.isdir(os.path.join(project, 'Converter', directory)):
            raise

# -------------------------------------------------------------------------------------------------------
# Select best resolution
print '## Etapa 2: Select best resolution'

# Set workspace
arcpy.env.workspace = shapefiles

featureclasses = arcpy.ListFeatureClasses()
for fc in featureclasses:
    out = os.path.join(project, 'Converter', 'Etapa_3_select', 'MP_' + os.path.splitext(fc)[0])
    print out
    arcpy.Select_analysis(fc, out, '"DataLevel" = 0')

# -------------------------------------------------------------------------------------------------------
# Ajust Fields
print '## Etapa 3: Ajusty Fields'

# Set workspace
path_in = os.path.join(project, 'Converter', 'Etapa_3_select')
path_out = os.path.join(project, 'Converter', 'Etapa_4_copy')
arcpy.env.workspace = path_in

# List Feature Class
featureclasses = arcpy.ListFeatureClasses()

for fc in featureclasses:
    print 'Analisando: ' + fc
    
    drop_field = []
    skip_field = ['OBJECTID', 'FID', 'Shape', 'Shape_Length', 'Shape_Area']
    keep_field = ['OBJECTID', 'FID', 'Shape', 'Shape_Length', 'Shape_Area', 'NAME', 'LAYER']
    
    fieldList = arcpy.ListFields(fc)
    for field in fieldList:
        if field.name not in keep_field and field.type not in keep_field:
            drop_field.append(field.name)
        
        print drop_field
    arcpy.DeleteField_management(fc, drop_field)
        
# -------------------------------------------------------------------------------------------------------

    fms = arcpy.FieldMappings()
    
    fieldList = arcpy.ListFields(fc)
    for field in fieldList:
        if field.name in skip_field:
            pass
        else:
            fm = arcpy.FieldMap()
            fm.addInputField(fc, field.name)
            if field.name == 'NAME':
                newfield = fm.outputField
                newfield.length = 200
                fm.outputField = newfield
            if field.name == 'LAYER':
                newfield = fm.outputField
                newfield.length = 200
                fm.outputField = newfield
            
            fms.addFieldMap(fm)
    
    arcpy.FeatureClassToFeatureClass_conversion(fc, path_out, fc, field_mapping=fms)

# -------------------------------------------------------------------------------------------------------
# Create Geodatabase e FeatureDatasets
print '## Etapa 4: Create Geodatabase e FeatureDatasets'

try:
    arcpy.CreatePersonalGDB_management(os.path.join(project, 'Geodata'), 'Geo_TrackSource.mdb')
except:
    print 'Erro qualquer no geodatabase'

datasets = ['TrackSource']
for ds in datasets:
    try:
        arcpy.CreateFeatureDataset_management(os.path.join(project, 'Geodata', 'Geo_TrackSource.mdb'), ds, arcpy.SpatialReference(4326))
    except:
        print 'Erro qualquer no geodatabase'

# -------------------------------------------------------------------------------------------------------
# Merge all MPs
print '## Etapa 5: Merge all MPs'

# Set workspace
path_in = os.path.join(project, 'Converter', 'Etapa_4_copy')
arcpy.env.workspace = path_in

# List Feature Class
featureclasses = arcpy.ListFeatureClasses()

# Set types
shapes = ['Point', 'Polygon', 'Polyline']

for shape in shapes:
    # Limpa a lista
    list_fcs = []    
    
    for fc in featureclasses:
        desc = arcpy.Describe(fc)
        if desc.shapeType == shape:
            list_fcs.append(os.path.join(path_in, fc))
            print list_fcs
    
    arcpy.Merge_management(list_fcs, os.path.join(project, 'Geodata', 'Geo_TrackSource.mdb', 'TrackSource', shape))    

# -------------------------------------------------------------------------------------------------------
# Deleta
print '## Etapa 5: Deleta Lixos'

directorys = ['Etapa_2_shp', 'Etapa_3_select', 'Etapa_4_copy']
for directory in directorys:
    try:
        shutil.rmtree(os.path.join(project, 'Converter', directory), ignore_errors=True)
    except OSError:
        if not os.path.isdir(os.path.join(project, 'Converter', directory)):
            raise

# -------------------------------------------------------------------------------------------------------
# Finalizando
arcpy.ResetEnvironments()
print '# ' + '-' * 100
print '# End'
