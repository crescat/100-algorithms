#!/bin/bash

RED="[31m"
GREEN="[32m"
RESET="[0m"

print_run() {
  local status file
  status="$1"
  file="$2"
  output=$(cat)

  if [[ "$status" -eq 0 ]]; then
    echo -e "[${GREEN}PASS${RESET}] $file"
  else
    echo -e "[${RED}FAIL${RESET}] $file, output:"
    echo "$output"
    echo
  fi
}

test_dir() {
  local dir="$1"
  local output
  local status
  local file
  local failed

  for file in $dir/*.py; do
    output=$(python "$file" 2>&1)
    status="$?"

    echo "$output" | print_run "$status" "$file"
    [[ "$status" -ne 0 ]] && failed=1
  done

  [[ "$failed" -eq 1 ]] && return 1 || return 0
}

# allow glob to yield empty result
shopt -s nullglob

for dir in *; do
  [[ -d "$dir" ]] && {
    test_dir "$dir" || failed=1
  }
done

if [[ "$failed" -eq 1 ]]; then
  echo "Some files failed to run"
  exit 1
else
  exit 0
fi


