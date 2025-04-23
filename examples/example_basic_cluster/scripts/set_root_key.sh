#!/bin/bash
ssh-keygen -t rsa -b 4096 -N "" -f ~/.ssh/id_rsa -q <<< y
cat .ssh/id_rsa.pub > .ssh/authorized_keys

