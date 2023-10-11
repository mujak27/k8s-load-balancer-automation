#!/bin/sh
APISERVER_VIP={$VIP-CONTROL-PLANE}
APISERVER_DEST_PORT={$VIP-CONTROL-PLANE-PORT}

exit() {
    echo "--- $* ---" 1>&2
    exit 1
}

if curl --silent --insecure https://localhost:${APISERVER_DEST_PORT}/ -o /dev/null 
    exit "Error GET https://localhost:${APISERVER_DEST_PORT}/"
fi

if ip addr | grep -q ${APISERVER_VIP}; then
    curl --silent --insecure https://${APISERVER_VIP}:${APISERVER_DEST_PORT}/ -o /dev/null || exit "Error GET https://${APISERVER_VIP}:${APISERVER_DEST_PORT}/"
fi