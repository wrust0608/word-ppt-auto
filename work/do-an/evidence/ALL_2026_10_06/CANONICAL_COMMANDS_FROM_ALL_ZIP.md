# Canonical Commands — ALL(1).zip

Status: `AUDITED_R2`

This file is a convenience index. For provenance-sensitive work, use `COMMAND_LINEAGE_MATRIX.md`, which separates:
- operator-entered/manifest command;
- Nmap-recorded argv from machine-generated raw output.

## Scenario 1 — operator commands

```bash
sudo nmap -sn -PR 192.168.56.0/24 -T3 --max-retries 2 -oA b2_host_discovery
sudo nmap -sn -PR 192.168.56.20 -T3 --max-retries 2 -oA b3_target_alive
sudo nmap -sS -p 139,445 192.168.56.20 -T3 --max-retries 2 --reason -oA b4_smb_ports
sudo nmap -sS -sV --version-intensity 5 -p 139,445 192.168.56.20 -T3 --max-retries 2 -oA b5_smb_version
sudo nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities 192.168.56.20 -T3 --max-retries 2 -oA b6_smb_nse
```

B1 is local state:
```bash
ip addr show
ip route show
```

## Scenario 2 — operator commands

```bash
sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20
nmap -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20
nmap -p 445 -n -T3 --max-retries 2 --script smb2-security-mode -oA evidence/nse-smb/NSE-SMB-03_signing 192.168.56.20
nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20
```

## Case B — operator action and retests

```powershell
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
```

```bash
nmap -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20
nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20
```

## Case C — operator retests

```bash
sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20
nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20
```

## Machine-generated command rule

Raw Nmap files record normalized argv, not necessarily the literal shell command. In particular:
- shell wrapper `sudo` is not present in Nmap raw headers;
- Nmap raw headers for Scenario 2 NSE-SMB-02/03/04, Case B retests, and Case C NSE-SMB-04 contain `--privileged`.

Do not merge these two provenance forms into one “exact command”.
