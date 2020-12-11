FROM python:3.9-alpine
MAINTAINER CRISTIAN_CONTRERA <cristiancontrera95@gmail.com>

RUN apk update && apk --no-cache add musl-dev linux-headers g++
WORKDIR /app

COPY requirements*.txt ./
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

COPY strictdf/ .
COPY scripts/run_test_alpine.sh .
RUN chmod +x run_test_alpine.sh

CMD ["./run_test_alpine.sh"]
