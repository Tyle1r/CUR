def engineOilFunction(Tinterp):
    # Reads data listed in Table A.6 and interpolates at Tinterp which should
    # be in Kelvins.
    # engineOilFunction produces a dictionary in Python which has the properties 
    # of engine oil in SI units.

    # Load engine oil data from CSV file if not already loaded
    global engineOil_data
    if 'engineOil_data' not in globals():
        engineOil_data = pd.read_csv('engineOil.csv').values

    # Use numpy.interp to interpolate the values in the table
    data = np.interp(Tinterp, engineOil_data[:, 0], engineOil_data[:, 1:])

    # Populate dictionary with interpolated values
    engineOil = {
        'rho': data[0],                        # kg/m^3
        'cp': data[1] * 1e3,                   # conversion to J/(kg K)
        'mu': data[2] * 1e-2,                  # eliminate mu scaling in table
        'Pr': data[6],                         # Prandtl number
        'beta': data[-1] * 1e-6               # thermal expansion coefficient
    }
    engineOil['nu'] = engineOil['mu'] / engineOil['rho']          # kinematic viscosity m^2/s
    engineOil['alpha'] = engineOil['nu'] / engineOil['Pr']        # thermal diffusivity m^2/s
    engineOil['k'] = engineOil['alpha'] * engineOil['rho'] * engineOil['cp']    # thermal conductivity W/(m K)

    return engineOil