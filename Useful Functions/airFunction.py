def airFunction(Tinterp):
    import pandas as pd
    import numpy as np
    import scipy.interpolate
    # Reads data listed in Table A.4 and interpolates at Tinterp which should
    # be in Kelvins.
    # air produces a dictionary in Python which has all the properties of air in SI
    # units.

    # Load air data from CSV file if not already loaded
    global air_data
    if 'air_data' not in globals():
        air_data = pd.read_csv('air.csv').values
    # Ensure air_data has the correct shape (2D array)
    if air_data.ndim != 2:
        raise ValueError("air_data must be a 2D array")

    # Ensure air_data has at least two columns (temperature and at least one property)
    if air_data.shape[1] < 2:
        raise ValueError("air_data must have at least two columns")
    # Use numpy.interp to interpolate the values in the table
    interp_func = scipy.interpolate.interp1d(air_data[:, 0], air_data[:, 1:], axis=0)
    # Perform interpolation at the specified temperature
    data = interp_func(Tinterp)

    # Populate dictionary with interpolated values
    air = {
        'rho': data[0],                        # kg/m^3
        'cp': data[1] * 1e3,                   # conversion to J/(kg K)
        'mu': data[2] * 1e-7,                  # eliminate mu scaling in table
        'Pr': data[3],                         # Prandtl number
    }
    air['nu'] = air['mu'] / air['rho']          # kinematic viscosity m^2/s
    air['alpha'] = air['nu'] / air['Pr']        # thermal diffusivity m^2/s
    air['k'] = air['alpha'] * air['rho'] * air['cp']    # thermal conductivity W/(m K)

    return air