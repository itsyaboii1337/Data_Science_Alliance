# Title

# Abstract
Large hospitals can generate up to hundreds of terabytes of medical data each year and this amount only increases with time.
In many countries (almost all developed countries), hospitals are by law required to store this medical data for 5 to 10 years.
As (nascent) datascientists we recognize that this medical data may contain information that could help improve health care.
It is therefore very dissapointing that as of today the large majority of medical data is simply stored and left unused, primarily due to privacy laws and regulations.
However, the consesus regarding these laws is starting to shift and effort are being made to help the medical field reap the benefits of Data Science. One of these effort is a website called "The Cancer Imaging Archieve (TCIA)" https://www.cancerimagingarchive.net/
which contains a wealth of medical imaging data in a large variety of different forms (CT, MRI, microscopic biopsy, radiographs, ...)

In short, our goal is to refine medical data and extract useful information from it.

# Research questions
There's a lot of different questions one could ask depending on the concidered data.
An example file is provided in this repositoy where the LIDC-IDRI dataset is briefly explored and some questions are investigated (results below). This dataset contains 1013 thoracic CT scans, and 2669 lung nodules (tumors) annoted by 4 different radiologists. Additionally some spreadsheets are provided which contain more information regarding count, size and malignancy of the tumors.

<img src="https://github.com/Senneschal/Data_Science_Alliance/blob/master/ctscan.png" alt="alt text" width="300" height="300">


**Some ideas:**

* It is commonly known that malignant tumors have an anarchic shape while benign tumors tend to be more spherical. This could be verified/quantified using this dataset. The anotations can be turned into 3D shapes of which the sphericity can be determined.

![alt text](https://github.com/Senneschal/Data_Science_Alliance/blob/master/Sphericity.png)

* This specific dataset is perticularly interesting for machine learning and computer aided diagnosis, which is something that could be explored in this project if this is an added value. Eitherway, because the diagnosis was performed by 4 radiologists independently one could look at the variance between the annotations of different radiologists and showcase the inconsistency of diagnosis between different radiologists. This problem may be much less prevalent when a computer performs this task.

<img src="https://github.com/Senneschal/Data_Science_Alliance/blob/master/annotations.png" alt="alt text" width="380" height="350">

* Adding up all the annotations could provide insight into which areas of the lungs are most likely to develope tumors and result in a sort of "probability map" wihtin a standardized lung volume

<img src="https://github.com/Senneschal/Data_Science_Alliance/blob/master/prob_map.png" alt="alt text" width="300" height="300">


* Since the scale of each scan is know one could estimate, for example, the size/BMI of the patient and find correlation with the annotated tumors. For simplcity I tried this by segmenting the lungs and using the lung volume instead.

![alt text](https://github.com/Senneschal/Data_Science_Alliance/blob/master/corr.png)

In this case a pearson correlation of -0.03 was found, which is rather insignificant.

Note: see Some_Examples.ipynb for further details on these results


# Dataset
One of these effort is a website called "The Cancer Imaging Archieve (TCIA)" https://www.cancerimagingarchive.net/
Which contains a wealth of medical imaging data in a large variety of different forms (CT, MRI, microscopic biopsy, radiographs, ...)
WE SHOULD TRY TO FIND MORE MEDICAL DATA, PERHAPS NOT IMAGING DATA.

# A list of internal milestones up until project milestone 2
Add here a sketch of your planning for the next project milestone.

# Questions for TAa
It would be nice to have another source of medical data, perhaps not imaging data, does anyone happen to have a suggestion?
