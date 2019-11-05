# Applying data analysis on medical data to help improve society's quality of life

# Abstract
Large hospitals can generate up to hundreds of terabytes of medical data each year and this amount only increases with time.
In many countries (almost all developed countries), hospitals are by law required to store this medical data for 5 to 10 years.
As (nascent) data scientists we recognize that this medical data may contain information that could help improve health care.
It is therefore very disappointing that as of today the large majority of medical data is simply stored and left unused, primarily due to privacy laws and regulations.
However, the consensus regarding these laws is starting to shift and effort is being made to help the medical field reap the benefits of Data Science. One of these efforts is a website called "The Cancer Imaging Archieve (TCIA)" https://www.cancerimagingarchive.net/
which contains a wealth of medical imaging data in a large variety of different forms (CT, MRI, microscopic biopsy, radiographs, ...)

In short, our goal is to refine medical data and extract useful information from it.

# Research questions
There's a lot of different questions one could ask depending on the considered data.
An example file is provided in this repository where the LIDC-IDRI dataset is briefly explored and some questions are investigated (results below). This dataset contains 1013 thoracic CT scans, and 2669 lung nodules (tumors) annotated by 4 different radiologists. Additionally some spreadsheets are provided which contain more information regarding count, size and malignancy of the tumors.

<img src="https://github.com/Senneschal/Data_Science_Alliance/blob/master/ctscan.png" alt="alt text" width="800" height="400">


**Somme possible research questions:**

* Is there a strong correlation between shape of tumors and their malignancy?

It is commonly known that malignant tumors have an anarchic shape while benign tumors tend to be more spherical. This could be verified/quantified using this dataset. The annotations can be turned into 3D shapes of which the sphericity can be determined.

![alt text](https://github.com/Senneschal/Data_Science_Alliance/blob/master/Sphericity.png)

* How well do the diagnosis agree of different radiologists and do they contract each other?

This specific dataset is particularly interesting for machine learning and computer aided diagnosis, which is something that could be explored in this project if this is an added value. Either way, because the diagnosis was performed by 4 radiologists independently one could look at the variance between the annotations of different radiologists and showcase the inconsistency of diagnosis between different radiologists. This problem may be much less prevalent when a computer performs this task.

<img src="https://github.com/Senneschal/Data_Science_Alliance/blob/master/annotations.png" alt="alt text" width="380" height="350">

* Are there certain regions in the lungs that are much more likely to develope lung tumors or are the rather homogeneously distributed?

Adding up all the annotations could provide insight into which areas of the lungs are most likely to develop tumors and result in a sort of "probability map" within a standardized lung volume

<img src="https://github.com/Senneschal/Data_Science_Alliance/blob/master/prob_map.png" alt="alt text" width="300" height="300">


* Is there a correlation between BMI and the prevalence of lung cancer?

Since the scale of each scan is known, one could estimate, for example, the size/BMI of the patient and find correlation with the annotated tumors. For simplicity I tried this by segmenting the lungs and using the lung volume instead.

![alt text](https://github.com/Senneschal/Data_Science_Alliance/blob/master/corr.png)

In this case a Pearson correlation of -0.03 was found, which is rather insignificant.

Note: see Some_Examples.ipynb for further details on these results and how they could be improved in the future.


# Dataset
"The Cancer Imaging Archieve (TCIA)" https://www.cancerimagingarchive.net/ contains a wealth of medical imaging data in a large variety of different forms (CT, MRI, microscopic biopsy, radiographs, ...)

WE SHOULD TRY TO FIND MORE MEDICAL DATA, PERHAPS NOT IMAGING DATA.

Some candidates:

### Nicer 
* https://www.nicer.org/en/data/nicer-database/


The nicer dataset contains cancer data (type of cancer, diagnosis, death...) for Switzerland by cantons. It seems to be complete and well organized. It respects medial naming conventions.
We need to request the access. 

You can find the description of it here : https://www.nicer.org/assets/files/data/ncd_4.1_abbrev_version_201706.pdf

### Ghdx health data 
* http://ghdx.healthdata.org/?fbclid=IwAR3PlLKVO_eOGYSjjPvuhDMzhpsCZC_WnYslJPYmOc7NgqC84XplYkVS-jU

# A list of internal milestones up until project milestone 2

## Data exploration 
* Request the datasets mentioned above. Find alternatives if we can't get them. 
* Start exploring and cleaning the different datasets, find additional sources of data if needed. 
* Compare and confront the different datasets

## Research questions 
* From this, refine the exploration ideas and the research question.

## General & team management  
* Package the work and define tasks and a more precise timeline. 
* We will refine or list of internal milestone with the data we get
* Refresh on Spark 

# Questions for TAa
It would be nice to have another source of medical data, perhaps not imaging data, does anyone happen to have a suggestion?
