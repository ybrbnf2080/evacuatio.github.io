FROM nginx:1.21.6-alpine

RUN mkdir /www/
RUN chown :nginx /www
RUN chmod 775 /www
RUN chmod ugo+rwxt /www




CMD ["nginx", "-g", "daemon off;"]
