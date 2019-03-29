#!/usr/bin/env bash

set -e

source ../.env

docker run \
	-it \
	--rm \
	--volume certbot-certs:/etc/letsencrypt \
	--volume certbot-challenges:/data/letsencrypt \
	certbot/certbot certonly \
		--webroot \
		--webroot-path /data/letsencrypt \
		--agree-tos \
		--non-interactive \
		--email ${ADMIN_EMAIL} \
		--domain ${DOMAIN} \
		--domain www.${DOMAIN} \
		--domain static.${DOMAIN}
