# ArcGIS-TrackSource
Cria base de dados do sistema viário do Brasil utilizando os mapas colaborativos do TrackSource.
Além do Sistema Viário, todas as outras feições existentes no projeto [TrackSource](http://tracksource.org.br/) serão importadas para essa base de dados vetorial.

## Para que serve?
Os arquivos do projeto TrackSource são disponibilizados em formato .img (Garmin). Nele constam todas as estradas e vias do Brasil, mapeadas de forma colaborativa. Tais mapas, muito frequentemente, são melhores que aqueles disponibilizados pelo IBGE em escala 1:250.000.

Dessa forma, para criar uam base de dados vetorial, é preciso converter de *.img* para *.mp*, por meio do software ***GPSMapEdit***, sendo esse um formato aberto de mapas de GPS.
Após isso é necessário converter os arquivos *.mp* para *.shp* (shapefile), por meio do software ***GlobalMapper***.

Somente com os arquivos shapefiles que o [script em python](Scripts/TrackSource.py) aqui disponibilizado deve ser aplicado, processando todos os arquivos conjuntamente para criar apenas uma base de dados.

![Project](ScreenShots/Project.png)

![Transformation](ScreenShots/Transformation.png)

## Como usar o Script?
1. Copiar todos os mapas .img (formato do TrackSource) da pasta aonde foi instalado o TrackSource para ..\Etapa_1\Maps
2. Aplicar a macro ConvertToNTM.vbs...que se encontra dentro de E:\GIS_Outros\BR_TrackSource\Converter\Etapa_1_img
3. Colocar os arquivos em formato .mp na pasta ..\Etapa_2
4. Usando a ferramenta Batch, interna, do Global Mapper, converter os arquivos .mp para shapefile...

Fazer o *download* (ou cópia) do arquivo [TrackSource.py](Scripts/TrackSource.py) e executar.

## Pré-requisitos
- TrackSource instalado;
- GPSMapEdit instalado;
- GlobalMapper instalado;
- ArcGIS instalado;

## Autor
* **Michel Metran**, veja [outros projetos](https://michelmetran.com)

Veja também a lista de [colaboradores](https://github.com/michelmetran/ArcGIS-TrackSource/settings/collaboration) que auxiliaram nesse projeto.

## Licença
Esse projeto é licenciado sob a 'MIT License'.

Veja o arquivo [LICENSE](LICENSE) para detalhes.

## Referências
1.	Sobre a [criação de transformações entre datum customizada no ArcGIS](http://desktop.arcgis.com/en/arcmap/10.5/tools/data-management-toolbox/create-custom-geographic-transformation.htm).
2.	Sobre [questões de geodésia definidas pelo IBGE](http://www.ibge.gov.br/home/geociencias/geodesia/pmrg/faq.shtm).
3.	Sobre [transformação entre referenciais geodésicos definidos pela Engenharia Cartográfica da UFRGS](http://www.ufrgs.br/engcart/Teste/refer_exp.html).
4.	Sobre os [parâmetros de transformações entre datum que existem, por *default*, no ArcGIS](http://help.arcgis.com/en/arcgisdesktop/10.0/help/003r/pdf/geographic_transformations.pdf).
