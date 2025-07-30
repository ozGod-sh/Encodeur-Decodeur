# -*- coding: utf-8 -*-
# Auteur: ozGod

import argparse
import base64
import codecs
import sys

def display_banner():
    """Affiche une bannière stylisée pour l'outil."""
    VERSION = "1.0.0"
    AUTHOR = "ozGod"
    banner = f"""
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  🔀 Encodeur-Décodeur v{VERSION}                            ║
║                                                              ║
║  Utilitaire pour encoder/décoder en Base64, Hex, ROT13.     ║
║  Créé par {AUTHOR}                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)

def process_data(data, format_type, action):
    """Encode ou décode les données selon le format et l'action spécifiés."""
    try:
        if format_type == 'b64':
            if action == 'encode':
                return base64.b64encode(data.encode('utf-8')).decode('utf-8')
            else:
                return base64.b64decode(data.encode('utf-8')).decode('utf-8')
        
        elif format_type == 'hex':
            if action == 'encode':
                return data.encode('utf-8').hex()
            else:
                return bytes.fromhex(data).decode('utf-8')

        elif format_type == 'rot13':
            # ROT13 est sa propre inverse, donc l'action n'a pas d'importance
            return codecs.encode(data, 'rot_13')
            
    except Exception as e:
        print(f"[!] Erreur lors du traitement : {e}", file=sys.stderr)
        sys.exit(1)

def main():
    display_banner()
    parser = argparse.ArgumentParser(
        description="Encode et décode des données dans différents formats.",
        epilog=f"Créé par ozGod. Formats: b64, hex, rot13"
    )
    parser.add_argument("format", help="Le format à utiliser.", choices=['b64', 'hex', 'rot13'])
    parser.add_argument("action", help="L'action à effectuer.", choices=['encode', 'decode'])
    parser.add_argument("data", help="La chaîne de caractères à traiter.")

    args = parser.parse_args()

    if args.format == 'rot13' and args.action == 'decode':
        print("[*] Info: L'encodage et le décodage ROT13 sont la même opération.")

    result = process_data(args.data, args.format, args.action)
    
    print("--- Entrée ---")
    print(args.data)
    print("\n--- Sortie ---")
    print(result)

if __name__ == "__main__":
    main()
