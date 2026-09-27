#!/bin/sh
# Pede o link de acesso do Teamtailor Connect por CURL (sem navegador): GET /connect/login
# para pegar authenticity_token e cookie, POST com candidate[email].
EMAIL="contact@vinicavalcanti.art"
for slug in "$@"; do
  J=$(mktemp)
  TOK=$(curl -sS --max-time 25 -c "$J" -A "Mozilla/5.0 Chrome/140.0" "https://$slug.teamtailor.com/connect/login" \
        | grep -o 'name="authenticity_token" value="[^"]*"' | head -1 | sed 's/.*value="//;s/"//')
  if [ -z "$TOK" ]; then echo "$slug: SEM TOKEN"; rm -f "$J"; continue; fi
  OUT=$(curl -sS --max-time 25 -b "$J" -c "$J" -A "Mozilla/5.0 Chrome/140.0" \
     -H "X-Requested-With: XMLHttpRequest" \
     --data-urlencode "authenticity_token=$TOK" \
     --data-urlencode "candidate[email]=$EMAIL" \
     -w "|http=%{http_code}" \
     "https://$slug.teamtailor.com/connect/login")
  echo "$slug => $(echo "$OUT" | tr -d '\n' | tail -c 300)"
  rm -f "$J"
  sleep 2
done
