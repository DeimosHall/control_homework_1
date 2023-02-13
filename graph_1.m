freq = 200;
T = 4 / freq;
t = linspace(0, 4 * T, 1000);
y = sin(200 * pi * t) + 0.3 * cos(400 * pi * t);
plot(t, y);
