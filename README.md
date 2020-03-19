 # Categorical or not 

In test2.py , regroup_category accepts two inputs data and integar i.

## Method Description

Check if datatype of variable at *i* position in *data* is categorical / bool 

If yes then its categorical.
	|-If no, check if it is datetime.
		|-If no, check if it unique_value_count / total_sample <=0.34 
			|- If yes, apply k-means using target variable to cluster the group and recategorise, use silhouette_score to decide on number of k
				|-hot encode these new labels to give new encoding
			|- if No it is not categorical
