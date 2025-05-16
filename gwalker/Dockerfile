FROM node:18-alpine as builder

WORKDIR /app

RUN apk add --no-cache git
RUN git clone https://github.com/Kanaries/graphic-walker.git .
RUN yarn --verbose --frozen-lockfile install
RUN yarn --verbose build

FROM node:18-alpine
RUN apk add --no-cache tini
ENTRYPOINT ["/sbin/tini", "--"]
COPY --from=builder /app/node_modules /node_modules
COPY --from=builder /app/packages/duckdb-wasm-computation /packages/duckdb-wasm-computation
COPY --from=builder /app/packages/graphic-walker /packages/graphic-walker
WORKDIR /packages/graphic-walker/
CMD [ "npm", "run", "dev" ]
