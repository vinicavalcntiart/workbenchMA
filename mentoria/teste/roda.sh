#!/usr/bin/env bash
# Exercita a lógica do agente fora do Apps Script, com agenda falsa.
# Uso: bash mentoria/teste/roda.sh
set -e
node "$(dirname "$0")/testa-agente.js"
