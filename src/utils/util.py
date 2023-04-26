import numpy as np

# Haversine Formula
def calc_distance(lat1,lon1,lat2,lon2):
    R = 6371  # Earth radius in km
    dlat = np.deg2rad(lat2 - lat1)
    dlon = np.deg2rad(lon2 - lon1)
    a = np.sin(dlat / 2) ** 2 + np.cos(np.deg2rad(lat1)) * np.cos(np.deg2rad(lat2)) * (np.sin(dlon / 2) ** 2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    d = R * c * 1000  # Distance in meters
    return d

def calc_TTC(d,v_rel):
    TTC = -d / v_rel
    return TTC