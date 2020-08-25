# import pandas and matplotlib 
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt 

# create 2D array of table given above 
data = [[ 5915630, 3217981, 181114, 'AMERICA' ], 
        [ 3167323, 2404585, 58546, 'INDIA'], 
        [ 3627217, 2778709, 115451, 'BRAZIL'], 
        [ 961493, 773095, 16448, 'RUSSIA'], 
        [ 611450, 516494, 13159, 'SOUTH AFRICA'], 
        [ 600438, 407301, 27813, 'PERU'], 
        [ 563705, 389124, 60800, 'MEXICO']] 
        

# dataframe created with 
# the above data array 
df = pd.DataFrame(data, columns = [ 'TOTAL CASE', 
                                    'RECOVERED',
                                    'DEATH', 'COUNTRY'] ) 

# create histogram for numeric data 
df.hist() 

# show plot 
plt.show() 

sns.countplot(wine_reviews['points'])
