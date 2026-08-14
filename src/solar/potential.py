def annual_energy_kwh(area_m2, irradiation_kwh_m2, efficiency_percent):
    return area_m2 * irradiation_kwh_m2 * efficiency_percent / 100
