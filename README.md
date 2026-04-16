# Simple QoS Priority Controller using Mininet
Computer Networks Project
## Objective
To simulate QoS in an SDN environment and analyze traffic behavior.

## Tools Used
- Ubuntu VM
- Mininet
- Open vSwitch
- ping
- iperf

## Topology Setup
Used a single-switch topology with 3 hosts.
<img width="687" height="623" alt="Pasted image (5)" src="https://github.com/user-attachments/assets/93e1ae7c-9fa7-43f9-8306-2bf7d842c13e" />

## Connectivity Test
Verified host connectivity using pingall.
<img width="581" height="389" alt="Screenshot From 2026-04-16 12-20-51" src="https://github.com/user-attachments/assets/535a852a-9f55-4ed9-9094-ff8f6662b274" />

## Latency Test

### h1 to h2
<img width="581" height="389" alt="Screenshot From 2026-04-16 12-21-33" src="https://github.com/user-attachments/assets/acae8985-0a52-441a-b97b-15cedb706f19" />

### h1 to h3
<img width="687" height="296" alt="Pasted image (5)" src="https://github.com/user-attachments/assets/b16854ac-c39a-4f2c-9d87-fc258fd14b1a" />

## Throughput Test

### h1 to h2 iperf
<img width="581" height="389" alt="Pasted image" src="https://github.com/user-attachments/assets/d1191ddc-2c61-4bbe-ab53-1044a55e3d25" />

### h1 to h3 iperf
<img width="581" height="389" alt="Pasted image (2)" src="https://github.com/user-attachments/assets/9f7cdd51-b072-4d0c-9b9f-596ab0fdf164" />

## Flow Table Verification
Observed flow entries in OVS switch.
<img width="911" height="427" alt="Pasted image (3)" src="https://github.com/user-attachments/assets/adcb8074-a4d9-4242-8313-b4e1cb5914e7" />

## Conclusion
Successfully demonstrated simple QoS traffic behavior using Mininet.
