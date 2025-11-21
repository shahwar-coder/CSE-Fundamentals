'''
📘 STORY: "THE JOURNEY OF A MESSAGE"

Imagine you (the sender) want to send a message "Hi" to your friend over the internet.
Your message travels DOWN the OSI layers on your device → Across the network → UP the layers on your friend's device.

Let’s follow this journey layer-by-layer like a story.

--------------------------------------
🥇 LAYER 7 — APPLICATION
--------------------------------------
You open WhatsApp and type "Hi".
The app says: "I want to send this message!"

(Responsibility: App-level communication)

--------------------------------------
🥈 LAYER 6 — PRESENTATION
--------------------------------------
A translator appears and says:
"Let me convert this into a proper format and encrypt it so no one understands your secret message."

(Responsibility: Formatting, encryption, compression)

--------------------------------------
🥉 LAYER 5 — SESSION
--------------------------------------
A session manager knocks:
"I'll create a communication room between you and your friend.
I'll also keep it open until you're done chatting."

(Responsibility: Opening and managing sessions)

--------------------------------------
🏅 LAYER 4 — TRANSPORT
--------------------------------------
A delivery captain comes:
"I'll break your message into small packets.
I'll add port numbers so the receiver knows which app it belongs to.
If TCP: I'll ensure reliability.
If UDP: I'll focus on speed."

(Responsibility: Segmentation, TCP/UDP, ports)

--------------------------------------
🎖️ LAYER 3 — NETWORK
--------------------------------------
A navigator joins:
"I will put a destination IP address.
I will find the best route through the network,
even if it crosses continents."

(Responsibility: IP addressing + routing)

--------------------------------------
🎗️ LAYER 2 — DATA LINK
--------------------------------------
A MAC-address guard appears:
"I’ll prepare frames and attach your device’s MAC address and the receiver’s next-hop MAC address.
I’ll also check for errors."

(Responsibility: MAC address, frames, error detection)

--------------------------------------
🔘 LAYER 1 — PHYSICAL
--------------------------------------
Finally, a cable worker/wireless signal handler says:
"I’ll convert all this into electrical/light/radio signals and push them through cables or air."

(Responsibility: Bits (0s/1s), physical medium)

--------------------------------------
🏁 On your friend’s device:
The journey reverses from LAYER 1 → LAYER 7
and your friend finally sees "Hi" in WhatsApp.

------------------------------------------------
🧠 MEMORY FLOW (STORY ORDER):
App → Translator → Session Manager → Delivery Captain → Navigator → MAC Guard → Signal Worker
------------------------------------------------

'''
