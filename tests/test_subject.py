import pandas as pd
import numpy as np
from src.utils.util import calc_distance, calc_TTC
from src.Subject import Subject

def test_find_leader_follower():
    # Test case 1
    T1 = pd.DataFrame({'Time (s)': [0, 1, 2, 3], 'Latitude': [0, 0, 0, 0], 'Longitude': [0, 0, 0, 0]})
    T2 = pd.DataFrame({'Time (s)': [0, 1, 2, 3], 'Latitude': [-27.93454934, -27.93455036, -27.93455155, -27.93455288], 'Longitude': [153.3911746, 153.391181, 153.3911883, 153.3911963]})
    subject = Subject()
    subject.find_leader_follower(T1, T2)
    assert subject.leader == 'T1'
    assert subject.follower == 'T2'

def test_notify():
    class Observer:
        def __init__(self):
            self.leader = None
            self.follower = None
            self.TTC = None

        def update(self, leader, follower, TTC):
            self.leader = leader
            self.follower = follower
            self.TTC = TTC

    T1 = pd.DataFrame({'Time (s)': [0, 1, 2, 3], 'Latitude': [0, 0, 0, 0], 'Longitude': [0, 0, 0, 0]})
    T2 = pd.DataFrame({'Time (s)': [0, 1, 2, 3], 'Latitude': [-27.93454934, -27.93455036, -27.93455155, -27.93455288], 'Longitude': [153.3911746, 153.391181, 153.3911883, 153.3911963]})

    subject = Subject()
    observer = Observer()
    subject.attach(observer)
    subject.find_leader_follower(T1, T2)
    assert observer.leader == 'T1'
    assert observer.follower == 'T2'
    assert observer.TTC is not None
