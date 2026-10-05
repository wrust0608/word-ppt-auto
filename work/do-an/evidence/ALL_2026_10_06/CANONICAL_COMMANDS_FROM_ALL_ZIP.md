# Canonical Commands Extracted from ALL(1).zip

These commands are copied from machine-generated raw `.nmap` headers or final run manifests. They are evidence facts, not report headings.

## Scenario 1

```bash
nmap -sn -PR -T3 --max-retries 2 -oA b2_host_discovery 192.168.56.0/24
nmap -sn -PR -T3 --max-retries 2 -oA b3_target_alive 192.168.56.20
nmap -sS -p 139,445 -T3 --max-retries 2 --reason -oA b4_smb_ports 192.168.56.20
nmap -sS -sV --version-intensity 5 -p 139,445 -T3 --max-retries 2 -oA b5_smb_version 192.168.56.20
nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities -T3 --max-retries 2 -oA b6_smb_nse 192.168.56.20
```

## Scenario 2

```bash
nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20
nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20
nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb2-security-mode -oA evidence/nse-smb/NSE-SMB-03_signing 192.168.56.20
nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20
```

## Case B

```powershell
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
```

```bash
nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20
nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20
```

## Case C

```bash
sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20
nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20
```
