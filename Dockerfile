FROM ruby:2.7.5

# throw errors if Gemfile has been modified since Gemfile.lock
#RUN bundle config --global frozen 1

WORKDIR /usr/src/app

COPY Gemfile Gemfile.lock ./
RUN bundle lock --add-platform x86_64-linux
RUN ls
RUN bundle update
RUN bundle install

#COPY . .

CMD ["bundle" ,"exec" ,"jekyll" ,"build" ]
