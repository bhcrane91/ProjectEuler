import numpy as np

#                  Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
months = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
yb = 1900
ye = 2000
months = np.reshape(np.tile(months, ye-yb), (ye-yb,np.size(months)))
