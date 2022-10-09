%
% Simulate noise from a sampled sine wave with a linear amplitude function
% a(t)
%

% discrete params
fs = 10000;

% real time params
f = 10;


t = 0:1/fs:3-1/fs;

i = 1;
v = rand(1, length(t));
for x = t 
    if x < 1
        v(i) = 3.3*(x);
    else
        v(i) = 3.3;
    end

    i = i + 1;
end

% v = (3.3 (1 - t));
out = v.*(sin(2*pi*f*t));

xdft = fft(out);
% 
% plot(out);
plot(t, abs(xdft));
