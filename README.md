# Simple QoS Priority Controller using POX and Mininet  
Computer Networks Project

## Problem Statement
This project implements a simple SDN-based QoS Priority Controller using POX and Mininet to demonstrate controller-switch interaction, flow rule handling, and network behavior observation.

## Objective
To prioritize selected traffic flows using SDN rules and analyze network latency, throughput, and flow table behavior.

## Tools Used
- Ubuntu VM
- Mininet
- POX Controller
- Open vSwitch
- ping
- iperf

## Topology Used
Single switch topology with 3 hosts:
- h1
- h2
- h3

## Setup and Execution Steps

### 
Step 1: Start POX Controller
python3 pox.py forwarding.qos_controller

Step 2: Start Mininet Topology
sudo mn --topo single,3 --controller remote

Step 3: Connectivity Test
pingall

Step 4: Latency Test
h1 ping -c 5 h2
h1 ping -c 5 h3

Step 5: Flow Table Verification
sudo ovs-ofctl dump-flows s1

Step 6: Throughput Test
h2 iperf -s &
h1 iperf -c 10.0.0.2

###Controller Logic

The custom POX controller handles PacketIn events and installs flow rules based on source and destination MAC addresses. The controller applies simple QoS-related forwarding logic and enables controller-switch interaction using OpenFlow.

Screenshots
1. POX Controller Startup
<img width="1011" height="735" alt="image" src="https://github.com/user-attachments/assets/7d91ffd4-c230-47bb-aa4e-19f5b3036321" />

2. Mininet Topology Startup
<img width="856" height="729" alt="Pasted image" src="https://github.com/user-attachments/assets/222cf07e-1330-443d-bc48-1ec2a869d85f" />

3. Connectivity Test - pingall
<img width="875" height="533" alt="Pasted image (2)" src="https://github.com/user-attachments/assets/ad84fae0-1fe9-4fd0-a75f-4915acaf9f5a" />

4. Latency Test - h1 to h2
<img width="875" height="533" alt="Pasted image (3)" src="https://github.com/user-attachments/assets/dc4647e8-9c8a-4c5d-a718-dbd7bc475964" />

5. Latency Test - h1 to h3
<img width="875" height="533" alt="Pasted image (4)" src="https://github.com/user-attachments/assets/e6711788-92fa-4cf3-a41b-591ef5f2ba9b" />

6. Flow Table Verification
<img width="1199" height="405" alt="Pasted image (5)" src="https://github.com/user-attachments/assets/d8bdd6a4-913a-44e5-a4dc-d5a43106c919" />

7. Throughput Test - iperf
<img width="827" height="731" alt="Pasted image (7)" src="https://github.com/user-attachments/assets/7484d94c-4a33-41f1-9763-87cdb5b4d553" />

The custom controller code used for this project is available in:

qos_controller.py
Conclusion

This project successfully demonstrated controller-switch interaction, flow rule handling, network behavior observation, and basic performance analysis using POX and Mininet in an SDN environment.
