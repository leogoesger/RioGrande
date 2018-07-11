import scipy.interpolate as ip

# Interpolate for k value
x = [0, 10, 20, 30, 35, 40, 45, 50]
thornthwaite_K = {
    "Jan": ip.interp1d(x, [1.04, 1.00, 0.95, 0.90, 0.87, 0.84, 0.80, 0.74], kind="linear"),
    "Fed": ip.interp1d(x, [0.94, 0.91, 0.90, 0.87, 0.85, 0.83, 0.81, 0.78], kind="linear"),
    "Mar": ip.interp1d(x, [1.04, 1.03, 1.03, 1.03, 1.03, 1.03, 1.02, 1.02], kind="linear"),
    "Apr": ip.interp1d(x, [1.01, 1.03, 1.05, 1.08, 1.09, 1.11, 1.13, 1.15], kind="linear"),
    "May": ip.interp1d(x, [1.04, 1.08, 1.13, 1.18, 1.21, 1.24, 1.28, 1.33], kind="linear"),
    "Jun": ip.interp1d(x, [1.01, 1.06, 1.11, 1.17, 1.21, 1.25, 1.29, 1.36], kind="linear"),
    "Jul": ip.interp1d(x, [1.04, 1.08, 1.14, 1.20, 1.23, 1.27, 1.31, 1.37], kind="linear"),
    "Aug": ip.interp1d(x, [1.04, 1.07, 1.11, 1.14, 1.16, 1.18, 1.21, 1.25], kind="linear"),
    "Sep": ip.interp1d(x, [1.01, 1.02, 1.02, 1.03, 1.03, 1.04, 1.04, 1.06], kind="linear"),
    "Oct": ip.interp1d(x, [1.04, 1.02, 1.00, 0.98, 0.97, 0.96, 0.94, 0.92], kind="linear"),
    "Nov": ip.interp1d(x, [1.01, 0.98, 0.93, 0.89, 0.86, 0.83, 0.79, 0.76], kind="linear"),
    "Dec": ip.interp1d(x, [1.01, 0.99, 0.91, 0.88, 0.85, 0.81, 0.75, 0.70], kind="linear"),
}

number_to_month = {
    0: "Jan",
    1: "Fed",
    2: "Mar",
    3: "Apr",
    4: "May",
    5: "Jun",
    6: "Jul",
    7: "Aug",
    8: "Sep",
    9: "Oct",
    10: "Nov",
    11: "Dec",
}

suppose_consumptive_use = {
    "Delicias": 104,
    "Florido": 91,
    "Ojinaga": 116,
    "Salado": 124.8
}


latitudes = {
    "Alamo":  26.4466,
    "Escondido": 28.7055,
    "LV_SD_SR": 29.2548,
    "Pecos_Opt1": 35.8270,
    "Pecos_Opt2_1": 33.3322,
    "Pecos_Opt2_2": 33.3322,
    "Pecos_Opt2_3": 33.3322,
    "Pecos_Opt3":  32.3337,
    "Pecos_Opt4_1": 31.3249,
    "Pecos_Opt4_2": 31.3249,
    "San_Juan": 26.3254,
}
