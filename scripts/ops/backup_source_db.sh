#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SOURCE_DB="$ROOT_DIR/var/data/macro_events.db"
BACKUP_DIR="$ROOT_DIR/var/backups/source-db"
KEEP=14

while [[ $# -gt 0 ]]; do
  case "$1" in
    --source-db-path)
      SOURCE_DB="$2"
      shift 2
      ;;
    --backup-dir)
      BACKUP_DIR="$2"
      shift 2
      ;;
    --keep)
      KEEP="$2"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

if [[ ! -f "$SOURCE_DB" ]]; then
  echo "Source DB not found: $SOURCE_DB" >&2
  exit 1
fi

mkdir -p "$BACKUP_DIR"
TS="$(date -u +%Y%m%d_%H%M%S)"
TARGET="$BACKUP_DIR/macro_events_${TS}.db"
cp "$SOURCE_DB" "$TARGET"

BACKUPS_RAW="$(ls -1t "$BACKUP_DIR"/macro_events_*.db 2>/dev/null || true)"
if [[ -n "$BACKUPS_RAW" ]]; then
  COUNT=0
  while IFS= read -r old; do
    [[ -z "$old" ]] && continue
    COUNT=$((COUNT + 1))
    if [[ $COUNT -gt $KEEP ]]; then
      rm -f "$old"
    fi
  done <<< "$BACKUPS_RAW"
fi

echo "Backup created: $TARGET"
