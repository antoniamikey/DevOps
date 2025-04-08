FROM nginx:alpine
LABEL org.opencontainers.image.source=https://github.com/antoniamikey/DevOps
COPY index.html /usr/share/nginx/html/index.html
