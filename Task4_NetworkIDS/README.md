# Network Intrusion Detection System (NIDS)

## Objective

Set up and configure Suricata as a Network Intrusion Detection System (NIDS) to monitor network traffic and detect ICMP traffic using a custom detection rule.

## Tools Used

- Kali Linux
- Suricata 8.0.6
- Custom Suricata Rule
- ICMP / Ping

## Network Configuration

- Network: 192.168.1.0/24
- Network Interface: wlan0
- Local IP Address: 192.168.1.8

## Implementation

Suricata was configured using the `suricata.yaml` configuration file and a custom rule to detect ICMP traffic.

Suricata was then started on the `wlan0` interface to monitor live network traffic.

## Testing

ICMP traffic was generated using:

```bash
ping -c 4 192.168.1.1
```
**Suricata successfully detected the ICMP traffic and generated the alert:**

```text
LAB - ICMP Traffic Detected
```

The alert was recorded in both:

- `fast.log`
- `eve.json`

## Result

Successfully configured and tested Suricata as a Network Intrusion Detection System. The custom rule detected the generated ICMP traffic and produced the expected security alert.

## Conclusion

This task demonstrated how Suricata can be used to monitor network traffic and detect specific network activity using custom detection rules.



