FROM python:3.9-alpine
MAINTAINER CRISTIAN_CONTRERA <cristiancontrera95@gmail.com>

RUN apk update && apk --no-cache add musl-dev linux-headers g++
WORKDIR /app

COPY requirements*.txt ./
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

COPY src/ src
COPY tests/ tests
COPY scripts/docker_run_test.sh .
RUN chmod +x docker_run_test.sh

CMD ["./docker_run_test.sh"]
