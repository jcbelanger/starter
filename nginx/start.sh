#!/usr/bin/env bash

set -e

DOMAIN=${DOMAIN:-localhost}
ADMIN_EMAIL=${ADMIN_EMAIL:-root@${DOMAIN}}
CERT_PATH=/etc/letsencrypt/live/${DOMAIN}

mkdir -p "${CERT_PATH}"
cd "${CERT_PATH}"

	
EXPIRES_TODAY="openssl x509 -checkend 86400 -noout -in fullchain.pem"
if [ ! -f fullchain.pem ] || [ "$(eval $EXPIRES_TODAY)" = "1" ]; then
    touch privkey.pem
    touch cert.pem
    touch fullchain.pem
	
	envsubst '${DOMAIN} ${ADMIN_EMAIL}' < /usr/src/app/cert.cnf.template > /usr/src/app/cert.cnf
	
	cat /usr/src/app/cert.cnf
	
    openssl req \
      -new \
      -nodes \
      -x509 \
      -days 365 \
      -newkey rsa:2048 \
      -config /usr/src/app/cert.cnf \
      -keyout privkey.pem \
      -out cert.pem

    cat cert.pem privkey.pem > fullchain.pem
fi

#todo implement certbot
if false; then
	certbot-auto certonly \
		--standalone \
		--agree-tos \
		--non-interactive \
		--email ${ADMIN_EMAIL} \
		--domain ${DOMAIN} \
		--domain www.${DOMAIN}

	certbot-auto renew \
		--quiet \
		--agree-tos \
		--non-interactive \
		--webroot \
		--webroot-path /var/www/html/ \
		--email ${ADMIN_EMAIL} \
		--domain ${DOMAIN} \
		--domain www.${DOMAIN} \
		--post-hook "nginx -s reload"
fi


envsubst '${DOMAIN}' < /usr/src/app/nginx.conf.template > /etc/nginx/nginx.conf
exec nginx -g 'daemon off;'
