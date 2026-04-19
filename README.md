# Simple QoS Priority Controller using POX and Mininet  
Computer Networks Project

## Problem Statement
The goal of this project is to implement a simple Software Defined Networking (SDN) based QoS Priority Controller using POX and Mininet. The system demonstrates controller-switch interaction, flow rule installation, and traffic behavior analysis.
The controller applies rule-based forwarding for different traffic flows. While strict priority queuing is not enforced, the implementation demonstrates SDN-based flow control and traffic handling.

## Objective
- To simulate QoS behavior in an SDN environment
- To observe controller-based packet handling
- To analyze latency, throughput, and flow table behavior.

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

- The controller listens for PacketIn events
- It extracts source and destination MAC addresses
- Installs flow rules using OpenFlow
- Implements simple QoS-based forwarding logic
- Demonstrates controller-based traffic handling.

###Expected Output

- Controller successfully connects to switch
- Hosts communicate through Mininet topology
- Flow rules are installed in Open vSwitch
- Latency observed using ping
- Throughput measured using iperf

###Screenshots

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
<img width="1203" height="402" alt="Screenshot From 2026-04-19 10-37-43" src="https://github.com/user-attachments/assets/d4335487-088f-40ac-860f-8b34d29c1bea" />

7. Throughput Test - iperf
<img width="877" height="725" alt="Screenshot From 2026-04-19 10-48-15" src="https://github.com/user-attachments/assets/86eeb1b4-ccd6-4a26-b08d-798faa355f8b" />
   
###Results

- Successful controller-switch interaction observed
- Flow rules installed and verified in switch
- Network latency measured between hosts
- Throughput analyzed using iperf
- Demonstrated SDN-based traffic handling

###Conclusion

This project successfully demonstrates the implementation of a simple QoS Priority Controller using POX and Mininet. The system validates controller-based flow handling, network behavior, and performance metrics in an SDN environment.

Source Code

The controller implementation is provided in:
qos_controller.py
