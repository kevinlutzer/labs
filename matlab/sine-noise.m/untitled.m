% 
% Simulate noise and sinewave 
%
%

t = 0:0.01:1-0.01;
x = sin(2*pi*10*t);
xdft = fft(x);
plot(abs(xdft))

