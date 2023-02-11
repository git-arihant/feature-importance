# feature-importance

### About
Feature importance is commonly employed for identifying the top n features that significantly contribute to desired prediction. For example, to find the top 50 or 100 genes responsible for lung or kidney cancer out of 50,000 genes. Thus, this is a huge time and resource-consuming practice. None of the available feature selection methods of python libraries may work in a huge dimension dataset consisting of thousands of features. In this work, a divide and conquer technique is proposed that helps to find the important features quickly and accurately. The proposed method will work for the qualitative, quantitative, continuous, and discrete datasets. The method can return top n features as per the user's requirement. 

Research paper: https://www.mdpi.com/2227-7390/11/4/920

### Workflow
![flowchart](https://lh4.googleusercontent.com/BKyXpukeFBCJkaD_wRx7Pzy2Fa_oVROHMigNcc-SYQ2bCieD-PeRpOVjsscK-hj9JIk=w2400)

### CLI
To run the program using command line:
  1. Keep the dataset file in the same folder as model.py file
  2. Run the following command in terminal- python model.py <dataset_file_name> <top_features_to_find>
  3. A new file, top_features.txt, will be made in the same folder containing the top seelcted features.
  
### Web service
A web service is also developed using fast api
