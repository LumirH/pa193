from python:3.12.3-bookworm

RUN apt-get update && apt-get install nginx -y 
RUN pip install azure-cli azure-identity azure-keyvault-secrets azure-keyvault-certificates

COPY pa193-server.conf /etc/nginx/conf.d/
RUN mkdir -p /data

COPY download_cert.py /
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

CMD /entrypoint.sh
