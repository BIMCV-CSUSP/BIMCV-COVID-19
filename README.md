# BIMCV-COVID-19
Following common strategies and initiatives emerged from the scientific community at international level, a series of actions are being carried out within the Valencia Region Image Bank (BIMCV) that combines data from the PADCHEST dataset with future datasets based on COVID-19 pathology to provide to the open scientific community, data of clinical-scientific value that helps early detection of COVID-19.

Medical Imaging Example of COVID-19 Rx from [medRxiv preprint doi](https://doi.org/10.1101/2020.02.14.20023028)
![ChestRX-COVID](https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/blob/master/chestRx/chest-covid.png)

## Objetivo
Recopilar y publicar las imágenes  de radiografía de tórax a las que se les eliminará cualquier dato que permita identificadas procedentes de los hospitales afiliados al BIMCV para el entrenamiento de modelos de Aprendizaje Profundo (Deep Learning o DL) que permita la detección precoz de infección y neumonía por Covid a partir de Radiografía por rayos X simple de tórax. 
Para ello, estas imágenes  se reestructurarán en subgrupos de imágenes procedentes del dataset PadChest con diagnósticos diferenciales relacionados con la semiología radiológica del COVID-19, de modo que permita desarrollar los primeros modelos basados en Inteligencia Artificial para predecir y comprender mejor la infección. 
## Acciones inmediatas a realizar
Nuestro grupo de investigación “Unidad Mixta de Imagen Biomédica FISABIO-CIPF” está trabajando para lanzar estos modelos utilizando la  plataforma de BIMCV (Openmind) de FISABIO que comparte con el CIPF, se trata de un conjunto de recursos computacionales comparte para afrontar estos retos a través de la red TransBioNet.
* Usando como base las imágenes de PadChest, y a la espera de que se nos autorice oficialmente por parte de las autoridades competentes, la extracción de conjunto nuevo de datos COVID-19 BIMCV de rayos X, se están realizado las siguientes tareas/acciones:
* Reorganización del dataset PadChest en patología relacionada con el curso de la patología COVID-19.
Extracción o organización de datos en subgrupos procedentes de PadChest (conocido en entornos de IA como Data curation) empezando con neumonía, infiltrados y controles).
* Particionado efectivo y bien equilibrado (ver figura 1)
* Preprocesado. Básicamente se van a almacenar las imágenes tanto en cluster como en Kaggle y preparadas en tres grupos de (entrenamiento o Train 60%, validación o Val 20%, prueba o Te 20%).
Se van a entrenar varios modelos y se dejarán en abierto aquellos con los que se obtenga una mejor precisión (accuracy) para que, cuando se adquiera el nuevo dataset BIMCV-COVID-19, se pueda realizar una transferencia de aprendizaje en nuevos modelos computacionales (Transfer-Learning) .

La base de datos PadChest se presenta particionada  en ["10 fold cross validation"](https://en.wikipedia.org/wiki/Cross-validation_(statistics)#k-fold_cross-validation) y siguiendo las siguientes criterios y/o especificaciones: 
* Conteos por sujeto y conteo de las particiones (Tr, Val y Te) total y por género
* El porcentaje total por partición para cada etiqueta de valor (tag separated value o tsv) generado.

Particionado PadChest:

![partition-COVID](https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/blob/master/chestRx/partition.png)
