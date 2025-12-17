#!/bin/sh

export SECRET_PASSWORD=`tr -dc A-Za-z0-9 </dev/urandom | head -c 20; echo `
export SECRET_ADMIN_PASSWORD=`tr -dc A-Za-z0-9 </dev/urandom | head -c 20; echo `

socat -dd 'TCP-LISTEN:13373,reuseaddr,fork' 'EXEC:/stack'