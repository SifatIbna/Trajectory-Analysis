## SYSTEM ARCHITECTURE

The system has a modular structure with three main components:

- Subject: A class that maintains the state of the system and notifies its observers when a new minimum time to collision (TTC) is found between two trajectories.
- Observer: A class that receives notifications from the Subject and prints out the current state of the system.
- Util: A collection of utility functions that are used to calculate distances and TTC.

Each component is defined in its own module, with the Subject and Observer classes in the src folder and the Util functions in a sub-folder src/utils.

The main.py script loads trajectory data from CSV files, creates a Subject and an Observer, attaches the observer to the subject, and then uses the subject to find the leader and follower between pairs of trajectories.

## DESIGN PATTERN

The system can be tested by running the main.py script with different trajectory data. The output should show the leader and follower for each pair of trajectories, along with the minimum TTC between them.

To ensure that the Util functions are working correctly, unit tests should be written for each function. These tests can be run using a testing framework such as pytest.

To ensure that the Subject and Observer classes are working correctly, integration tests should be written that simulate different scenarios and verify that the correct output is produced. For example, a test could simulate two trajectories that are about to collide and ensure that the Observer prints out a minimum TTC that is less than zero.
