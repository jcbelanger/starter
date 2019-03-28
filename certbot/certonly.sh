#!/usr/bin/env bash

set -e

source ../.env

docker run -it --rm certbot/certbot certonly \
	--volume certbot-certs:/etc/letsencrypt \
	--volume certbot-challenges:/usr/share/nginx/html/ \
	--webroot \
	--webroot-path /usr/share/nginx/html/ \
	--agree-tos \
	--non-interactive \
	--email ${ADMIN_EMAIL} \
	--domain ${DOMAIN} \
	--domain www.${DOMAIN} \
	--domain static.${DOMAIN}