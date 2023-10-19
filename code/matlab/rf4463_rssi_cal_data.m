% For the si446x chip the rssi can be caluated using:
% rssi_computed = (rssi_reg_value)/2 - rssi_cal


% Test data from Nice RF for the rf446x series of modules this is for
% all of the frequencies they support.
rssi_computed = [-120, -110, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0];
rssi_reg_value = [28, 44, 65, 86, 106, 126, 146, 166, 186, 208, 229, 247, 250];

hold on; % Set hold on so the next plot does not blow away the one we just drew.

% Plot
figure(1);
plot(rssi_reg_value, rssi_computed, 'o');
point_count = 1000; % how many points in the best fit line data

coefficients = polyfit(rssi_reg_value, rssi_computed, 1);
rssi_reg_value_fit = linspace(min(rssi_reg_value), max(rssi_reg_value), point_count);

rssi_computed_fit = polyval(coefficients , rssi_reg_value_fit);
plot(rssi_reg_value_fit, rssi_computed_fit, 'r-', 'LineWidth', 2); % Plot fitted line.
grid on;

slope_fit = (rssi_computed_fit(end) - rssi_computed_fit(1)) / (rssi_reg_value_fit(end) - rssi_reg_value_fit(1));
rssi_cal = - rssi_computed_fit(point_count/2) + rssi_reg_value_fit(point_count/2) * slope_fit;

