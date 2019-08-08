#!/usr/bin/env bash
ssh -o StrictHostKeyChecking=no root@83.12.177.185 << 'ENDSSH'
 cd /recruitment-teonite
 docker login -u $REGISTRY_USER -p $CI_BUILD_TOKEN $CI_REGISTRY
 docker pull registry.gitlab.com/michal-czarnecki/recruitment-teonite:latest
 docker-compose up -d
ENDSSH