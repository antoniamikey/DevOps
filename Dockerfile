FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
LABEL org.opencontainers.image.source=https://github.com/antoniamikey/DevOps