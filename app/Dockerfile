# syntax=docker/dockerfile:1.2
FROM python:alpine3.14
WORKDIR /code
#RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk add gcc musl-dev linux-headers
COPY requirements.txt ./
RUN pip install -r requirements.txt
#RUN --mount=type=secret,id=username,dst=/foobar cat /foobar
COPY . .
CMD ["flask", "run"]