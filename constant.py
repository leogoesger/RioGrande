import scipy.interpolate as ip

# Interpolate for k value
x = [0,10,20,30,35,40,45,50];
thornthwaite_K = {
    "Jan": ip.UnivariateSpline(x, [1.04, 1.00, 0.95, 0.90, 0.87, 0.84, 0.80, 0.74], k=3, s=3),
    "Fed": ip.UnivariateSpline(x, [0.94, 0.91, 0.90, 0.87, 0.85, 0.83, 0.81, 0.78], k=3, s=3),
    "Mar": ip.UnivariateSpline(x, [1.04, 1.03, 1.03, 1.03, 1.03, 1.03, 1.02, 1.02], k=3, s=3),
    "Apr": ip.UnivariateSpline(x, [1.01, 1.03, 1.05, 1.08, 1.09, 1.11, 1.13, 1.15], k=3, s=3),
    "May": ip.UnivariateSpline(x, [1.04, 1.08, 1.13, 1.18, 1.21, 1.24, 1.28, 1.33], k=3, s=3),
    "Jun": ip.UnivariateSpline(x, [1.01, 1.06, 1.11, 1.17, 1.21, 1.25, 1.29, 1.36], k=3, s=3),
    "Jul": ip.UnivariateSpline(x, [1.04, 1.08, 1.14, 1.20, 1.23, 1.27, 1.31, 1.37], k=3, s=3),
    "Aug": ip.UnivariateSpline(x, [1.04, 1.07, 1.11, 1.14, 1.16, 1.18, 1.21, 1.25], k=3, s=3),
    "Sep": ip.UnivariateSpline(x, [1.01, 1.02, 1.02, 1.03, 1.03, 1.04, 1.04, 1.06], k=3, s=3),
    "Oct": ip.UnivariateSpline(x, [1.04, 1.02, 1.00, 0.98, 0.97, 0.96, 0.94, 0.92], k=3, s=3),
    "Nov": ip.UnivariateSpline(x, [1.01, 0.98, 0.93, 0.89, 0.86, 0.83, 0.79, 0.76], k=3, s=3),
    "Dec": ip.UnivariateSpline(x, [1.01, 0.99, 0.91, 0.88, 0.85, 0.81, 0.75, 0.70], k=3, s=3),
}


number_to_month = {
    0:"Jan",
    1:"Fed",
    2:"Mar",
    3:"Apr",
    4:"May",
    5:"Jun",
    6:"Jul",
    7:"Aug",
    8:"Sep",
    9:"Oct",
    10:"Nov",
    11:"Dec",
}
