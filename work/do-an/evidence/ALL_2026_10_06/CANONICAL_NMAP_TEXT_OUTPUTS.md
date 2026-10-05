# Canonical Nmap Text Outputs — ALL(1).zip

Source archive SHA-256:
`dc63f3ba5ed514f0c6b5e947474baca712c15a4c08c42b2228e421512cb04ff3`

This file copies the canonical human-readable `.nmap` outputs needed for report analysis. XML/GNMAP siblings remain bound by SHA-256 in the evidence package provenance.

## Scenario 1 — b2_host_discovery.nmap

```text
# Nmap 7.99 scan initiated Sat Oct  3 21:47:30 2026 as: /usr/lib/nmap/nmap -sn -PR -T3 --max-retries 2 -oA b2_host_discovery 192.168.56.0/24
Nmap scan report for 192.168.56.1
Host is up (0.00040s latency).
MAC Address: 0A:00:27:00:00:13 (Unknown)
Nmap scan report for 192.168.56.20
Host is up (0.00021s latency).
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.56.100
Host is up (0.00026s latency).
MAC Address: 08:00:27:13:44:71 (Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.56.10
Host is up.
# Nmap done at Sat Oct  3 21:47:32 2026 -- 256 IP addresses (4 hosts up) scanned in 1.91 seconds
```

## Scenario 1 — b3_target_alive.nmap

```text
# Nmap 7.99 scan initiated Sat Oct  3 21:48:55 2026 as: /usr/lib/nmap/nmap -sn -PR -T3 --max-retries 2 -oA b3_target_alive 192.168.56.20
Nmap scan report for 192.168.56.20
Host is up (0.00034s latency).
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)
# Nmap done at Sat Oct  3 21:48:55 2026 -- 1 IP address (1 host up) scanned in 0.12 seconds
```

## Scenario 1 — b4_smb_ports.nmap

```text
# Nmap 7.99 scan initiated Sat Oct  3 21:49:52 2026 as: /usr/lib/nmap/nmap -sS -p 139,445 -T3 --max-retries 2 --reason -oA b4_smb_ports 192.168.56.20
Nmap scan report for 192.168.56.20
Host is up, received arp-response (0.00035s latency).

PORT    STATE SERVICE      REASON
139/tcp open  netbios-ssn  syn-ack ttl 128
445/tcp open  microsoft-ds syn-ack ttl 128
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)

# Nmap done at Sat Oct  3 21:49:54 2026 -- 1 IP address (1 host up) scanned in 1.30 seconds
```

## Scenario 1 — b5_smb_version.nmap

```text
# Nmap 7.99 scan initiated Sat Oct  3 21:50:57 2026 as: /usr/lib/nmap/nmap -sS -sV --version-intensity 5 -p 139,445 -T3 --max-retries 2 -oA b5_smb_version 192.168.56.20
Nmap scan report for 192.168.56.20
Host is up (0.00030s latency).

PORT    STATE SERVICE      VERSION
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Oct  3 21:51:04 2026 -- 1 IP address (1 host up) scanned in 7.67 seconds
```

## Scenario 1 — b6_smb_nse.nmap

```text
# Nmap 7.99 scan initiated Sat Oct  3 21:52:02 2026 as: /usr/lib/nmap/nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities -T3 --max-retries 2 -oA b6_smb_nse 192.168.56.20
Nmap scan report for 192.168.56.20
Host is up (0.00034s latency).

PORT    STATE SERVICE
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)

Host script results:
| smb-protocols:
|   dialects:
|     NT LM 0.12 (SMBv1) [dangerous, but default]
|     2.0.2
|     2.1
|     3.0
|_    3.0.2
| smb2-capabilities:
|   2.0.2:
|     Distributed File System
|   2.1:
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.0:
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.0.2:
|     Distributed File System
|     Leasing
|_    Multi-credit operations
| smb2-security-mode:
|   3.0.2:
|_    Message signing enabled but not required

# Nmap done at Sat Oct  3 21:52:15 2026 -- 1 IP address (1 host up) scanned in 12.45 seconds
```

## Scenario 2 — NSE-SMB-01_ports.nmap

```text
# Nmap 7.99 scan initiated Sat Oct  3 22:07:14 2026 as: /usr/lib/nmap/nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20
Nmap scan report for 192.168.56.20
Host is up, received arp-response (0.00052s latency).

PORT    STATE SERVICE      REASON
139/tcp open  netbios-ssn  syn-ack ttl 128
445/tcp open  microsoft-ds syn-ack ttl 128
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)

# Nmap done at Sat Oct  3 22:07:15 2026 -- 1 IP address (1 host up) scanned in 1.33 seconds
```

## Scenario 2 — NSE-SMB-02_protocols.nmap

```text
# Nmap 7.99 scan initiated Sat Oct  3 22:08:14 2026 as: /usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20
Nmap scan report for 192.168.56.20
Host is up (0.00053s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)

Host script results:
| smb-protocols:
|   dialects:
|     NT LM 0.12 (SMBv1) [dangerous, but default]
|     2.0.2
|     2.1
|     3.0
|_    3.0.2

# Nmap done at Sat Oct  3 22:08:19 2026 -- 1 IP address (1 host up) scanned in 5.39 seconds
```

## Scenario 2 — NSE-SMB-03_signing.nmap

```text
# Nmap 7.99 scan initiated Sat Oct  3 22:09:15 2026 as: /usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb2-security-mode -oA evidence/nse-smb/NSE-SMB-03_signing 192.168.56.20
Nmap scan report for 192.168.56.20
Host is up (0.00032s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)

Host script results:
| smb2-security-mode:
|   3.0.2:
|_    Message signing enabled but not required

# Nmap done at Sat Oct  3 22:09:17 2026 -- 1 IP address (1 host up) scanned in 1.32 seconds
```

## Scenario 2 — NSE-SMB-04_ms17010.nmap

```text
# Nmap 7.99 scan initiated Sat Oct  3 22:10:40 2026 as: /usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20
Nmap scan report for 192.168.56.20
Host is up (0.00047s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)

# Nmap done at Sat Oct  3 22:10:42 2026 -- 1 IP address (1 host up) scanned in 1.35 seconds
```

## Case B — NSE-SMB-02_protocols.nmap

```text
# Nmap 7.99 scan initiated Sat Oct  3 22:29:22 2026 as: /usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20
Nmap scan report for 192.168.56.20
Host is up (0.00043s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)

Host script results:
| smb-protocols:
|   dialects:
|     2.0.2
|     2.1
|     3.0
|_    3.0.2

# Nmap done at Sat Oct  3 22:29:28 2026 -- 1 IP address (1 host up) scanned in 5.38 seconds
```

## Case B — NSE-SMB-04_ms17010.nmap

```text
# Nmap 7.99 scan initiated Sat Oct  3 22:29:54 2026 as: /usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20
Nmap scan report for 192.168.56.20
Host is up (0.00041s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)

# Nmap done at Sat Oct  3 22:29:55 2026 -- 1 IP address (1 host up) scanned in 1.34 seconds
```

## Case C — NSE-SMB-01_ports.nmap

```text
# Nmap 7.99 scan initiated Sun Oct  4 03:20:18 2026 as: /usr/lib/nmap/nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20
Nmap scan report for 192.168.56.20
Host is up, received arp-response (0.00054s latency).

PORT    STATE    SERVICE      REASON
139/tcp filtered netbios-ssn  no-response
445/tcp filtered microsoft-ds no-response
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)

# Nmap done at Sun Oct  4 03:20:19 2026 -- 1 IP address (1 host up) scanned in 1.33 seconds
```

## Case C — NSE-SMB-04_ms17010.nmap

```text
# Nmap 7.99 scan initiated Sun Oct  4 03:29:25 2026 as: /usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20
Nmap scan report for 192.168.56.20
Host is up (0.00054s latency).

PORT    STATE    SERVICE
445/tcp filtered microsoft-ds
MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)

# Nmap done at Sun Oct  4 03:29:25 2026 -- 1 IP address (1 host up) scanned in 0.51 seconds
```
