function water = waterFunction(Tinterp)
% Reads data listed in Table A.6 and interpolates at Tinterp which should
% be in Kelvins. 
% waterFunction produces a MATLAB structure which has the saturated liquid 
% properties of water in SI units.
% To get the properties of a structure in MATLAB use . operater
% (water.rho, water.cp, water.mu, water.Pr, water.nu, water.alpha, water.k
% and water.beta) 

% The function should be in the current folder or MATLAB Search Path along
% with the water.csv


persistent water_data;
if isempty(water_data)
    [water_data] = csvread('water.csv');
end

% Use interp1 to interpolate the values in the table

[data] = interp1(water_data(:,1),water_data(:,2:end),Tinterp);
water.rho = 1000/data(2);      % kg/m^3
water.cp = data(5)*1e3;   % conversion to J/(kg K)
water.mu = data(7)*1e-6;  % eliminate mu scaling in table
water.Pr = data(11);       % Prandtl number 
water.nu = water.mu/water.rho;        % kinematic viscosity m^2/s
water.alpha = water.nu/water.Pr;      % thermal diffusivity m^2/s
water.k = water.alpha*water.rho*water.cp;    % thermal conductivity W/(m K)
water.beta = data(end-1)*1e-6; % thermal expansion coefficient
end

