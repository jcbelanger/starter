#!/usr/bin/env bash

set -e

PARENT_DIR=$(dirname "$(readlink -f "$0")")/../

source ${PARENT_DIR}/.env

docker run \
	-it \
	--rm \
	--volume starter_certbot-certs:/etc/letsencrypt \
	--volume starter_certbot-challenges:/data/letsencrypt \
	certbot/certbot certonly \
		--webroot \
		--webroot-path /data/letsencrypt \
		--agree-tos \
		--non-interactive \
		--cert-name ${DOMAIN} \
		--email ${ADMIN_EMAIL} \
		--domain ${DOMAIN} \
		--domain www.${DOMAIN} \
		--domain static.${DOMAIN} \
		$( (("$DEBUG" == "1")) && echo "--dry-run" ) \
		"$@"
#		--post-hook "cd "$PARENT_DIR" && ls" #docker-compose kill -s SIGHUP nginx"


cd $PARENT_DIR && docker-compose kill -s SIGHUP nginx
