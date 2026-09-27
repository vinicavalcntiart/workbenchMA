#!/bin/sh
# Como o pede_link.sh, mas por HOST completo (alguns locatarios usam dominio proprio e o
# slug.teamtailor.com devolve 301 para careers.<casa>.com, e o curl sem -L perde o token).
EMAIL="contact@vinicavalcanti.art"
for host in "$@"; do
  J=$(mktemp)
  TOK=$(curl -sSL --max-time 25 -c "$J" -A "Mozilla/5.0 Chrome/140.0" "https://$host/connect/login" \
        | grep -o 'name="authenticity_token" value="[^"]*"' | head -1 | sed 's/.*value="//;s/"//')
  if [ -z "$TOK" ]; then echo "$host: SEM TOKEN"; rm -f "$J"; continue; fi
  CODE=$(curl -sSL --max-time 25 -b "$J" -c "$J" -A "Mozilla/5.0 Chrome/140.0" \
     --data-urlencode "authenticity_token=$TOK" --data-urlencode "candidate[email]=$EMAIL" \
     -o /dev/null -w "%{http_code}" "https://$host/connect/login")
  echo "$host => http=$CODE"
  rm -f "$J"; sleep 2
done
