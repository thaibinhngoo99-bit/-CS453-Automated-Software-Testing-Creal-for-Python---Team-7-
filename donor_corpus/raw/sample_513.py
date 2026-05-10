import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
wheat_df = pd.read_csv('/home/dipanjan/DAT210x/Module3/Datasets/wheat.data', index_col=0);


#
# TODO: Create a 2d scatter plot that graphs the
# area and perimeter features
# 
# .. your code here ..
wheat_df.plot.scatter(x='area', y='perimeter')

#
# TODO: Create a 2d scatter plot that graphs the
# groove and asymmetry features
# 
# .. your code here ..
wheat_df.plot.scatter(x='groove', y='asymmetry')

#
# TODO: Create a 2d scatter plot that graphs the
# compactness and width features
# 
# .. your code here ..
wheat_df.plot.scatter(x='compactness', y='width')


# BONUS TODO:
# After completing the above, go ahead and run your program
# Check out the results, and see what happens when you add
# in the optional display parameter marker with values of
# either '^', '.', or 'o'.
wheat_df.plot.scatter(x='compactness', y='width', marker='o')

plt.show()


