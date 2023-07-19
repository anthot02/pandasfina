import pandas as pd
from data.platos import platosPopulares
from helpers.lanzarTabla import lanzartablaHTML

tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)
lanzartablaHTML(tablaPlatos,"tabla1")