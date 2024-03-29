% Demo to show spline interpolation.
% Clean up / initialize
clc; 
close all; 
clear all; 
workspace; % Display workspace panel.

% Create the original knot points.
lengthX = 10;
x = 1:lengthX;
y = rand (lengthX,1);
% Plot it and show how the line has sharp bends.
plot(x, y, '-sr', 'LineWidth', 2);
set(gcf, 'Position', get(0,'Screensize')); % Maximize figure.

% Use splines to interpolate a smoother curve,
% with 10 times as many points,
% that goes exactly through the same data points.
samplingRateIncrease = 10;
newXSamplePoints = linspace(1, max(x), lengthX * samplingRateIncrease);
smoothedY = spline(x, y, newXSamplePoints);

% Plot smoothedY and show how the line is
% smooth, and has no sharp bends.
hold on; % Don't destroy the first curve we plotted.
plot(newXSamplePoints, smoothedY, '-ob');
title('Spline Interpolation Demo', 'FontSize', 20);

legend('Original Points', 'Spline Points');

slopes = [0, diff(smoothedY)];
plot(newXSamplePoints, slopes, 'k-', 'LineWidth', 3);
% Draw x axis
line(xlim, [0,0], 'Color', 'k', 'LineWidth', 2);
grid on;

legend('Original Points', 'Spline Points', 'Slope');

