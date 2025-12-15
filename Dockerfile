FROM klakegg/hugo:0.152.2-ext-alpine

WORKDIR /src

COPY . .

EXPOSE 1313

CMD ["server", "--bind", "0.0.0.0"]
