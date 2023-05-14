# Configuration block for the server
server {
    # Port that the web server is going to listen on
    listen ${LISTEN_PORT};

    # Location block to map different URL mappings
    location /static {
        alias /vol/static;
    }

    # Handles the rest of the request that aren't met by the above block
    # Blocks are executed in order
    location / {
        uwsgi_pass           ${APP_HOST}:${APP_PORT};
        # uWSGI params are parameters that are required for the HTTP req to be processed in uWSGI
        include              /etc/nginx/uwsgi_params;
        # Maximum body size of the req
        client_max_body_size 10M;
    }
}
