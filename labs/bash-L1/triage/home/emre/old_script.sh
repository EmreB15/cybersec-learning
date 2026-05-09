#!/bin/bash
# Backup script - copies ~/projects to /mnt/backup/ daily.
rsync -av "$HOME/projects/" "/mnt/backup/projects-$(date +%F)/"
