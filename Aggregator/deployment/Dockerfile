FROM python:3-stretch AS builder
LABEL maintainer="olgierd@kasprowicz.pro"

COPY requirements.txt dev-requirements.txt /svc/
# Precompile dependencies to wheels
RUN pip3 install wheel && pip3 wheel -r /svc/requirements.txt -r /svc/dev-requirements.txt --wheel-dir=/svc/.wheels

COPY . /svc


FROM python:3-stretch
WORKDIR /svc

COPY --from=builder /svc /svc/
RUN pip install --no-index --find-links=/svc/.wheels -r requirements.txt -r dev-requirements.txt
RUN chown nobody:nogroup /svc
RUN mkdir /svc/data &&\
    chown nobody:nogroup /svc/data

USER nobody
EXPOSE 8080
CMD ["./scripts/startup"]
