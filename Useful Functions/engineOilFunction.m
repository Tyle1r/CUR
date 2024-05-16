function engineOil = engineOilFunction(Tinterp)
% Reads data listed in Table A.6 and interpolates at Tinterp which should
% be in Kelvins. 
% waterFunction produces a MATLAB structure which has the saturated liquid 
% properties of water in SI units.
% To get the properties of a structure in MATLAB use . operater
% (water.rho, water.cp, water.mu, water.Pr, water.nu, water.alpha, water.k
% and water.beta) 

% The function should be in the current folder or MATLAB Search Path along
% with the water.csv


persistent engineOil_data;
if isempty(engineOil_data)
    [engineOil_data] = csvread('engineOil.csv');
end

% Use interp1 to interpolate the values in the table

[data] = interp1(engineOil_data(:,1),engineOil_data(:,2:end),Tinterp);
engineOil.rho = data(1);      % kg/m^3
engineOil.cp = data(2)*1e3;   % conversion to J/(kg K)
engineOil.mu = data(3)*1e-2;  % eliminate mu scaling in table
engineOil.Pr = data(7);       % Prandtl number 
engineOil.nu = engineOil.mu/engineOil.rho;        % kinematic viscosity m^2/s
engineOil.alpha = engineOil.nu/engineOil.Pr;      % thermal diffusivity m^2/s
engineOil.k = engineOil.alpha*engineOil.rho*engineOil.cp;    % thermal conductivity W/(m K)
engineOil.beta = data(end)*1e-6; % thermal expansion coefficient
end

