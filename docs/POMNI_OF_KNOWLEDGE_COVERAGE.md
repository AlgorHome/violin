# Pomni-Of Knowledge Coverage

This index preserves the 91 categories supplied in `SECURITY ENGINEERING.txt`.
It is a coverage register, not a claim that the model already knows every fact
or has permission to run every technique. The original attachment remains
outside the repository; this file contains category names only.

## How to use the index

For each category, maintain a record with: owner, source URLs and licenses,
source publication and retrieval dates, taxonomy version, concepts, safe
lab tasks, defender-visible signals, held-out evaluation IDs, observed pass
rate, false-positive rate, and last review date. Separate the raw source,
curated lesson, synthetic lab, hidden answer, and scored agent trace.

An unfilled category is `unmapped`, not `covered`. Knowledge coverage means
the agent can explain a concept and cite a current source. Lab competence
means repeated successful performance on unseen, isolated variants with
evidence. Neither one implies permission to interact with a live target.

## Current source anchors

Check the source's current edition and license at ingestion; never assume a
document remains current because it appears in this list.

| Purpose | Primary source | Update rule |
|---|---|---|
| Work roles and task/knowledge/skill statements | [NIST NICE Framework](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/nice-framework-current-versions) | Check component releases quarterly. |
| Security outcomes and governance | [NIST CSF](https://www.nist.gov/cyberframework) | Check official revisions quarterly. |
| Observed adversary behavior, detection, Enterprise/Mobile/ICS | [MITRE ATT&CK](https://attack.mitre.org/resources/updates/) | Pin the version; inspect releases and change logs monthly. |
| Vulnerability weakness taxonomy | [MITRE CWE](https://cwe.mitre.org/) | Pin a release and review changes quarterly. |
| Attack-pattern taxonomy | [MITRE CAPEC](https://capec.mitre.org/) | Pin a release and review changes quarterly. |
| Known exploitation in the wild | [CISA KEV data](https://github.com/cisagov/kev-data) | Check updates daily; do not infer exposure from a CVE alone. |
| CVE metadata and product applicability | [NVD API](https://nvd.nist.gov/developers) and vendor advisories | Check changes daily; confirm with vendor source. |
| Web, API, and AI application testing | [OWASP WSTG](https://wstg.owasp.org/), [API Security](https://owasp.org/API-Security/), [GenAI Security](https://genai.owasp.org/) | Pin editions; review releases quarterly. |

Add vendor advisories, protocol specifications, platform documentation,
public incident reports, and peer-reviewed research per domain. Record exact
URLs, dates, scope, and confidence. A source list is a starting point, not a
bulk-upload instruction or an assertion of training rights.

## Refresh and evaluation pipeline

1. **Discover:** inspect official feeds and change logs for additions,
   deprecations, corrections, and conflicting claims.
2. **Curate:** deduplicate, validate provenance, remove secrets and personal
   data, record license and publication date, and distinguish fact from claim.
3. **Map:** link each item to one or more categories below and to the exact
   version of the source taxonomy.
4. **Teach:** create concise concepts, examples, counterexamples, defensive
   signals, and remediation; keep executable lab content in isolated fixtures.
5. **Practice:** build owned, resettable labs with explicit scope, telemetry,
   and ground truth; vary the environment so the answer cannot be memorized.
6. **Evaluate:** hold out cases by root cause and product family; score
   evidence, false positives, recovery, and reproducibility across runs.
7. **Review:** have a human validate consequential changes before promotion.
   Preserve old source versions and model scores for regression analysis.

Use the companion [incident-learning rubric](../skills/pentest/references/incident-learning.md)
for historical cases. Do not use incident reports as operational instructions
for avoiding detection or targeting high-privilege systems.

## Security engineering domains (55)

- E01: Security Architecture
- E02: Defensive Security Engineering
- E03: Offensive Security Engineering
- E04: Application Security Engineering
- E05: Network Security Engineering
- E06: Cloud Security Engineering
- E07: Identity & Access Security
- E08: Endpoint Security
- E09: Infrastructure Security
- E10: Operating-System Security
- E11: Kernel & Driver Security
- E12: Mobile Security
- E13: IoT & Embedded Security
- E14: Hardware Security
- E15: Firmware Security
- E16: Automotive Security
- E17: OT / ICS Security
- E18: Wireless & RF Security
- E19: Telecommunications Security
- E20: Web Security
- E21: API Security
- E22: Database Security
- E23: Data Security
- E24: Cryptographic Engineering
- E25: Security Protocol Engineering
- E26: Reverse Engineering
- E27: Vulnerability Research
- E28: Fuzzing
- E29: Exploit Research
- E30: Malware Research
- E31: Detection Engineering
- E32: Security Monitoring
- E33: Threat Intelligence
- E34: Digital Forensics
- E35: Incident Response
- E36: Security Operations
- E37: Security Automation
- E38: DevSecOps
- E39: Supply-Chain Security
- E40: Software Supply-Chain Security
- E41: Container Security
- E42: Kubernetes Security
- E43: AI / ML Security
- E44: Security Testing
- E45: Red Teaming
- E46: Purple Teaming
- E47: Penetration Testing
- E48: Adversary Simulation
- E49: Security Research
- E50: Privacy Engineering
- E51: Zero-Trust Engineering
- E52: Resilience Engineering
- E53: Security Governance
- E54: Risk Engineering
- E55: Security Program Engineering

## Malicious-activity categories (36)

- A01: Initial Access
- A02: Reconnaissance
- A03: Social Engineering
- A04: Credential & Identity Attacks
- A05: Malware
- A06: Exploitation
- A07: Privilege Escalation
- A08: Persistence
- A09: Defense Evasion
- A10: Execution
- A11: Discovery
- A12: Collection
- A13: Command & Control
- A14: Lateral Movement
- A15: Data Exfiltration
- A16: Impact / Destruction
- A17: Financial Cybercrime
- A18: Espionage
- A19: Disinformation / Influence
- A20: Disruption
- A21: Supply-Chain Attacks
- A22: Cloud Attacks
- A23: Web / API Attacks
- A24: Mobile Attacks
- A25: Network Attacks
- A26: Wireless / RF Attacks
- A27: IoT / Embedded Attacks
- A28: Hardware Attacks
- A29: Automotive Attacks
- A30: OT / ICS Attacks
- A31: Cryptographic Attacks
- A32: AI / ML Attacks
- A33: Privacy / Surveillance Abuse
- A34: Cyberterrorism
- A35: Cyberwarfare
- A36: Criminal Cyber Ecosystems

These categories are for recognition, defense, and controlled assessment. They do not define an execution plan.
