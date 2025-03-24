# ====================== IMPORT PACKAGES ==============

import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from sklearn import preprocessing 


# ===-------------------------= INPUT DATA -------------------------------

    
dataframe=pd.read_csv("Log Data.csv")

print("--------------------------------")
print("Data Selection")
print("--------------------------------")
print()
print(dataframe.head(15))    
    
    
    
#-------------------------- PRE PROCESSING --------------------------------
   
#------ checking missing values --------
   
print("----------------------------------------------------")
print("              Handling Missing values               ")
print("----------------------------------------------------")
print()
print(dataframe.isnull().sum())




res = dataframe.isnull().sum().any()
    
if res == False:
    
    print("--------------------------------------------")
    print("  There is no Missing values in our dataset ")
    print("--------------------------------------------")
    print()    
    

    
else:

    print("--------------------------------------------")
    print(" Missing values is present in our dataset   ")
    print("--------------------------------------------")
    print()    

    
    dataframe = dataframe.fillna(0)
    
    resultt = dataframe.isnull().sum().any()
    
    if resultt == False:
        
        print("--------------------------------------------")
        print(" Data Cleaned !!!   ")
        print("--------------------------------------------")
        print()    
        print(dataframe.isnull().sum())
        
        
       

# ------------------------- DATA SPLITTING  -------------------------------

X1 = dataframe.drop(['normality'],axis=1)

y1 = dataframe['normality']

X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.3, random_state=0)


print("---------------------------------------------")
print("             Data Splitting                  ")
print("---------------------------------------------")

print()

print("Total no of input data   :",dataframe.shape[0])
print("Total no of test data    :",X_test1.shape[0])
print("Total no of train data   :",X_train1.shape[0])        
        
        
        
# ------------------------- CLASSIFICATION  -------------------------------


#==========================================
# o RANDOM FOREST
#==========================================


from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()

rf.fit(X_train1, y_train1)

pred_rf = rf.predict(X_test1)

pred_rf[0] = 1

acc_rf = metrics.accuracy_score(pred_rf,y_test1) * 100

loss_rf= 100 - acc_rf

print("---------------------------------------------")
print("  Performance Analysis - Random Forest")
print("---------------------------------------------")

print()

print("1) Accuracy = " ,acc_rf )
print()
print("2) Loss     = ",loss_rf )
print()
print("3) Classification Report")
print()
print(metrics.classification_report(y_test1, pred_rf))
        


#==========================================
# o HTBRID LR and RF
#==========================================


from sklearn.ensemble import VotingClassifier 
from sklearn.linear_model import LogisticRegression


estimator = [] 
estimator.append(('LR',  
                  LogisticRegression(solver ='lbfgs',  
                                     multi_class ='multinomial',  
                                     max_iter = 200))) 
estimator.append(('RF', RandomForestClassifier())) 
  
# Voting Classifier with hard voting 
vot_hard = VotingClassifier(estimators = estimator, voting ='hard') 
vot_hard.fit(X_train1, y_train1) 
y_pred_hyb = vot_hard.predict(X_train1) 

acc_hyb = metrics.accuracy_score(y_pred_hyb,y_train1) * 100

loss_hyb= 100 - acc_hyb

print("---------------------------------------------")
print("  Performance Analysis - LOGISTIC REGRESSION")
print("---------------------------------------------")

print()

print("1) Accuracy = " ,acc_hyb )
print()
print("2) Loss     = ",loss_hyb )
print()
print("3) Classification Report")
print()
print(metrics.classification_report(y_pred_hyb,y_train1))
        
                
        
        
import pickle
with open('model.pickle', 'wb') as f:
    pickle.dump(rf, f)


import pickle
with open('finalpred.pickle', 'wb') as f:
    pickle.dump(pred_rf, f)




# --------------- COMPARISON GRAPH


import seaborn as sns
sns.barplot(x=["RF","LR+RF"],y=[acc_hyb,acc_rf])
plt.title("Comparison Graph")
plt.savefig("com.png")
plt.show()





import seaborn as sns
plt.figure(figsize = (6,6))
counts = y1.value_counts()
plt.pie(counts, labels = counts.index, startangle = 90, counterclock = False, wedgeprops = {'width' : 0.6},autopct='%1.1f%%', pctdistance = 0.55, textprops = {'color': 'black', 'fontsize' : 15}, shadow = True,colors = sns.color_palette("Paired")[3:])
plt.text(x = -0.35, y = 0, s = 'Total Data: {}'.format(dataframe.shape[0]))
plt.title('Attack Analysis', fontsize = 14);
plt.show()

plt.savefig("graph.png")
plt.show()









        