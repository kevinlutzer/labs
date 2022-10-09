%
% Simulate noise from a sampled sine wave with a linear amplitude function
% a(t)
%

% discrete params
fs = 1000;
steps = 2 ^ bits;

% real time params
f = 10;
v = (3.3 * t)

t = 0:1/fs:1-1/fs;
out = v*(sin(2*pi*f*t));

x = append(x, out);

%xdft = fft(x);
plot(x);