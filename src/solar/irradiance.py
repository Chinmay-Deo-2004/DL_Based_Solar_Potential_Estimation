import pandas as pd
import pvlib


def annual_poa_irradiance(latitude, longitude, tilt, azimuth, year=2023):
    site = pvlib.location.Location(latitude, longitude)
    times = pd.date_range(f"{year}-01-01", f"{year + 1}-01-01", inclusive="left", freq="1h", tz=site.tz)
    position = site.get_solarposition(times)
    sky = site.get_clearsky(times)
    poa = pvlib.irradiance.get_total_irradiance(tilt, azimuth, position["apparent_zenith"], position["azimuth"], sky["dni"], sky["ghi"], sky["dhi"])
    return float(poa["poa_global"].sum() / 1000)
