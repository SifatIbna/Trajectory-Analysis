class IObserver:
    def update(self, leader, follower, TTC):
        pass

class Observer(IObserver):
    def update(self, leader, follower, TTC):
        print(f'Leader: {leader}, Follower: {follower}, Minimum TTC: {TTC:.2f} seconds')