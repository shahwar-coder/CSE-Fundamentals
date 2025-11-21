'''
Q1. What is the OSI Model?
Ans:
The OSI Model is a 7-layer framework that explains how data moves across a network.
Each layer has a specific job, from physical signals to user-level apps.

• Helps understand networking by breaking it into clear layers.
'''
# Memory Trick:
# All People Seem To Need Data Processing (7→1)



'''
Q2. What does the Application Layer (Layer 7) do?
Ans:
It provides services to end users through applications like browsers, email, WhatsApp.
It interacts directly with users.

• Think: “Where users touch the network.”
'''
# Examples:
# HTTP, HTTPS, SMTP, FTP



'''
Q3. What is the job of the Presentation Layer (Layer 6)?
Ans:
This layer converts data into formats apps understand.
It handles:
• Encryption/Decryption  
• Compression  
• Data encoding formats (JPEG, MP4, PDF)

• Think: “Make data look right + stay secure.”
'''
# Example:
# TLS/SSL encryption happens here.



'''
Q4. What does the Session Layer (Layer 5) manage?
Ans:
It creates, maintains, and ends sessions between devices.
Manages multiple ongoing connections.

• Think: “Logins, video calls, chats = sessions.”
'''
# Example:
# Keeping your Zoom call alive while another app is also connected.



'''
Q5. What is the role of the Transport Layer (Layer 4)?
Ans:
Ensures delivery of data:
• TCP → reliable, ordered  
• UDP → fast, no guarantee  
Includes segmentation, flow control, and error recovery.

• Uses port numbers to identify applications.
'''
# Example:
# Port 80 → HTTP, Port 443 → HTTPS



'''
Q6. What does the Network Layer (Layer 3) handle?
Ans:
Handles routing + logical addressing.
Uses IP addresses to move packets between networks.

• Think: “Find the best path.”
'''
# Example:
# Routers operate here using IP (IPv4/IPv6).



'''
Q7. What does the Data Link Layer (Layer 2) do?
Ans:
Deals with MAC addresses, frames, and error detection using CRC.
Ensures reliable frame transfer between devices on the same network.

• Think: “Communication inside the local network.”
'''
# Example:
# Switches and NIC (Network Interface Card) work at this layer.



'''
Q8. What is the role of the Physical Layer (Layer 1)?
Ans:
It sends raw bits (0s and 1s) across physical media like cables and radio waves.
No data meaning — only signals.

• Think: “Electric signals, light pulses, radio waves.”
'''
# Example:
# Ethernet cable, fiber optic cable, WiFi radio signal.



'''
Q9. Why are the OSI layers important in networking?
Ans:
They help:
• Troubleshoot networks layer-by-layer  
• Standardize communication  
• Build protocols cleanly  
• Understand where devices & technologies belong

• OSI = universal networking roadmap.
'''
# Example:
# WiFi problem? Check Layer 1.
# IP misconfiguration? Check Layer 3.
# App not loading? Check Layer 7.



'''
# Memory Trick:
# "All People Seem To Need Data Processing"
'''
