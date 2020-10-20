# BIMCV COVID19 iterations 1 + 2 Dataset

Thank you for your Interest in the BIMCV-COVID19 iterations Dataset.

Please read distribution rights at [LICENSE.md](LICENSE.md).


## Description

BIMCV-COVID19+ dataset is a large dataset with chest X-ray images CXR (CR, DX) and computed tomography (CT) imaging of COVID-19 patients along with their radiographic findings, pathologies, polymerase chain reaction (PCR), immunoglobulin G (IgG) and immunoglobulin M (IgM) diagnostic antibody tests and radiographic reports from Medical Imaging Databank in Valencian Region Medical Image Bank (BIMCV). The findings are mapped onto standard Unified Medical Language System (UMLS) terminology and they cover a wide spectrum of thoracic entities, contrasting with the much more reduced number of entities annotated in previous datasets. Images are stored in high resolution and entities are localized with anatomical labels in a Medical Imaging Data Structure \([MIDS](https://bimcv.cipf.es/bimcv-projects/mids/)\) format. In addition, 10 images were annotated by a team of expert radiologists to include semantic segmentation of radiographic findings. Moreover, extensive information is provided, including the patient’s demographic information, type of projection and acquisition parameters for the imaging study, among others. This first iteration of the database includes 1380 CX, 885 DX and 163 CT studies.

## Data Sources

This directory contains an anonymized dataset of torax Rx from COVID19 patients, prepared by the same authors as [PADCHEST dataset](http://bimcv.cipf.es/bimcv-projects/padchest) and described in the following preprint [arXiv:2006.01174](https://arxiv.org/abs/2006.01174).

* The dataset is spread over the 81 different tgz archives. For each one of the archives there is a corresponding `*.tar-tvf.txt` file with the list of files inside the archive.

* There are also three additional archives corresponding to: the metadata and several scripts \([covid19_posi_subjects.tar.gz](https://b2drop.bsc.es/index.php/s/BIMCV-COVID19-cIter_1_2/download?path=%2F&files=covid19_posi_subjects.tar.gz)\); the one corresponding to the header description of the datasets  \([covid19_posi_head.tar.gz](https://b2drop.bsc.es/index.php/s/BIMCV-COVID19-cIter_1_2/download?path=%2F&files=covid19_posi_head.tar.gz)\); and another one to the sessions \([covid19_posi_sessions_tsv.tar.gz](https://b2drop.bsc.es/index.php/s/BIMCV-COVID19-cIter_1_2/download?path=%2F&files=covid19_posi_sessions_tsv.tar.gz)\). Additionally, you can find more details about the metadata at <https://bimcv.cipf.es/bimcv-projects/bimcv-covid19/#1590859488150-148be708-c3f3> and <https://github.com/BIMCV-CSUSP/BIMCV-COVID-19>

* Files [sha1sums.txt](https://b2drop.bsc.es/index.php/s/BIMCV-COVID19-cIter_1_2/download?path=%2F&files=sha1sums.txt) and [sha1sums-b.txt](https://b2drop.bsc.es/index.php/s/BIMCV-COVID19-cIter_1_2/download?path=%2F&files=sha1sums-b.txt) have the SHA1 sums of all the archives and metadata in this dataset, as well as `*.tar-tvf.txt` and `LICENSE.md` files.

* NOTICE (20th October 2020): Due to the high demand of this dataset, it is recommended downloading the data through WebCAV protocol (please, see more details in the dataset webpage).
  
