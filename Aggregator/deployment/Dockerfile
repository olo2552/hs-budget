FROM python:3-stretch AS builder
LABEL maintainer="olgierd@kasprowicz.pro"

COPY requirements.txt /svc/
# Precompile dependencies to wheels
RUN pip3 install wheel && pip3 wheel -r /svc/requirements.txt --wheel-dir=/svc/.wheels

COPY aggregator /svc/aggregator
COPY main /svc/main
COPY manage.py /svc
#COPY scripts/entrypoint /svc


FROM python:3-stretch
WORKDIR /svc

COPY --from=builder /svc /svc/
RUN pip install --no-index --find-links=/svc/.wheels -r requirements.txt
RUN chown nobody /svc

USER nobody
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
#CMD ["./entrypoint"]
