#ECDF - Empirical cumulative distribution function(notes)

#An empirical cumulative distribution function is called the Empirical Distribution Function, or EDF for short. It is also referred to as the Empirical Cumulative Distribution 
#Function, or ECDF.The EDF is calculated by ordering all of the unique observations in the data sample and calculating the cumulative probability for each as the number of 
#observations less than or equal to a given observation divided by the total number of observations.

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y
