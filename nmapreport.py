import subprocess
import argparse
import pandas as pd
import re
from datetime import datetime
import socket

def resolve_domain(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        return None

def run_nmap(target, verbose):
    if verbose:
        print(f"[+] Ejecutando Nmap rápido contra {target} con -Pn -T4 -n -p- --open...")

    result = subprocess.run(
        ["nmap", "-sV", "-Pn", "-T4", "-n", "-p-", "--open", target],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if verbose:
        print("[+] Escaneo completado.")
    return result.stdout

def parse_nmap_output(output, verbose):
    if verbose:
        print("[+] Analizando resultados...")
    host_info = []
    current_host = ""
    for line in output.splitlines():
        if "Nmap scan report for" in line:
            match = re.search(r"Nmap scan report for (.+)", line)
            current_host = match.group(1) if match else ""
        elif re.match(r"\d+/tcp", line):
            parts = line.split()
            if len(parts) >= 3:
                port = parts[0]
                state = parts[1]
                service = parts[2]
                version = " ".join(parts[3:]) if len(parts) > 3 else ""
                host_info.append({
                    "Host": current_host,
                    "Port": port,
                    "State": state,
                    "Service": service,
                    "Version": version
                })
    if verbose:
        if host_info:
            print(f"[+] Se encontraron {len(host_info)} servicios.")
        else:
            print("[!] No se encontraron puertos abiertos.")
    return host_info

def export_to_excel(data, output_file, verbose):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    if verbose:
        print(f"[+] Reporte exportado exitosamente a: {output_file}")

def main(target, output, verbose):
    resolved_ip = resolve_domain(target)
    if not resolved_ip:
        print(f"[-] No se pudo resolver el dominio o IP: {target}")
        return

    if verbose and resolved_ip != target:
        print(f"[+] Dominio {target} resuelto a {resolved_ip}")

    nmap_output = run_nmap(target, verbose)
    parsed_data = parse_nmap_output(nmap_output, verbose)
    export_to_excel(parsed_data, output, verbose)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Escaneo de todos los puertos abiertos con Nmap y exportación a Excel")
    parser.add_argument("-t", "--target", required=True, help="Host, dominio o IP objetivo")
    parser.add_argument("-o", "--output", default=f"nmap_open_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx", help="Archivo de salida Excel")
    parser.add_argument("-v", "--verbose", action="store_true", help="Modo verboso para mostrar progreso")

    args = parser.parse_args()
    main(args.target, args.output, args.verbose)
