import pandas as pd

from src.Subject import Subject
from src.Observer import Observer

# Load trajectory data
T1 = pd.read_csv('data/T1.csv')
T2 = pd.read_csv('data/T2.csv')
T2_2 = pd.read_csv('data/T2_2.csv')
T3 = pd.read_csv('data/T3.csv')
T4 = pd.read_csv('data/T4.csv')

# Create the subject and observers
subject = Subject()
observer1 = Observer()

# Attach the observers to the subject
subject.attach(observer1)

# Find the leader and follower between T1 and T2
subject.find_leader_follower(T1, T2)

# Find the leader and follower between T1 and T2_2
subject.find_leader_follower(T1, T2_2)

# Find the leader and follower between T3 and T4
subject.find_leader_follower(T3, T4)
