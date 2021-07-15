#!/usr/bin/env bash
set -euo pipefail

aws iam list-roles \
  | jq '.Roles' \
  | sqlite-utils insert demo_database.db roles --ignore --pk RoleName -

  set +eo pipefail
  sqlite-utils query demo_database.db 'SELECT RoleName from roles' \
    | jq -r '.[]|.RoleName' \
    | while read -r role_name; do
      echo -e "\n** ${role_name} **" 1>&2
      aws iam get-role --role-name "$role_name"
    done \
    | jq -c --unbuffered '.Role' \
    | tee >(1>&2 cat) \
    | sqlite-utils insert demo_database.db roles --nl --truncate --alter --replace --pk RoleName -