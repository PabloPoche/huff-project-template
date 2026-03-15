#!/bin/bash
set -e

echo "Instalando hevm 0.48.1..."
curl -L https://github.com/dapphub/dapptools/releases/download/hevm/0.48.1/hevm \
  -o /usr/local/bin/hevm && chmod +x /usr/local/bin/hevm
echo "hevm $(hevm version) instalado ✓"

echo "Aplicando patches a la extensión huff-language..."
MAIN_JS="/home/codespace/.vscode-remote/extensions/huff-language.huff-language-0.0.32/out/main.js"

for i in {1..30}; do
  [ -f "$MAIN_JS" ] && break
  echo "Esperando extensión... ($i)"
  sleep 2
done

python3 /workspaces/huff-project-template/.devcontainer/patch_extension.py
echo "Setup completado ✓"
