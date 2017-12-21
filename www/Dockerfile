FROM nginx:1.12-alpine

# Add dependencies for our scripts
RUN apk add --no-cache bash openssl

# nginx configuration and entrypoint
COPY conf /etc/nginx
COPY entrypoint.sh .

# mountable ssl certificate and key directory
# (we don't want any keys in this repository)
VOLUME /etc/ssl/private

# mountable content
VOLUME /usr/share/nginx/html

CMD ["./entrypoint.sh"]