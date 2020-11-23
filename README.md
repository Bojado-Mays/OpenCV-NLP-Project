[![Header](https://github.com/Bojado-Mays/OpenCV-NLP-Project/blob/main/images/OpenCV-3.png)](https://docs.google.com/presentation/d/1vh6ZvfivoNm11TFUI4vqfKOedULE1-DPEDNCz6mNWnY/edit#slide=id.gacc0181b49_1_635)

## About the Project
For this project we will be scraping data from GitHub repository README files. We chose to scrape data over OpenCV (Open Source Computer Vision Library) repos across Github.  

## Goals
Our goal is to build a model that can predict what programming language a repository is, given the text of the README file.


## Deliverables
- A well-documented Jupyter Notebook that contains your analysis.
- One or two google slides suitable for a general audience that summarize your findings. Include a well-labelled visualization in your slides.


## Data Dictionary
| Feature | Definition |
|---------------------------|--------------------------------------------------|
| OpenCV            | (Open Source Computer Vision Library) is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez (which was later acquired by Intel).|  
| NLP               | (Natural Language Processing) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. |  
| Repo              | A directory or storage space for your projects. Code, text, or image files are stored. |  
| Language          | Refers to programming languages are used in computer programming to implement algorithms. |
| Readme Contents   | A README file contains information about other files in a directory or archive of computer software, it is usually a simple plain text file. |
| Term Frequency (TF)   | How often a word appears in a document. |  
| Inverse Documnet Frequency (IDF)   | A measure based on how many documents a word will appear in. |  
| (TF-IDF)   | A combination of the two measures above. |  


## Project Steps
### Acquire
- Data is aquired from 250 different (most starred) repos over the topic of OpenCV.
- Write the python code necessary to extract the text of the README file for each repo. 
- The functions are stored in the acquire.py file.
- Create a data.json file with a dictionary of all the repos.
- File is a reproducible component for gathering the data.

### Prepare
- Create a prepare.py file. 
- Build the dataset.
- Missing values are investigated and handled.
- Run train, validate, and test.
- File is a reproducible component that is ready for exploration.

### Explore
- Explore scraped data.
- Find patterns by creating wordclouds and histograms.
- Summarize takeaways and conclusions.   

### Model
- Fit different models and using different representations of the text (e.g. simple bag of words, TF-IDF values).
- Build a function that will take in the text of a README file and predict the programming language of repo.

### Conclusions
- Even though OpenCV is primarly written in C++, most words repos are written in Python.  

- Repo Languages (out of 250 total most starred repos explored):  
    - Python 40.4% ; 101 repos
    - C++ 31.6%, 79 repos
    - Java 6.4%, 16 repos
    
- We choose to only explore Python and C++ repos because there are the most significant.
- Combined total of 180 repos explored (Python and C++).
- Most common words for Python and C++ combined are  &#9 ; , image, and opencv.
- The symbols &#9 ;, appear to be a tab character of some sort from html related to ascii.
- Best model was Combined Terms Model that maintained an 83% accuracy on the entire dataset.

### Future Investigations
- Are similar patterns seen across other computer vision software repos, such as (Matlab, TensorFlow, and SimpleCV)?
- We could gather a higher quantity of repo data for more accurate results. 
- Futher modeling could be conducted.

## How to Reproduce
All files are reproducible and available for download and use.
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, data.json, and Final_Report.ipynb files

## Contact Us 
Dani Bojado
- daniella.bojado@gmail.com 

Matthew Mays
- matthew.c.mays96@gmail.com
