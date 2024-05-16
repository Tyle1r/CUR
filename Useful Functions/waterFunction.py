def waterFunction(Tinterp):
    # Reads data listed in Table A.6 and interpolates at Tinterp which should
    # be in Kelvins.
    # waterFunction produces a dictionary in Python which has the saturated liquid 
    # properties of water in SI units.

    # Load water data from CSV file if not already loaded
    global water_data
    if 'water_data' not in globals():
        water_data = pd.read_csv('water.csv').values

    # Use numpy.interp to interpolate the values in the table
    data = np.interp(Tinterp, water_data[:, 0], water_data[:, 1:])

    # Populate dictionary with interpolated values
    water = {
        'rho': 1000 / data[1],                 # kg/m^3
        'cp': data[4] * 1e3,                   # conversion to J/(kg K)
        'mu': data[6] * 1e-6,                  # eliminate mu scaling in table
        'Pr': data[10],                        # Prandtl number
        'beta': data[-2] * 1e-6               # thermal expansion coefficient
    }
    water['nu'] = water['mu'] / water['rho']          # kinematic viscosity m^2/s
    water['alpha'] = water['nu'] / water['Pr']        # thermal diffusivity m^2/s
    water['k'] = water['alpha'] * water['rho'] * water['cp']    # thermal conductivity W/(m K)

    return water
