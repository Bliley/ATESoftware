AGING

This operation involves a system with 8 available racks. Each rack accommodates 32 positions for testing 
crystal oscillators. This system is governed by a LabVIEW program specifically designed to identify the system, rack, 
and position for testing. The objective is to assess the aging characteristics of the crystal oscillators over a period 
of several days.

---------------------------------------------------------------------------------------------------------------------------------

Functional Test

As part of the code's functional test, a rack is selected for evaluation by the user, focusing on the 
assessment of all active positions within that rack. The purpose of this step is to verify if the frequency 
is being correctly captured before proceeding with the comprehensive testing.

All the positions within the chosen rack are checked for "active" status. This ensures that only the functional 
and operational positions are considered for frequency evaluation, excluding any inactive or faulty positions.

Subsequently, the LabVIEW code initiates a sequential testing process, where it individually connects to each active 
position within the rack. It retrieves the frequency data from each active position and the user can validate if the 
captured values align with the expected range and characteristics of the crystal oscillators under test.

---------------------------------------------------------------------------------------------------------------------------------

Aging Test

The Aging Test begins in the program when either the force readings button is pressed, or when a scheduled time occurs.
It initiates the testing process beginning at the first rack and position and checks whether it is active or not. It then 
establishes a connection with the crystal oscillator at that specific location, enabling the measurement of its frequency. 
The program records the initial frequency of the oscillator as a baseline reference.

Over the course of the following days, the the crystal oscillators are continuously monitored and the frequency is recorded.
It compares the current frequency with the initial baseline frequency, allowing it to track the extent of aging or any 
frequency drift occurring over time.

As the testing progresses, the LabVIEW program collects and stores the frequency data for each crystal oscillator 
by sending it to the necessary table in the local database. By analyzing the recorded frequency data,
aging patterns and any potential trends or anomalies across the tested crystal oscillators can be identified.
This valuable information aids in understanding the long-term performance and stability of the crystal oscillators, 
facilitating informed decisions regarding their usage and replacement if necessary.