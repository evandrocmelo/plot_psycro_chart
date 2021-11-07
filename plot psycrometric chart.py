import psychrolib
import matplotlib.pyplot as plt
import numpy as np

psychrolib.SetUnitSystem(psychrolib.SI)

pressure = 101325

t_array = np.arange(5, 45, 0.1)
rh_array = np.arange(0, 1.1, 0.1)
enthalpy_array = np.arange(0, 120000, 10000)
hr_hor_lines = np.arange(0.005, 0.03, 0.005)
twb_array = np.arange(-10, 45, 5)

f, ax = plt.subplots()

# plot constant relative humidity lines
for rh in rh_array:
    hr_array = []
    for t in t_array:
        hr = psychrolib.GetHumRatioFromRelHum(t, rh, pressure)
        hr_array.append(hr)
    ax.plot(t_array, hr_array, 'k')

for twb in twb_array:
    hr_array = []
    t_plot_array = []
    for t in t_array:
        if twb <= t:
            # print(twb, t)
            hr = psychrolib.GetHumRatioFromTWetBulb(t, twb, pressure)
            hr_array.append(hr)
            t_plot_array.append(t)
    ax.plot(t_plot_array, hr_array, 'b')


ax.set(ylim=(0, 0.025), xlim=(10, 40), ylabel=r"Humidity Ratio [$kg_{water}/kg_{dry air}$]", xlabel="Dry-bulb Temperature [°C]")
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
plt.tight_layout()
plt.show()