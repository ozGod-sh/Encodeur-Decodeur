# 🔀 Encodeur-Décodeur - Utilitaire de Transformation de Données

**Créé par ozGod-sh**

## Description

Encodeur-Décodeur est un outil polyvalent pour encoder et décoder des données dans différents formats couramment utilisés en cybersécurité. Il supporte Base64, hexadécimal et ROT13, facilitant l'analyse de données et les tests de sécurité.

## Fonctionnalités

### 🔄 Formats supportés
- **Base64** : Encodage/décodage standard (RFC 4648)
- **Hexadécimal** : Conversion binaire vers hex et vice versa
- **ROT13** : Chiffrement par substitution simple (auto-inverse)

### ⚡ Caractéristiques
- **Interface simple** : Commande unique pour tous les formats
- **Gestion d'erreurs** : Messages d'erreur clairs
- **Encodage UTF-8** : Support des caractères internationaux
- **Validation** : Vérification des données d'entrée

## Installation

### Prérequis
- Python 3.6+
- Aucune dépendance externe (utilise la bibliothèque standard)

### Installation
```bash
cd Encodeur-Decodeur
# Aucune installation requise - utilise uniquement la stdlib Python
```

## Utilisation

### Syntaxe de base
```bash
python encodeur_decodeur.py <FORMAT> <ACTION> <DONNÉES>
```

### Paramètres
- `FORMAT` : Type d'encodage (b64, hex, rot13)
- `ACTION` : Opération à effectuer (encode, decode)
- `DONNÉES` : Chaîne de caractères à traiter

### Exemples d'utilisation

#### 1. Encodage Base64
```bash
python encodeur_decodeur.py b64 encode "Hello World!"
```

#### 2. Décodage Base64
```bash
python encodeur_decodeur.py b64 decode "SGVsbG8gV29ybGQh"
```

#### 3. Encodage hexadécimal
```bash
python encodeur_decodeur.py hex encode "Secret"
```

#### 4. Décodage hexadécimal
```bash
python encodeur_decodeur.py hex decode "536563726574"
```

#### 5. ROT13 (encode/decode identique)
```bash
python encodeur_decodeur.py rot13 encode "Test Message"
```

## Structure des fichiers

```
Encodeur-Decodeur/
├── encodeur_decodeur.py    # Script principal
└── README.md              # Cette documentation
```

## Logique de fonctionnement

### 1. Base64
```python
if action == 'encode':
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')
else:
    return base64.b64decode(data.encode('utf-8')).decode('utf-8')
```

### 2. Hexadécimal
```python
if action == 'encode':
    return data.encode('utf-8').hex()
else:
    return bytes.fromhex(data).decode('utf-8')
```

### 3. ROT13
```python
return codecs.encode(data, 'rot_13')  # Auto-inverse
```

## Cas d'usage

### Analyse de sécurité
- **Décodage de payloads** : Analyser des données encodées
- **Obfuscation** : Encoder des données pour éviter la détection
- **Forensique** : Décoder des artefacts trouvés
- **Reverse engineering** : Analyser des chaînes encodées

### Tests de pénétration
- **Bypass de filtres** : Encoder des payloads malveillants
- **Injection** : Préparer des données pour injection
- **Évasion** : Contourner les systèmes de détection
- **Analyse de trafic** : Décoder des communications

### Développement
- **Debug** : Vérifier l'encodage de données
- **Tests** : Préparer des données de test
- **Validation** : Vérifier les transformations
- **Documentation** : Créer des exemples

## Exemples détaillés

### Base64
```bash
# Encodage
$ python encodeur_decodeur.py b64 encode "admin:password"
--- Entrée ---
admin:password

--- Sortie ---
YWRtaW46cGFzc3dvcmQ=

# Décodage
$ python encodeur_decodeur.py b64 decode "YWRtaW46cGFzc3dvcmQ="
--- Entrée ---
YWRtaW46cGFzc3dvcmQ=

--- Sortie ---
admin:password
```

### Hexadécimal
```bash
# Encodage
$ python encodeur_decodeur.py hex encode "Hello"
--- Entrée ---
Hello

--- Sortie ---
48656c6c6f

# Décodage
$ python encodeur_decodeur.py hex decode "48656c6c6f"
--- Entrée ---
48656c6c6f

--- Sortie ---
Hello
```

### ROT13
```bash
# Encodage/Décodage (identique)
$ python encodeur_decodeur.py rot13 encode "Secret Message"
--- Entrée ---
Secret Message

--- Sortie ---
Frperg Zrffntr

$ python encodeur_decodeur.py rot13 decode "Frperg Zrffntr"
--- Entrée ---
Frperg Zrffntr

--- Sortie ---
Secret Message
```

## Gestion des erreurs

### Erreurs courantes
- **Base64 invalide** : Caractères non-Base64
- **Hex invalide** : Caractères non-hexadécimaux
- **Longueur impaire** : Hex avec nombre impair de caractères
- **Encodage UTF-8** : Caractères non-décodables

### Exemples d'erreurs
```bash
# Base64 invalide
$ python encodeur_decodeur.py b64 decode "Invalid@Base64!"
[!] Erreur lors du traitement : Incorrect padding

# Hex invalide
$ python encodeur_decodeur.py hex decode "ZZZ"
[!] Erreur lors du traitement : non-hexadecimal number found in fromhex() arg at position 0
```

## Intégration avec d'autres outils

### Scripts d'automatisation
```bash
#!/bin/bash
# Décoder plusieurs chaînes Base64
while read line; do
    echo "Décodage: $line"
    python encodeur_decodeur.py b64 decode "$line"
done < base64_strings.txt
```

### Pipeline de données
```python
import subprocess

def encode_data(data, format_type):
    result = subprocess.run(['python', 'encodeur_decodeur.py', format_type, 'encode', data], 
                          capture_output=True, text=True)
    return result.stdout.split('--- Sortie ---\n')[1].strip()
```

### Avec Burp Suite
```bash
# Préparer des payloads encodés
python encodeur_decodeur.py b64 encode "<script>alert(1)</script>" > payload_b64.txt
python encodeur_decodeur.py hex encode "' OR 1=1 --" > payload_hex.txt
```

## Extensions possibles

### Nouveaux formats
```python
# URL encoding
import urllib.parse
def url_encode(data):
    return urllib.parse.quote(data)

# HTML entities
def html_encode(data):
    return ''.join(f'&#{ord(c)};' for c in data)

# JWT decode
import json
def jwt_decode(token):
    parts = token.split('.')
    header = base64.b64decode(parts[0] + '==').decode()
    payload = base64.b64decode(parts[1] + '==').decode()
    return json.loads(header), json.loads(payload)
```

### Mode batch
```python
def process_file(filename, format_type, action):
    with open(filename, 'r') as f:
        for line in f:
            result = process_data(line.strip(), format_type, action)
            print(f"{line.strip()} -> {result}")
```

### Interface graphique
```python
import tkinter as tk
from tkinter import ttk

class EncoderDecoderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Encodeur-Décodeur")
        # Interface graphique...
```

## Comparaison des formats

### Base64
- **Usage** : Transmission de données binaires en texte
- **Efficacité** : 33% d'augmentation de taille
- **Caractères** : A-Z, a-z, 0-9, +, /, =
- **Cas d'usage** : Email, URLs, JSON, XML

### Hexadécimal
- **Usage** : Représentation binaire lisible
- **Efficacité** : 100% d'augmentation de taille
- **Caractères** : 0-9, A-F (ou a-f)
- **Cas d'usage** : Debugging, forensique, crypto

### ROT13
- **Usage** : Obfuscation simple (non-cryptographique)
- **Efficacité** : Aucune augmentation de taille
- **Caractères** : Lettres uniquement (A-Z, a-z)
- **Cas d'usage** : Spoilers, obfuscation basique

## Sécurité et limitations

### ⚠️ Avertissements
- **ROT13 n'est pas du chiffrement** : Facilement cassable
- **Base64 n'est pas du chiffrement** : Juste de l'encodage
- **Hex n'est pas sécurisé** : Représentation alternative
- **Pas de validation de sécurité** : Ne vérifie pas le contenu

### Bonnes pratiques
- **Ne pas confondre encodage et chiffrement**
- **Utiliser pour l'obfuscation légère uniquement**
- **Toujours valider les données décodées**
- **Ne pas stocker de secrets en Base64/Hex**

## Alternatives et outils similaires

### Outils en ligne de commande
```bash
# Base64 (Linux/macOS)
echo "Hello" | base64
echo "SGVsbG8K" | base64 -d

# Hex (Linux/macOS)
echo "Hello" | xxd -p
echo "48656c6c6f0a" | xxd -r -p

# ROT13 (Linux/macOS)
echo "Hello" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

### Outils graphiques
- **CyberChef** : Outil web complet
- **Burp Suite Decoder** : Intégré dans Burp
- **HxD** : Éditeur hexadécimal Windows
- **010 Editor** : Éditeur binaire avancé

## Améliorations futures

### Fonctionnalités
- Support de fichiers en entrée/sortie
- Mode batch pour traiter plusieurs chaînes
- Détection automatique du format
- Validation et vérification des données

### Interface
- Interface graphique complète
- Mode interactif
- Historique des conversions
- Export des résultats

### Formats additionnels
- URL encoding/decoding
- HTML entities
- Unicode escaping
- JWT token parsing

## Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

---

**Encodeur-Décodeur v1.0.0** | Créé par ozGod-sh