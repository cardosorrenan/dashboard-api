FROM matheusnunes/rails:2.6.6


ARG CI_BUILD

RUN mkdir -p /bycoders-model
WORKDIR /bycoders-model/

COPY . /bycoders-model/

RUN if [ -z "$CI_BUILD" ]; then bundle install -j "$(getconf _NPROCESSORS_ONLN)" --retry 3; fi

RUN if [ -n "$CI_BUILD" ]; then test -d bundle && cp -r bundle /; fi || true
RUN if [ -n "$CI_BUILD" ]; then bundle check && use_local="--local"; fi || true
RUN if [ -n "$CI_BUILD" ]; then bundle install -j "$(getconf _NPROCESSORS_ONLN)" --path=/bundle $use_local --retry 3; fi
