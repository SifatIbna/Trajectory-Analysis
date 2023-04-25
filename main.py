import csv
from typing import List

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Trajectory(Subject):
    def __init__(self, filename: str, vehicle_length: float):
        super().__init__()
        self.filename = filename
        self.vehicle_length = vehicle_length
        self.positions = []
        self.timestamps = []
        self.load_data()

    def load_data(self):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            print(reader)
            for row in reader:
                print(row)
                lat, lon, timestamp = row
                print(lat)
                self.positions.append((float(lat), float(lon)))
                self.timestamps.append(float(timestamp))

        self.notify()

class Observer:
    def update(self, subject):
        pass

class TTCObserver(Observer):
    def __init__(self, leader: Trajectory, follower: Trajectory, vehicle_length: float):
        self.leader = leader
        self.follower = follower
        self.vehicle_length = vehicle_length

    def update(self, subject):
        if subject in [self.leader, self.follower]:
            if len(self.leader.positions) > 0 and len(self.follower.positions) > 0:
                ttc = self.calculate_ttc()
                print(f"Minimum TTC: {ttc:.2f}s")

    def calculate_ttc(self):
        xi = self.leader.positions[-1][0]
        xf = self.follower.positions[-1][0]
        ti = self.leader.timestamps[-1]
        tf = self.follower.timestamps[-1]
        D = self.vehicle_length
        Vf = self.calc_speed(self.follower)
        Vi = self.calc_speed(self.leader)

        if Vf <= Vi:
            return float('inf')
        else:
            ttc = (xi - xf - D) / (Vf - Vi)
            return ttc

    def calc_speed(self, traj):
        if len(traj.positions) < 2:
            return 0

        dx = traj.positions[-1][0] - traj.positions[-2][0]
        dy = traj.positions[-1][1] - traj.positions[-2][1]
        dt = traj.timestamps[-1] - traj.timestamps[-2]
        dist = self.calc_distance(dx, dy)
        speed = dist / dt
        return speed

    def calc_distance(self, dx, dy):
        return (dx**2 + dy**2)**0.5

class LeaderFollowerObserver(Observer):
    def __init__(self, leader: Trajectory, follower: Trajectory):
        self.leader = leader
        self.follower = follower

    def update(self, subject):
        if subject in [self.leader, self.follower]:
            if len(self.leader.positions) > 0 and len(self.follower.positions) > 0:
                leader, follower = self.leader_follower()
                print(f"Leader: {leader}, Follower: {follower}")

    def leader_follower(self):
        if self.leader.positions[-1][0] > self.follower.positions[-1][0]:
            return self.leader, self.follower
        else:
            return self.follower, self.leader

if __name__ == "__main__":
    t1 = Trajectory('data/T1.csv', 3)
    t2 = Trajectory('data/T2.csv', 3)
    t2_2 = Trajectory('data/T2_2.csv', 3)
    t3 = Trajectory('data/T3.csv', 3)
    t4 = Trajectory('data/T4.csv', 3)

    ttc_obs_1 = TTCObserver(t1, t2, 3)
    ttc_obs_2 = TTCObserver(t1, t2_2, 3)
    ttc_obs_3 = TTCObserver(t3, t4, 3)

    lf_obs_1 = LeaderFollowerObserver(t1, t2)
    lf_obs_2 = LeaderFollowerObserver(t1, t2_2)
    lf_obs_3 = LeaderFollowerObserver(t3, t4)

    t1.attach(ttc_obs_1)
    t1.attach(ttc_obs_2)
    t3.attach(ttc_obs_3)

    t1.attach(lf_obs_1)
    t1.attach(lf_obs_2)
    t3.attach(lf_obs_3)
