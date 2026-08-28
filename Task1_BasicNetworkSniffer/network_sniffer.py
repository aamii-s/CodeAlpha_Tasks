from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


def packet_callback(packet):

    if IP in packet:

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport

        elif UDP in packet:
            protocol = "UDP"
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport

        elif ICMP in packet:
            protocol = "ICMP"
            source_port = "-"
            destination_port = "-"

        else:
            protocol = "Other"
            source_port = "-"
            destination_port = "-"

        print("\n" + "=" * 55)
        print("PACKET CAPTURED")
        print("=" * 55)

        print(f"Source IP       : {source_ip}")
        print(f"Destination IP  : {destination_ip}")
        print(f"Protocol        : {protocol}")
        print(f"Source Port     : {source_port}")
        print(f"Destination Port: {destination_port}")

        if Raw in packet:
            payload = packet[Raw].load

            print(f"Payload         : {payload[:50]}")


print("==========================================")
print("          BASIC NETWORK SNIFFER")
print("==========================================")
print("Starting packet capture...")
print("Press Ctrl+C to stop.")

sniff(prn=packet_callback, store=False)
