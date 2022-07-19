#library
import seaborn as sns
from sklearn.metrics import confusion_matrix

def confusion_matrix_custom(y_true,y_pred):

    #Create a usual confusion matrix
    cf_matrix = confusion_matrix(y_true, y_pred)

    #Plotting
    sns.heatmap(cf_matrix, annot=True, fmt='', cmap='Blues')
