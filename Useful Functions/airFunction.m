function air = airFunction(Tinterp)
% Reads data listed in Table A.4 and interpolates at Tinterp which should
% be in Kelvins. 
% air produces a MATLAB structure which has all the properties of air in SI 
% units. To get the properties of a structure in MATLAB use . operater
% (air.rho, air.cp, air.mu, air.Pr, air.nu, air.alpha, air.k) 

% The function should be in the current folder or MATLAB Search Path along
% with the air.csv


persistent air_data;
if isempty(air_data)
    [air_data] = csvread('air.csv');
end

% Use interp1 to interpolate the values in the table

[data] = interp1(air_data(:,1),air_data(:,2:end),Tinterp);
air.rho = data(1);      % kg/m^3
air.cp = data(2)*1e3;   % conversion to J/(kg K)
air.mu = data(3)*1e-7;  % eliminate mu scaling in table
air.Pr = data(4);       % Prandtl number 
air.nu = air.mu/air.rho;        % kinematic viscosity m^2/s
air.alpha = air.nu/air.Pr;      % thermal diffusivity m^2/s
air.k = air.alpha*air.rho*air.cp;    % thermal conductivity W/(m K)
end

