'''
Q1. What is the main responsibility of the OSI Network Layer?
Ans:
The Network Layer performs **packet routing** across networks.
It chooses the best path and handles logical addressing using IP.

• Think: "Which route should this packet take?"
'''
# Devices: Routers work here.
# Data unit: Packets



'''
Q2. Why is the Transport Layer called the “host-to-host” layer?
Ans:
Because it delivers data **end-to-end** from one device to another,
independent of the network path.

• It uses port numbers to identify applications on each host.
'''
# Example:
# Port 80 → HTTP
# Port 443 → HTTPS



'''
Q3. What does the Data Link Layer handle?
Ans:
It handles **framing**, **MAC addressing**, and **error detection** using CRC.
It ensures reliable data transfer between two directly connected nodes.

• Think: “Local delivery inside the LAN.”
'''
# Devices: Switches, NIC cards
# Data unit: Frames



'''
Q4. What is the difference between a packet and a frame?
Ans:
Packet → Layer 3 (Network layer), contains IP addresses  
Frame  → Layer 2 (Data link layer), contains MAC addresses

• Same data, different headers based on the layer.
'''
# Example:
# Packet (IP: source/dest)
# Frame  (MAC: source/dest)



'''
Q5. Why can routing only happen at the Network Layer?
Ans:
Because routing decisions use **IP addresses**, and IP exists only at Layer 3.
Routers read IP headers to choose the next hop.

• Data Link Layer cannot route because MAC addresses cannot cross networks.
'''
# Example:
# Router → decides path based on IP
# Switch → forwards inside LAN using MAC



'''
Q6. What makes the Transport Layer different from the Data Link Layer?
Ans:
Transport Layer:
• End-to-end communication (host-to-host)
• Uses port numbers
• Handles reliability, congestion control

Data Link Layer:
• Node-to-node communication (within LAN)
• Uses MAC addresses
• Handles framing + error detection
'''
# Example:
# L4: TCP ensures ordered delivery
# L2: CRC checks errors on each hop



'''
Q7. What is multiplexing, and which OSI layer does it belong to?
Ans:
Multiplexing allows many apps to share the same network using **port numbers**.
This is handled at the **Transport Layer**.

• Each port = one application endpoint.
'''
# Example:
# Browser (443), WhatsApp call (UDP random port), Spotify (port 4070)



'''
Q8. Why does error handling appear at the Data Link Layer?
Ans:
Because errors like collisions/noise occur at the local transmission level.
The Data Link Layer uses CRC checks to detect such errors before forwarding.

• It protects local LAN communication.
'''
# L4 (TCP) → handles end-to-end errors
# L2 (CRC) → handles local link errors



'''
Q1. What is the role of the Network Layer?
Ans:
The Network Layer handles packet routing and path selection.
It uses logical addressing (IP) to move packets across networks.
'''
# Example:
# Your data may route through R1 → R3 → R7 to reach a remote server.



'''
Q2. Why is "bit synchronization" NOT a Data Link Layer function?
Ans:
Because bit synchronization belongs to the Physical Layer.
Physical Layer handles timing, signals, and converting bits into electrical/light waves.
Data Link Layer instead handles framing, MAC addressing, and error detection.
'''
# Example:
# Physical Layer ensures "when" a bit starts; Data Link ensures "how" frames are built.



'''
Q3. What does the Data Link Layer actually do?
Ans:
It manages framing, MAC addressing, and error detection.
It provides reliable node-to-node communication within the same LAN.
'''
# Example:
# Switches read MAC addresses to decide where to forward frames.



'''
Q4. What is the responsibility of the Transport Layer?
Ans:
It provides end-to-end (host-to-host) process communication.
Uses port numbers and supports reliable (TCP) or fast (UDP) delivery.
'''
# Example:
# Web browser uses port 443 (HTTPS); video call uses UDP for speed.



'''
Q5. How does the Transport Layer ensure correct process communication?
Ans:
By assigning port numbers to different applications and managing reliability,
flow control, and congestion control.
'''
# Example:
# Your laptop may use ports 443 (browser), 5228 (WhatsApp), 3478 (Zoom) simultaneously.



'''
Q6. What is the function of the MAC Sublayer?
Ans:
The MAC Sublayer controls channel access on shared mediums.
It prevents collisions and coordinates transmission using CSMA/CD, CSMA/CA, or TDMA.
'''
# Example:
# WiFi uses CSMA/CA so that multiple devices don’t talk at the same time.
# Layer 2 — Data Link Layer
#    ├── LLC (Logical Link Control) sublayer
#    └── MAC (Media Access Control) sublayer   ← **MAC is here**




'''
Q7. How is the MAC Sublayer different from Network Layer?
Ans:
MAC Sublayer operates locally (within same LAN) controlling medium access.
Network Layer operates globally, choosing routes across routers using IP addresses.
'''
# Example:
# MAC = "who gets to talk on WiFi?"
# Network = "which path does the packet take across cities?"



'''
Q8. Why must we distinguish Physical, Data Link, and MAC Sublayer correctly?
Ans:
Because many exam MCQs mix their functions.
Correct mapping:
- Physical → bits, synchronization
- Data Link → framing, MAC addressing, CRC
- MAC Sublayer → medium access control
'''
# Example:
# "Collision avoidance" → MAC Sublayer (Layer 2 sublayer), not Network or Physical.

