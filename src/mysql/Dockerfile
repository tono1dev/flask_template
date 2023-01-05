FROM mysql:8-debian

COPY ./conf/config-file.cnf /etc/mysql/conf.d/config-file.cnf

# 日本語環境を追加
RUN apt-get update && apt-get install -y locales  
RUN sed -i -E 's/# (ja\_JP.UTF-8)/\\1/' /etc/locale.gen && locale-gen  

ENV LC_ALL ja_JP.UTF-8

ENV TZ Asia/Tokyo
ENV LANG ja\_JP.UTF-8

CMD ["mysqld"]

EXPOSE 3306
