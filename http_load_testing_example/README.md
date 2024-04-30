

```bash
poetry run gunicorn \
--bind :5000 \
--workers 3 \
--worker-class gevent \
--worker-connections 999 \
endpoints_localhost:app &
```

```bash
pkill -f gunicorn
```
