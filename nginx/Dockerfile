FROM nginx
EXPOSE 80 443
VOLUME /etc/letsencrypt
WORKDIR /usr/src/app/
HEALTHCHECK CMD curl --fail --insecure https://localhost/health-check || exit 1

RUN apt-get update && \
    apt-get install --no-install-recommends --assume-yes curl openssl && \
    rm --recursive --force /var/lib/apt/lists/*

COPY nginx.conf.template .
COPY cert.cnf.template .
COPY start.sh .
RUN chmod +x start.sh
CMD ./start.sh