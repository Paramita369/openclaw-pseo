#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SOURCE_DB="$ROOT_DIR/var/data/macro_events.db"
BACKUP_DIR="$ROOT_DIR/var/backups/source-db"
BACKUP_FILE=""

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
    --backup-file)
      BACKUP_FILE="$2"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

if [[ -z "$BACKUP_FILE" ]]; then
  BACKUP_FILE="$(ls -1t "$BACKUP_DIR"/macro_events_*.db 2>/dev/null | head -n 1 || true)"
fi

if [[ -z "$BACKUP_FILE" || ! -f "$BACKUP_FILE" ]]; then
  echo "Backup file not found" >&2
  exit 1
fi

mkdir -p "$(dirname "$SOURCE_DB")"
cp "$BACKUP_FILE" "$SOURCE_DB"

echo "Restored source DB: $SOURCE_DB"
echo "From backup: $BACKUP_FILE"
