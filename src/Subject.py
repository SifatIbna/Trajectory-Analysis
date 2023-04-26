import numpy as np
from src.utils.util import calc_distance,calc_TTC

class ISubject:

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.leader, self.follower, self.TTC)

class Subject(ISubject):
    """
    The subject class that will notify its observers when a new minimum TTC is found.
    """
    def __init__(self):
        super().__init__()
        self.leader = None
        self.follower = None
        self.TTC = None

    def find_leader_follower(self, T1, T2):
        d1 = calc_distance(T1['Latitude'], T1['Longitude'], T2['Latitude'], T2['Longitude']) - 3  # Subtract vehicle length

        d2 = calc_distance(T1['Latitude'].shift(-1), T1['Longitude'].shift(-1), T2['Latitude'].shift(-1), T2['Longitude'].shift(-1)) - 3  # Subtract vehicle length

        v1 = d1.diff() / (T1['Time (s)'].diff() / 1000)  # Relative speed
        v2 = d2.diff() / (T2['Time (s)'].diff() / 1000)  # Relative speed

        TTC = calc_TTC(d1 - d2, v2 - v1)  # Minimum TTC

        idx_min_TTC = np.argmin(TTC)
        if d1.iloc[idx_min_TTC] < d2.iloc[idx_min_TTC]:
            leader = 'T1'
            follower = 'T2'
        else:
            leader = 'T2'
            follower = 'T1'
        self.leader = leader
        self.follower = follower
        self.TTC = TTC.iloc[idx_min_TTC]
        self.notify()
