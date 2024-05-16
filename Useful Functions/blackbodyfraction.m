function [f] = blackbodyfraction(Tlambda)

% This function calculates int(E_lam,bb/(E_bb),0,lamT)
% The argument should be lambda*T in micrometers Kelvin
% The function returns the fraction given in Table 12.2
% in the book

syms lamT
C1 = 3.742e8;   % W mum^4/m^2
C2 = 1.439e4;    % mu m K
sigma = 5.67e-8; % Stefan Boltzmann [W/(m^2 K^4)]\

% Equation 12.34
f = double(int(C1/(sigma*lamT^5*(exp(C2/lamT)-1)),0,Tlambda));

end