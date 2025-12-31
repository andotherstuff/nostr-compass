FROM hugomods/hugo:dart-sass-git

WORKDIR /src

COPY . .

EXPOSE 1313

CMD ["server", "--bind", "0.0.0.0"]
