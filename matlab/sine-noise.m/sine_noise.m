% 
% Simulate noise from a sampled sine wave
%
x = [];
for bits = [4, 8, 10, 12]
    % discrete params
    fs = 1000;
    steps = 2 ^ bits;
    
    % real time params
    f = 10;
    v = 3.3;
    
    t = 0:1/fs:1-1/fs;
    out = v*(round((sin(2*pi*f*t)*steps),0)/steps);

    x = append(x, out);
    
    %xdft = fft(x);
    %plot(abs(xdft))
end

plot(x[1]);
