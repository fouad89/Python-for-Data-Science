def failed_banks_analysis():
	'''
	This function will retrieve data for the failed banks in the US. 
	performing some analysis to find states with the highest ratio of failed banks
	vs states with the lowest ratio. 

	Analysis will be done to understand the which months witnessed the highest number of failed banks

	'''
	### imports 

	import numpy as np 
	import pandas as pd
	from pandas import Series,DataFrame,read_html
	import datetime as dt 

	###

	url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
	#read the file from url
	dframe = pd.io.html.read_html(url)

	#To obtain the table
	dframe = dframe[0] 

	#table view
	
	#view the column names
	dframe_columns = dframe.columns.values

	# to find the 5 states with highest/lowest number of failed banks
	highest_st_fail =dframe['ST'].value_counts()[:5]
	lowest_state_fail = df2['ST'].value_counts()[-5:]
	# to change the format of the 





	return 	dframe_columns, highest_st_fail, lowest_state_fail



# To print out the function output into a file 
with open('pdoutput.txt','w') as f:

	print(failed_banks_analysis(), file=f)