# Applying data analysis on medical data to help improve society's quality of life

https://senneschal.github.io/DataStory/

# Research questions

**Globalized view of medical data:**

<p align="center">
<img src="https://github.com/Senneschal/Data_Science_Alliance/blob/master/Images/scheme.png" alt="alt text" width="700" height="910"></p>

# Dataset

### Ghdx health data 
* http://ghdx.healthdata.org

Wealth of global medical data.

### Cardiovascular disease
* https://www.kaggle.com/sulianova/cardiovascular-disease-dataset

### Breast cancer
* https://www.kaggle.com/hdza1991/breast-cancer-wisconsin-data-set
* https://www.kaggle.com/yuqing01/breast-cancer

(A lot of breast cancer imaging data can also be found in the TCIA)

### Imaging data
* https://www.cancerimagingarchive.net/

"The Cancer Imaging Archieve (TCIA)" contains a wealth of medical imaging data in a large variety of different forms (CT, MRI, microscopic biopsy, radiographs, ...)

### Economical data (GDP per capita) 

* https://data.worldbank.org/indicator/ny.gdp.pcap.cd


# Achievements at milestone 2
An overview of all the work that has been done at this point can be found in the notebook **Milestone2.ipynb**. Unfortunately, the interactive plots and maps cannot be rendered without the notebook showing. The maps are, however, visible in the HTML file DataExploration.html.

In part 4, countries have been grouped together by hierarchial clustering. Unfortunately, the plots of these groupings do not show, for unknown reasons. This issue will be solved as soon as possible. 

In part 5, the data notebook could not be compiled due to technichal issues. The solution to these issues is known, but it cannot be done in time for deadline. (fixed now)


# All achievements at milestone 3

For each contributer in approximately chronological order

### Nathan Sennesael:
* Medical imageing analysis (discarded)
* Cardiovascular disease analysis
* Data explorations and Initial world maps for impact of diseases
* Skeleton code and layout of DataStory + writing

### Ruben Janssens
* Further analysis on impact of disease
* Measures for the effects of diseases
* Further analysis on risk factor analysis
* Cleaning up and writing notebook and DataStory

### Joakim Kattelus
* Clustering algorithm
* Correlations between countries
* ML model on risk factors
* Writting on DataStory


### Aurelien Gabriel Debbas
* Economic analysis
* Making beautiful visualizations with plotly
* Interactive plots that can be imbedded in the datastory
* Writing on DataStory




# A list of internal milestones up until project milestone 3
For the different research questions, the following things will be done:

## 1. Which diseases have the most significant negative impact on society's quality of life as of today? How does differ between countries and over time?
* Compare the different measures and choose which ones will be used for future analyses.
* Extend the analyses of all measures to look at the evolution over time (this was not yet done for the YLL).
* Decide on a set of disease categories to analyse. Thoroughly check this dataset to make sure any more needed cleaning and wrangling is done.
* Fix the visualisation so that all countries are correctly visualised. Add a slider to more easily see the evolution over time.

Then, more substantive analyses can be made:
* Which diseases have the largest impact on the different countries? Look at a top 1,2,3...? This information can then be used to steer the analysis for the next research questions.

## 2. How is the prevalence of different diseases linked to different risk factors?
* Use the data from question 1 to analyse specific risk factors and the phenomena observed in that question.
* Perform analyses like this one for cardiovascular diseases for other diseases.
* Try to link the risk factors identified here with health data about different countries.

## 3. How is this linked to the living conditions within each country?
* Perform statistical analyses on this data (e.g. look for a correlation).
* Look for other data on the living conditions of a country (e.g. HDI, Gini inequality index, government health budget)
* Try to cluster countries which exhibit similar characteristics.

## 4. Is the prevalence of diseases in a country correlated with that of other countries? What can this tell us about the spread of diseases?
* This analysis can be started once the measures and diseases are decided upon.
